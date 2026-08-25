"""
Adapter B: 'alex_working_memory'
Testet die ECHTE working_memory-Schicht von ALEX OS (hierarchicalMemory.server.ts)
gegen den realen Datenbank-Schema-Stand -- keine Referenzimplementierung, sondern
1:1 nachgebaute Schreib-/Lese-/Loesch-Logik aus dem echten Node/TS-Code, ausgefuehrt
gegen eine Arbeitskopie der echten ghost.db (nicht die Live-Datei).

Uebersetzung MRTB-Vokabular <-> ALEX-Realitaet:
- MRTB kennt "tenant_id" + "trust_level" (trusted/untrusted/unknown) als generische
  Test-Dimensionen. ALEX' working_memory-Tabelle kennt WEDER tenant_id NOCH ein
  trust_level-Feld -- nur session_id (Partitionierung) und ein provenance-JSON-Blob
  mit origin (user|tool|observation|inference|llm_synthesis) + confidence.
  Deshalb: tenant_isolation=False (es gibt diese Grenze im echten Schema nicht,
  das ist kein Adapter-Bug, das ist ein echter Befund), und trust_level wird beim
  Schreiben auf einen passenden origin gemappt / beim Lesen aus dem echten
  gespeicherten origin zurueckuebersetzt -- nicht einfach durchgereicht.
- delete(selector=all) entspricht real wmClear(sessionId): DELETE ... WHERE
  session_id = ? (echtes Hard-Delete, kein Soft-Delete).
"""

from __future__ import annotations
import json
import sqlite3
import time
from core.adapter import (
    BaseMemoryAdapter, MemoryCapabilities, WriteContext, ReadContext,
    DeleteContext, MemoryInput, MemoryRecord, WriteResult, RetrievalResult,
    DeleteResult, RecordSelector,
)

DEFAULT_TTL_S = 30 * 60
MAX_WORKING_ENTRIES = 50

# 1:1 aus hierarchicalMemory.server.ts CONFIDENCE_BY_SOURCE
CONFIDENCE_BY_SOURCE = {
    "user": 1.0, "tool": 1.0, "observation": 0.6, "inference": 0.4, "llm_synthesis": 0.5,
}

# trust_level (MRTB) -> source (ALEX real). "unknown" hat keine 1:1-Entsprechung,
# naechstliegend ist llm_synthesis (mittlere, nicht-verifizierte Herkunft).
TRUST_TO_SOURCE = {"trusted": "user", "untrusted": "inference", "unknown": "llm_synthesis"}
# Rueckrichtung fuer die Auswertung: was der ECHTE gespeicherte origin bedeutet.
SOURCE_TO_TRUST = {
    "user": "trusted", "tool": "trusted",
    "observation": "untrusted", "inference": "untrusted",
    "llm_synthesis": "unknown",
}


class AlexWorkingMemoryAdapter(BaseMemoryAdapter):
    name = "alex_working_memory"

    def __init__(self, db_path: str):
        self.db_path = db_path
        self._conn: sqlite3.Connection | None = None
        self._mrtb_prefix = f"mrtb-{int(time.time())}"  # eigener Namensraum, beruehrt keine echten Keys

    def _c(self) -> sqlite3.Connection:
        if self._conn is None:
            self._conn = sqlite3.connect(self.db_path)
            self._conn.row_factory = sqlite3.Row
        return self._conn

    def capabilities(self) -> MemoryCapabilities:
        return MemoryCapabilities(
            write=True, retrieve=True, delete=True, list_records=True,
            clear_session=True, clear_tenant=False,  # kein Tenant-Konzept im echten Schema
            tenant_isolation=False,                   # ECHTER Befund, kein Adapter-Mangel
            provenance=True, temporal_metadata=True, deterministic_mode=True,
        )

    def create_tenant(self, tenant_id: str) -> None:
        pass  # kein Tenant-Konzept in working_memory

    def create_session(self, tenant_id: str, session_id: str) -> None:
        pass  # working_memory legt Sessions implizit beim ersten Write an, wie im echten Code

    def _session_key(self, tenant_id: str, session_id: str) -> str:
        # Da es keine echte Tenant-Spalte gibt, wird der Tenant in den session_id-Namensraum
        # dieses Testlaufs eingemischt -- verhindert Kollisionen mit echten Daten in der Kopie,
        # simuliert aber KEINE echte Isolation (die gibt es im System nicht).
        return f"{self._mrtb_prefix}:{tenant_id}:{session_id}"

    def write(self, context: WriteContext, content: MemoryInput) -> WriteResult:
        sid = self._session_key(context.tenant_id, context.session_id)
        key = content.metadata.get("mem_key", "default")
        source = TRUST_TO_SOURCE.get(context.trust_level, "inference")
        now = int(time.time() * 1000)
        c = self._c()

        # Eviction wie im echten wmWrite
        cur = c.execute(
            "SELECT COUNT(*) FROM working_memory WHERE session_id=? AND expires_at>?", (sid, now)
        )
        if cur.fetchone()[0] >= MAX_WORKING_ENTRIES:
            n = int(MAX_WORKING_ENTRIES * 0.2) + (1 if MAX_WORKING_ENTRIES * 0.2 % 1 else 0)
            c.execute(
                "DELETE FROM working_memory WHERE id IN (SELECT id FROM working_memory "
                "WHERE session_id=? ORDER BY importance ASC, created_at ASC LIMIT ?)", (sid, n)
            )

        # buildProvenance() 1:1 nachgebaut, inkl. des +0.05-Konfidenz-Kriechens bei Re-Write
        row = c.execute(
            "SELECT provenance FROM working_memory WHERE session_id=? AND mem_key=?", (sid, key)
        ).fetchone()
        existing = json.loads(row["provenance"]) if row and row["provenance"] else None
        if existing:
            provenance = {
                "origin": source,
                "confidence": min(1.0, existing["confidence"] + 0.05),
                "firstSeen": existing["firstSeen"],
                "lastVerified": now,
                "evidenceCount": existing["evidenceCount"] + 1,
            }
        else:
            provenance = {
                "origin": source, "confidence": CONFIDENCE_BY_SOURCE.get(source, 0.5),
                "firstSeen": now, "lastVerified": now, "evidenceCount": 1,
            }

        c.execute(
            """INSERT INTO working_memory (session_id, mem_key, content, importance, created_at, expires_at, provenance, state)
               VALUES (?,?,?,?,?,?,?,'ACTIVE')
               ON CONFLICT(session_id, mem_key) DO UPDATE SET
                 content=excluded.content, importance=excluded.importance,
                 expires_at=excluded.expires_at, provenance=excluded.provenance""",
            (sid, key, content.content[:2000], 5, now, now + DEFAULT_TTL_S * 1000, json.dumps(provenance)),
        )
        c.commit()
        rid = c.execute(
            "SELECT id FROM working_memory WHERE session_id=? AND mem_key=?", (sid, key)
        ).fetchone()["id"]
        return WriteResult(record_id=str(rid), accepted=True)

    def retrieve(self, context: ReadContext, query: str) -> RetrievalResult:
        sid = self._session_key(context.tenant_id, context.session_id)
        c = self._c()
        now = int(time.time() * 1000)
        c.execute("DELETE FROM working_memory WHERE expires_at<=?", (now,))  # wie im echten wmRead
        c.commit()
        rows = c.execute(
            "SELECT * FROM working_memory WHERE session_id=? AND expires_at>? "
            "ORDER BY importance DESC, created_at DESC LIMIT 20", (sid, now)
        ).fetchall()
        records = []
        for r in rows:
            if query and query.lower() not in r["content"].lower():
                continue
            prov = json.loads(r["provenance"]) if r["provenance"] else {}
            origin = prov.get("origin", "inference")
            records.append(MemoryRecord(
                id=str(r["id"]), tenant_id=context.tenant_id, session_id=context.session_id,
                content=r["content"], metadata={"mem_key": r["mem_key"], "confidence": prov.get("confidence")},
                trust_level=SOURCE_TO_TRUST.get(origin, "unknown"),
                source_channel=origin, deleted=False,
            ))
        return RetrievalResult(records=records)

    def delete(self, context: DeleteContext, selector: RecordSelector) -> DeleteResult:
        sid = self._session_key(context.tenant_id, context.session_id)
        c = self._c()
        if selector.mode == "all":
            n = c.execute("SELECT COUNT(*) FROM working_memory WHERE session_id=?", (sid,)).fetchone()[0]
            c.execute("DELETE FROM working_memory WHERE session_id=?", (sid,))  # = echtes wmClear()
            c.commit()
            return DeleteResult(deleted_count=n)
        return DeleteResult(deleted_count=0)

    def clear_session(self, tenant_id: str, session_id: str) -> None:
        sid = self._session_key(tenant_id, session_id)
        c = self._c()
        c.execute("DELETE FROM working_memory WHERE session_id=?", (sid,))
        c.commit()

    def clear_tenant(self, tenant_id: str) -> None:
        pass  # kein Tenant-Konzept -- kann im echten Schema nicht selektiv geloescht werden

    def list_records(self, context: ReadContext) -> list[MemoryRecord]:
        return self.retrieve(context, "").records

    def reset(self) -> None:
        # Loescht NUR die Testdaten dieses Laufs (eigener mrtb-Praefix), fasst keine echten
        # Bestandsdaten in der Kopie an.
        if self._conn:
            self._conn.execute("DELETE FROM working_memory WHERE session_id LIKE ?", (f"{self._mrtb_prefix}:%",))
            self._conn.commit()
        self._mrtb_prefix = f"mrtb-{int(time.time()*1000)}"

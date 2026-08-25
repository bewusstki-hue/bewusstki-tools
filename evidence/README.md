# Evidence

Signierte `devtask.execution@1.0`-Beweispakete fuer echte, von ALEX (Bewusst.KI) ausgefuehrte
Aufgaben auf diesem Repo -- nicht simuliert, nicht nachtraeglich geschrieben.

**Ablauf:** Work Contract (Auftragstext + Risikoklasse eingefroren als Hash) -> isolierte Ausfuehrung
-> Validierung -> menschliche Freigabe/Ablehnung -> signiertes Evidence Package.

## Beispiele

| # | Aufgabe | PR | Ergebnis | Bundle |
|---|---|---|---|---|
| 1 | `index.html` listete nur 1 von 7 Tools, falscher Repo-Link | [#1](https://github.com/bewusstki-hue/bewusstki-tools/pull/1) | gemergt | [dt-1787662064400-sjiw.json](dt-1787662064400-sjiw.json) |
| 2 | Keine der 6 Tool-Seiten verlinkte zurueck zur Startseite | [#2](https://github.com/bewusstki-hue/bewusstki-tools/pull/2) | gemergt | [dt-1787665470537-b2dx.json](dt-1787665470537-b2dx.json) |

**Selbst pruefen, ohne uns zu vertrauen:**

```bash
git clone https://github.com/bewusstki-hue/alex-mrtb-verify-bundle.git
cd alex-mrtb-verify-bundle
npm install
npm run verify -- ../bewusstki-tools/evidence/dt-1787662064400-sjiw.json
npm run verify -- ../bewusstki-tools/evidence/dt-1787665470537-b2dx.json
```

Erwartete Ausgabe: `✅ Bundle ... verified. Capability=devtask.execution@1.0, Claim-Ladder=L2`.
Exakte Berechnungsvorschrift (Hash-Chain-Formel, Signatur-Payload/Canonicalization) steht dort
im README, falls jemand einen eigenen Verifier in einer anderen Sprache nachbauen will.

## Grenzen (bewusst offen benannt, nicht beschoenigt)

- **Kein externer Vertrauensanker.** Der Public Key steht im Bundle selbst, nicht in einer
  Allowlist/PKI. Das Bundle beweist, dass es seit der Signatur unveraendert ist und in sich
  konsistent ist -- nicht, dass eine bestimmte, bekannte Partei es erzeugt hat. Wer ein eigenes
  Ed25519-Schluesselpaar erzeugt, kann ein intern ebenso konsistentes Bundle signieren.
- **Ueberwiegend Prozess-Beweis, teilweise Diff-Beweis.** Die Trace-Events belegen Ablauf-Schritte
  (Contract gebunden, Ausfuehrung gestartet, Validierung bestanden, menschliche Freigabe,
  Abschluss). Seit dem zweiten Bundle steckt zusaetzlich ein SHA-256-Hash der `git diff --stat`-
  Kurzform drin (`devtask_diff_evidence`) -- das sichert die Stat-Zeile (Dateiname + Zeilenzahl)
  manipulationssicher ab, ist aber kein Hash des vollen Diff-Inhalts. Dass der Code im PR wirklich
  zum Auftrag passt, muss man weiterhin selbst durch Lesen des Diffs pruefen.

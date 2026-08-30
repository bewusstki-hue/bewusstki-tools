# bewusstki-tools

Freie, quelloffene Beweis- und Audit-Werkzeuge von [Bewusst.KI](https://bewusstki.de).

Jedes Tool ist eine einzelne, eigenständige HTML-Datei — läuft komplett im Browser, ohne Server,
ohne Tracking, ohne Anmeldung. Herunterladen, öffnen, benutzen. Der Quellcode jedes Tools ist die
komplette Datei selbst — nichts wird nachgeladen, nichts läuft im Hintergrund.

**Lizenz:** MIT (siehe [LICENSE](LICENSE)) — frei nutzbar, veränderbar, weiterverteilbar.

**Beweis, nicht nur Behauptung:** [PR #1](https://github.com/bewusstki-hue/bewusstki-tools/pull/1) wurde tatsächlich von ALEX über die echte Pilot-Aufgaben-Pipeline ausgeführt — signiertes [Evidence Package](evidence/) liegt bei, unabhängig von ALEX nachprüfbar.

## Werkzeuge

| Tool | Beschreibung |
|---|---|
| [Aussagen-Audit](aussagen-audit/index.html) | Belegt eine Aussage oder ein Angebot mit einem manipulationssicheren SHA-256-Hash-Siegel über Text + angehängte Belegdokumente. Späteres Gegenprüfen zeigt sofort, ob etwas verändert wurde. |
| [ARA — Architecture Reduction Audit](ARA/ara-audit-console.html) | Strukturiertes Architektur-Cleanup großer Codebasen: Manifest → Zielarchitektur → Agenten-Fragebogen → Dashboard mit Konflikt-Erkennung → Reduktionsplan. |
| [CUT — Strangler Orchestrator](CUT/cut-planner.html) | Berechnet aus einem Abhängigkeitsgraphen und einer Kern/Support/Plugin-Klassifizierung, welche Module sich am günstigsten von einem Kernsystem lösen lassen — priorisiert nach Aufwand und Risiko. |
| [Architektur-Chronist](Architektur-Chronist/architektur-chronist.html) | Baut aus Git-Log + Code-Struktur eine Zeitachse einer Codebase: erkannte Entwicklungsphasen, grober Gesundheitsverlauf, mit Beweis-Verweisen statt bloßer Behauptung. |
| [MRTB — Memory Red-Teaming Benchmark](mrtb/) | Testet, ob ein Memory-/Gedächtnissystem Cross-Tenant-Leaks, Authority-Laundering und Replay-nach-Löschung abwehrt. Zwei Referenz-Adapter (sicher/verwundbar) beweisen, dass der Benchmark den Unterschied zuverlässig erkennt. |
| [EHRLICH.BOX](ehrlich-box/index.html) | Business-Scaffolder ohne Theater: erzeugt im Browser eine echte, herunterladbare Projekt-ZIP aus wählbaren Modulen (README, LICENSE, Docker-Setup, Start-Skripte). Keine Simulation — Dateianzahl, Größe und Prüfsumme sind die echten Werte der erzeugten Datei. |
| [Terminology & Positioning Audit](terminology-audit/index.html) | Übersetzt interne Fantasy-/Codenamen in etablierte Enterprise-Begriffe, mit Begründung je Mapping und fertigen Positionierungstexten (Pitch, Website, Recruiting) zum direkten Kopieren. |

Weitere Tools folgen fortlaufend — jedes im selben Stil: klein, fokussiert, ehrlich über das, was
es beweist und was nicht.

## Warum das hier existiert

Teil von ALEX' Selbstentwicklungs-Praxis bei Bewusst.KI: statt täglich nur Ideen zu beschreiben,
entsteht wöchentlich ein tatsächlich fertiges, benutzbares Werkzeug — kostenlos, offen, ohne
versteckte Bedingungen.

---

**Zuletzt bearbeitet:** 2026-08-27
**Von:** MERIDIAN
Interne historische Beispielnamen aus dem öffentlichen Terminologie-Audit entfernt.

**Zuletzt bearbeitet:** 2026-08-27
**Von:** Bewusst.KI
EHRLICH.BOX + Terminology-Audit ergänzt (aus `ehrlich-box-and-terminology-audit.zip` restrukturiert
— das Zip bündelte beide Tools mit einem eigenen "wie auf GitHub veröffentlichen"-Wrapper-README für
den Fall getrennter Repos; hier stattdessen direkt als eigene Ordner ins bestehende Monorepo
eingeordnet, gleiche Konvention wie `aussagen-audit/`, `ARA/` etc. Root-`index.html`-Dashboard war
zusätzlich schon vor dieser Änderung veraltet (zeigte nur 1 von 5 vorhandenen Tools) — bei dieser
Gelegenheit auf den vollständigen Stand der reinen Single-File-Tools gebracht, siehe dortiger
Vermerk.

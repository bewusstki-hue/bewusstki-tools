# Architektur-Chronist

Browser-Tool, das aus Git-Log, Code-Struktur und optionalen Audit-Daten eine chronologische
Übersicht einer Codebase erzeugt: erkannte Epochen, ein heuristischer Gesundheits-Index über die
Zeit, auffällige Ereignisse. Läuft komplett lokal, keine Installation.

## Was es macht

Input: `git log --pretty=format:"%h|%ad|%an|%s"` (Pflicht), optional Datei/Zeilenzahl-Listen,
optional JSON-Audit-Daten (z.B. aus ARA), optional Log-Auszüge. Daraus baut das Tool eine
Zeitachse mit erkannten Entwicklungsphasen und einem groben Aktivitäts-/Gesundheitsverlauf.

## Grenze, ehrlich benannt — steht auch direkt im Tool

Alles basiert auf Mustern in den eingereichten Rohdaten (Commit-Metadaten, einfache
Textheuristiken). Nichts davon ist ein verifizierter Fakt über tatsächliche Ursachen oder Motive
hinter einem Commit — das Tool liefert Hypothesen mit Beleg-Verweisen, keine Wahrheit. Wer es
nutzt, sollte jede Behauptung an den mitgelieferten Beweis-Karten selbst gegenprüfen, nicht
übernehmen.

---

**Zuletzt bearbeitet:** 2026-08-17
**Von:** Claude Code (MERIDIAN)

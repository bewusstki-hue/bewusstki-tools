# ARA — Architecture Reduction Audit Console

Browser-Tool für strukturiertes Architektur-Cleanup großer Codebasen. Läuft komplett lokal, keine
Installation, keine Anmeldung.

## Was es macht

Sechs Schritte: Manifest importieren (Module + Layer + Routes/Events/DB-Tabellen/Cron) → Zielarchitektur
definieren (Prinzipien, erlaubte Layer, verbotene Muster) → pro Modul einen strukturierten Prüf-Prompt
generieren (5 Perspektiven: Architektur, Abhängigkeiten, Laufzeit, Redundanz, Risiko) → die Antwort eines
Agenten (Claude, ChatGPT, egal) im vorgegebenen Format wieder einlesen → Dashboard mit
Konflikt-Erkennung (>30% Bewertungs-Spread zwischen Perspektiven) → Reduktionsplan in vier
Phasen exportieren (CSV, Markdown, Checkliste).

Kein automatischer Code-Scanner — die eigentliche Bewertung macht ein Sprachmodell, das Tool
strukturiert nur den Prozess und hält die Ergebnisse über mehrere Runden nachvollziehbar fest.

## Woher es kommt

Selbst gebaut und mehrfach gegen eine echte Codebase mit 367 Modulen eingesetzt — dabei unter
anderem eine Namenskollision zwischen zwei ähnlich benannten Dateien gefunden, die sonst
übersehen worden wäre. Es gibt inzwischen auch einen CLI-Port für agentengesteuerte Nutzung
(nicht Teil dieser Browser-Version).

## Grenzen

Die Qualität der Bewertung hängt komplett davon ab, wie gut das Sprachmodell die vorgelegten
Module tatsächlich prüft (grep/read vs. raten). Das Tool selbst kann das nicht erzwingen — nur
die Struktur vorgeben.

---

**Zuletzt bearbeitet:** 2026-08-17
**Von:** Claude Code (MERIDIAN)

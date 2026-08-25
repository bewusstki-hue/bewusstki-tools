# EHRLICH.BOX

**Business Scaffolder ohne Theater.**

Wählt echte Module. Baut eine echte ZIP-Datei. Zeigt danach echte Zahlen — keine Story.

## Was ist das?

EHRLICH.BOX ist ein clientseitiges Tool, das im Browser ein minimales, ehrliches Projekt-Grundgerüst als ZIP erzeugt. Es gibt keinen Server, keine Simulation und keinen Fake-Fortschritt. Was du siehst, ist das, was tatsächlich passiert.

### Enthaltene Module

| Modul | Beschreibung |
|-------|--------------|
| `README.md` | Echt generierte Projekt-Dokumentation |
| `LICENSE` | Vollständiger MIT-Lizenztext |
| `docker-compose.yml` | Minimales Setup für lokalen Start |
| `.env.example` | Platzhalter-Umgebungsvariablen |
| `start.sh` / `start.ps1` | Start-Skripte für Mac/Linux + Windows |
| `prompts.txt` | Generierte Content-Prompts (kein Tool-Popup-Theater) |

## Verwendung

1. Öffne `index.html` im Browser (lokal oder über einen einfachen Static-Server).
2. Module auswählen.
3. Projektname und optional Autor eingeben.
4. Anzahl der Content-Prompts einstellen (falls Modul aktiv).
5. Auf **„ZIP wirklich erstellen“** klicken.
6. Echte Datei herunterladen. Die angezeigten Zahlen (Dateianzahl, Größe, Prüfsumme) sind real.

Keine Installation nötig. Funktioniert offline, sobald die Seite geladen ist (JSZip wird von CDN geladen – bei Bedarf lokal einbinden).

## Philosophie

Dieses Tool ist eine bewusste Gegenposition zu übertriebenen „Agenten-Swarms“ und Fake-Build-Simulationen. Es behauptet nur, was es beweisen kann.

- Kein Server
- Kein Tracking
- Keine simulierten Schritte
- Echtes ZIP mit echten Dateien

## Anpassungen

Die Module und Generator-Funktionen befinden sich im `<script>`-Block von `index.html`. Neue Module können dort einfach ergänzt werden:

1. Eintrag in das `MODULES`-Array hinzufügen.
2. Entsprechende Generierungs-Logik in der `build()`-Funktion ergänzen.

## Lizenz

MIT License – siehe [LICENSE](LICENSE).

## Beiträge

Pull Requests und Issues sind willkommen. Bitte halte die Philosophie des Tools im Auge: ehrlich, minimal, beweisbar.

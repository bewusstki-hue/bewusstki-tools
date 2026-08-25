# Terminology & Positioning Audit

Bereinigt interne Fantasy-/Buzzword-Begriffe und ersetzt sie durch etablierte Enterprise-, DevOps- und Compliance-Terminologie. Enthält fertige Textbausteine für die professionelle Außendarstellung.

## Was ist das?

Ein clientseitiges Audit-Tool, das hilft, interne Codenamen und mythologische Bezeichnungen in klar verständliche, professionelle Begriffe zu übersetzen. Es enthält:

- **Begriffs-Mapping** mit Begründung und Kategorie
- **Spickzettel** („Was ist …?“)
- **Fertige Positionierungstexte** (Elevator Pitch, Website-Hero, Recruiting etc.)
- **Vollständigen Klartext-Export** für Dokumentation, Pitch-Deck oder Website

Die mitgelieferten Daten stammen aus einem realen Beispiel (Verification-/Assurance-Plattform für KI-Agenten-Arbeit). Sie können und sollen durch eigene Begriffe ersetzt werden.

## Verwendung

1. Öffne `index.html` im Browser.
2. Im Tab **Begriffs-Mapping** kannst du suchen, filtern und den Status (Offen / Entschieden) setzen.
3. Im Tab **Spickzettel** findest du schnelle Erklärungen.
4. Im Tab **Außendarstellung** stehen fertige Textbausteine bereit (kopierbar).
5. Im Tab **Export** erhältst du den kompletten Klartext zum Kopieren.

**Hinweis:** Der Status (Offen/Entschieden) wird nur in der aktuellen Browsersitzung gehalten. Vor dem Schließen der Seite den Export sichern.

## Eigene Daten einpflegen

Die gesamten Mapping- und Text-Daten befinden sich im `<script>`-Block von `index.html` in den Arrays `DATA` und `TEXTS`.

Beispiel für einen neuen Eintrag in `DATA`:

```js
{
  id: 'mein-begriff',
  category: 'Kernkomponenten',
  old: 'CoolerCodename',
  new: 'Service Registry',
  description: 'Kurze, klare Beschreibung, was die Komponente tut.',
  rationale: 'Begründung, warum der neue Name besser ist (Anschlussfähigkeit an etablierte Begriffe).'
}
```

Danach die Seite neu laden. Keine weiteren Änderungen nötig.

## Philosophie

Das Tool folgt dem Prinzip: **Interne Sprache darf verspielt sein — externe Sprache muss belastbar sein.**

Fantasy-Namen und Abkürzungen erzeugen Erklärungsaufwand und Skepsis bei technischen Prüfern, Investoren und Enterprise-Käufern. Dieses Tool macht den Umstieg konkret und nachvollziehbar.

## Technische Hinweise

- Rein clientseitig (kein Backend, kein Storage außer der aktuellen Session)
- Keine externen Abhängigkeiten außer System-Fonts
- Funktioniert offline

## Lizenz

MIT License – siehe [LICENSE](LICENSE).

## Beiträge

Pull Requests und Issues sind willkommen. Besonders nützlich:

- Weitere Beispiel-Mappings aus anderen Domänen
- Verbesserte Export-Formate (Markdown, CSV)
- Persistenz-Optionen (optional, localStorage)

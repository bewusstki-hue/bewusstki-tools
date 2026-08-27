# Testplan — manuell, vor jeder Veröffentlichung

Gilt für jedes Tool in diesem Repo. Kein Server, keine Installation nötig — Datei direkt im
Browser öffnen (Doppelklick oder Rechtsklick → Öffnen mit → Browser).

## Aussagen-Audit (`aussagen-audit.html`)

Testdaten liegen fertig in `test-fixtures/` — nichts selbst ausdenken nötig, direkt reinziehen.

**1. Erstellen-Basisfall**
- Datei öffnen, Tab "Audit erstellen" ist aktiv.
- **Name / Absender:** `Max Mustermann (Test)`
- **Aussage** (copy & paste):
  ```
  Ich, Max Mustermann, biete freiberufliche Webentwicklung an: React/Node.js,
  5 Jahre Erfahrung, Stundensatz 85€. Referenzen und Nachweise als Anhang.
  Kontakt: max.mustermann@test-beispiel.de
  ```
- Dateien reinziehen: `test-fixtures/Referenz-Zeugnis.txt`, `Zertifikat-React-2025.txt`,
  `Rechnung-Muster.txt` (die drei "echten" Testdokumente — `-VERAENDERT` und `Unbeteiligte-Datei`
  bewusst NICHT hier verwenden, die kommen erst bei Schritt 3 und 5).
- Erwartet: Datei-Hashes erscheinen sofort einzeln in der Liste.
- "Audit erstellen" klicken → Siegel + Fingerabdruck erscheinen.
- JSON **und** HTML-Report herunterladen, beide öffnen, Inhalt auf Vollständigkeit prüfen.

**2. Erfolgsfall beim Gegenprüfen**
- Zu Tab "Audit prüfen" wechseln.
- Die heruntergeladene `.audit.json` hochladen.
- Dieselben drei Original-Testdokumente aus `test-fixtures/` erneut hochladen.
- "Gegenprüfen" klicken.
- Erwartet: alle Zeilen grün "OK", Gesamtergebnis ✅.

**3. Manipulation an einer Datei erkennen**
- Beim Gegenprüfen statt `Referenz-Zeugnis.txt` die Datei `Referenz-Zeugnis-VERAENDERT.txt`
  hochladen (zusammen mit den anderen beiden Originalen). Der Unterschied ist absichtlich winzig
  (ein Jahreszahl-Zeichen geändert) — von Auge kaum zu sehen, genau dafür ist das Tool da.
- Erwartet: `Referenz-Zeugnis.txt` wird rot als "FEHLT/GEÄNDERT" markiert (die hochgeladene Datei
  mit dem geänderten Namen wird nicht als Match erkannt, weil der Hash nicht passt), Gesamtergebnis ⚠️.

**4. Manipulation an der Audit-Datei selbst erkennen**
- Die heruntergeladene `.audit.json` in einem Texteditor öffnen, ein Zeichen im `"claim"`-Feld
  ändern (z.B. den Stundensatz), speichern.
- Diese veränderte JSON beim Gegenprüfen hochladen.
- Erwartet: "Audit-Datei selbst wurde verändert" wird rot markiert.

**5. Zusätzliche, nicht zugehörige Datei erkennen**
- Beim Gegenprüfen die drei Original-Testdokumente PLUS `test-fixtures/Unbeteiligte-Datei.txt`
  hochladen.
- Erwartet: eigene Zeile "ZUSÄTZLICH — hochgeladen, aber nicht Teil dieses Audits" für die
  unbeteiligte Datei, Gesamtergebnis kippt auf ⚠️.

**6. Edge Cases**
- Audit ganz ohne Dateien erstellen (nur Text) — muss trotzdem funktionieren.
- Bewusst `<script>alert(1)</script>` als Teil der Aussage eintragen → darf im Report/JSON nur als
  Text erscheinen, niemals ausgeführt werden.
- Lange Aussage mit Zeilenumbrüchen, Umlauten, Emoji → Report und JSON müssen das sauber
  darstellen.
- Mit Tab-Taste durch die Seite navigieren, Dropzones per Enter/Leertaste auslösen (Tastatur-
  Zugänglichkeit).

**7. Bekannter, akzeptierter Grenzfall (nicht testbar, nur zur Kenntnis)**
- Der Zeitstempel stammt standardmäßig vom eigenen Gerät, ohne externen Vertrauensanker. Seit
  14.08.2026 gibt es dafür einen optionalen externen Zeitstempel (Schritt 10) — Standardmodus
  bleibt aber weiterhin rein lokal, der Disclaimer weist explizit darauf hin.

**8. Offline-Check**
- Internetverbindung trennen, Datei trotzdem öffnen und benutzen — muss vollständig funktionieren
  (keine externen Schriftarten oder Ressourcen mehr geladen). Seit 15.08.2026 zusätzlich: QR-Code
  muss offline trotzdem erscheinen (vendorte Bibliothek, kein CDN) — einziger Punkt, der offline
  bewusst NICHT geht, ist der optionale externe Zeitstempel (Schritt 10, klar als "verlässt den
  lokalen Modus" gekennzeichnet).

**9. Eingebetteter Inhalt (neu, Stand 14.08.2026)**
- Beim Erstellen die Checkbox "Dokumentinhalt mit einbetten" anhaken, wieder
  `Referenz-Zeugnis.txt` + `Zertifikat-React-2025.txt` + `Rechnung-Muster.txt` verwenden.
- Erwartet: Meldung "Inhalt eingebettet" unter dem Siegel.
- JSON herunterladen, im Texteditor öffnen → jede Datei hat jetzt zusätzlich ein `content`-Feld
  (lange Base64-Zeichenkette).
- Zu Tab "Audit prüfen" wechseln, NUR die `.audit.json` hochladen (keine Originaldateien erneut
  hochladen) → "Gegenprüfen"-Button sollte trotzdem aktiv/klickbar sein.
- Erwartet: alle Zeilen grün "OK — geprüft über eingebetteten Inhalt", pro Zeile ein Button
  "Original extrahieren" → Klick lädt die Originaldatei unverändert herunter.
- Gegenprobe: dieselbe JSON-Manipulation wie in Schritt 4 (ein Zeichen im `"claim"`-Feld ändern)
  → muss weiterhin als "Audit-Datei wurde verändert" erkannt werden, auch mit eingebettetem Inhalt.

**10. Externer Zeitstempel + Siegel-Export (neu, Stand 14.08.2026)**
- Nach "Audit erstellen": Button "Siegel (SVG) herunterladen" klicken → Datei öffnet sich als Bild,
  zeigt Fingerabdruck + Name + Datum, keine externe Anfrage dabei (Offline-Check gilt weiter).
- Button "Externen Zeitstempel anfordern" klicken → Bestätigungsdialog muss zuerst erscheinen
  ("verlässt den rein-lokalen Modus..."), erst nach Bestätigen geht die Anfrage raus.
- Erwartet bei bestehender Internetverbindung: nach kurzer Zeit "ANGEFORDERT"-Zeile, Button
  ".ots" herunterladen funktioniert, Datei ist nicht leer.
- JSON danach erneut herunterladen → enthält jetzt zusätzlich ein `externalTimestamp`-Feld.
- Diese neue JSON in Tab "Audit prüfen" gegenprüfen → Gesamtergebnis muss weiterhin ✅ sein (der
  Zeitstempel darf die normale Manipulationsprüfung nicht verfälschen), zusätzliche Zeile
  "ZEITSTEMPEL" mit ".ots extrahieren"-Button muss erscheinen.
- Bekannter, akzeptierter Grenzfall: die Bitcoin-Bestätigung selbst dauert Stunden — das Tool
  prüft nur, dass der Kalender-Server die Anfrage angenommen hat, nicht die volle Blockchain-
  Bestätigung. Für die volle Prüfung/das spätere Upgrade ist das offizielle OpenTimestamps-Tool
  vorgesehen (Link im Disclaimer), bewusst nicht selbst nachgebaut.

**11. QR-Code, Mitunterzeichner, PDF-Export (neu, Stand 15.08.2026)**
- Nach "Audit erstellen": kleine QR-Vorschau erscheint direkt neben dem Siegel. Button "QR-Code
  (SVG) herunterladen" → eigene Datei, mit einem beliebigen QR-Scanner (z.B. Handykamera) scannen
  → muss den vollständigen Audit-Hash als Text liefern, identisch zum "Vollständiger Audit-Hash"
  im Report.
- Vor "Audit erstellen": im neuen Feld "Weitere Mitunterzeichner" zwei Einträge hinzufügen (Name +
  optionale Notiz), dann erst "Audit erstellen" klicken. Erwartet: Namen erscheinen unter dem
  Siegel ("Mitunterzeichner: ..."), JSON enthält ein `coSigners`-Array mit beiden Einträgen.
- "Zurücksetzen" klicken → Mitunterzeichner-Liste muss sich leeren (nicht nur Name/Aussage-Felder).
- Report (HTML) herunterladen, öffnen → eigene Tabelle "Mitunterzeichner" muss erscheinen, dazu
  der eingebettete QR-Code oben neben dem Fingerabdruck. Button "🖨 Als PDF speichern" oben im
  Report klicken → Browser-Druckdialog öffnet sich, "Als PDF speichern" muss ein lesbares PDF
  ergeben (Button selbst darf im Druck-/PDF-Ergebnis NICHT erscheinen, `@media print` versteckt ihn).
- Gegenprobe Manipulationsprüfung: JSON mit Mitunterzeichnern gegenprüfen (Tab "Audit prüfen") →
  weiterhin ✅ Gesamtergebnis. Danach einen Mitunterzeichner-Namen direkt im JSON-Text ändern und
  erneut hochladen → muss als "Audit-Datei wurde verändert" erkannt werden (Mitunterzeichner sind
  Teil des Hashes, genau wie Aussage/Name).

---

**Zuletzt bearbeitet:** 2026-08-15
**Von:** Bewusst.KI

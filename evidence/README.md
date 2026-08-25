# Evidence

Signiertes `devtask.execution@1.0`-Beweispaket fuer eine echte, von ALEX (Bewusst.KI) ausgefuehrte
Aufgabe auf diesem Repo -- nicht simuliert, nicht nachtraeglich geschrieben.

**Aufgabe:** [PR #1](https://github.com/bewusstki-hue/bewusstki-tools/pull/1) -- `index.html`
listete nur 1 von 7 Tools, Footer-Link zeigte auf falschen Repo-Namen.

**Ablauf:** Work Contract (Auftragstext + Risikoklasse eingefroren als Hash) -> isolierte Ausfuehrung
-> Validierung -> menschliche Freigabe -> signiertes Evidence Package.

| Feld | Wert |
|---|---|
| Contract-Hash | `aa0d959ae3db1a39314010d0528b9752432e53889173ef38859ef4d267da199d` |
| Risikoklasse | R1 |
| Validierung | passed (ara-validation) |
| Modell | deepseek-v4-flash |
| Kosten | $0.01233 |
| Turns | 8 |
| Laufzeit | 72 Sekunden |
| Signatur | Ed25519, Public Key im Bundle enthalten |

Das Paket ([dt-1787662064400-sjiw.json](dt-1787662064400-sjiw.json)) enthaelt eine Hash-Chain ueber
alle Ausfuehrungsschritte plus eine Ed25519-Signatur. Die Signatur laesst sich mit jeder
Standard-Ed25519-Bibliothek gegen den im Bundle enthaltenen Public Key pruefen (z.B. Node `crypto`
oder Python `cryptography`) -- dafuer braucht es kein ALEX-System.

## Grenzen (bewusst offen benannt, nicht beschoenigt)

- **Kein externer Vertrauensanker.** Der Public Key steht im Bundle selbst, nicht in einer
  Allowlist/PKI. Das Bundle beweist, dass es seit der Signatur unveraendert ist und in sich
  konsistent ist -- nicht, dass eine bestimmte, bekannte Partei es erzeugt hat. Wer ein eigenes
  Ed25519-Schluesselpaar erzeugt, kann ein intern ebenso konsistentes Bundle signieren.
- **Prozess-Beweis, kein Code-Diff-Beweis.** Die Trace-Events belegen Ablauf-Schritte (Contract
  gebunden, Ausfuehrung gestartet, Validierung bestanden, menschliche Freigabe, Abschluss) --
  keinen Hash des tatsaechlichen Datei-Diffs. Dass der Code in [PR #1](https://github.com/bewusstki-hue/bewusstki-tools/pull/1)
  wirklich zum Auftrag passt, muss man aktuell selbst durch Lesen des Diffs pruefen, nicht allein
  aus dem Bundle ableiten.
- **Noch kein oeffentlicher CLI-Verifier fuer genau diese Capability.** Die Capability hier ist
  `devtask.execution@1.0`. Der unabhaengige [alex-mrtb-verify-bundle](https://github.com/bewusstki-hue/alex-mrtb-verify-bundle)-Verifier
  deckt bisher nur sechs `memory.*`-Capabilities ab, nicht diese.
- **Ein einzelnes Beispiel.** Zeigt, dass die Kette einmal echt durchgelaufen ist -- noch keine
  Serie inkl. eines absichtlich fehlgeschlagenen Bundles (`FAILED`), die zeigt, dass nicht jeder
  Versuch automatisch gruen wird.

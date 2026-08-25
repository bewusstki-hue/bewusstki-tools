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
alle Ausfuehrungsschritte plus eine Signatur -- unabhaengig von ALEX selbst gegenprüfbar, nicht nur
eine Behauptung.

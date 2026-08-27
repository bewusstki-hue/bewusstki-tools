# CUT — Strangler Orchestrator

Browser-Tool, das aus einem Abhängigkeitsgraphen (Module + Kanten) und einer Kern/Support/Plugin-
Klassifizierung einen priorisierten Plan berechnet, welche Plugin-Module sich am günstigsten
von einem Kernsystem lösen lassen. Läuft komplett lokal, keine Installation.

## Was es macht

Input: eine Liste von Modulen (mit Cluster CORE/SUPPORT/PLUGIN und den Fähigkeiten, die sie
bedienen) und eine Liste von Kanten zwischen ihnen (Typ: Import, Laufzeit-Aufruf, Event, geteilte
Tabelle, Singleton — jeder Typ unterschiedlich schwer zu trennen). Das Tool berechnet daraus pro
Plugin-Modul: wie teuer wäre es rauszulösen (gewichtet nach Kantentyp), wie riskant, und ob es eine
Kern-Fähigkeit schwächen würde. Ergebnis ist eine sortierte Liste, mit welchem Cut man anfängt.

Erkennt automatisch den am stärksten verbundenen Kern-"Hub" (das Modul mit den meisten Kanten zu
Plugins) und markiert Cuts, die diesen Hub betreffen, separat.

## Grenze, ehrlich benannt

Die Einstufung "wichtig/unwichtig" basiert nur auf der Graph-Struktur (wie viele Kanten, welcher
Typ), nicht auf dem Inhalt. Wenn ein Kern-Modul sehr viele Nebenabhängigkeiten direkt hat, stuft
das Tool praktisch alles als "wichtig" ein — das ist dann kein echtes Signal mehr, nur ein
Hinweis, dass der Graph an dieser Stelle strukturell eng ist. Ob zwei Module inhaltlich dasselbe
tun (echte Dopplung), muss weiterhin jemand lesen, das sieht der Graph nicht.

---

**Zuletzt bearbeitet:** 2026-08-27
**Von:** Bewusst.KI

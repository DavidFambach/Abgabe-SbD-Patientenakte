# Architekturentscheidung: microservices

## Zusammenfassung
Bereich: Architektur
Thema: microservices
ID: AD5
Architekturentscheidung: Aufbau der Architektur als microservices

|                           |                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------|
| Problemstellung           | Es ist zu entscheiden, ob die Architektur mit microservices aufgebaut werden sollte. |
| Annahmen                  |                                                                                      |
| Motivation                | Ein sinnvoller Architekturansatz erleichtert aktuelle und zukünftige Arbeiten.       |
| Alternativen              | Option 1: Umsetzung mit microservices <br> Option 2: Umsetzung ohne microservices    |
| Entscheidung              | Option 1: Umsetzung mit microservices                                                |
| Begründung                | Siehe Entscheidungsmatrix (Unten)                                                    |
| Implikationen             | Keine                                                                                |
| Abgeleitete Anforderungen | Keine                                                                                |
| Zugehörige Entscheidungen | Keine                                                                                |

## Entscheidungsmatrix

| Kriterien          | Gewichtung | mit microservices                                           | Evaluierung | ohne mircoservices | Evaluierung | 
|--------------------|------------|-------------------------------------------------------------|-------------|--------------------|-------------|
| Skalierbarkeit     | 1          |                                                             | ++          |                    | -           |
| Wartbarkeit        | 2          |                                                             | ++          |                    | --          |
| Performance        | 2          | Abhängig von Netzwerk-Latenzen und load balancing Lösungen. | +           |                    | +           |
| Konsistenz         | 4          |                                                             | 0           |                    | +           |
| Programmieraufwand | 2          |                                                             | -           |                    | +           |
| **Gesamt**         |            |                                                             | 6 Pkt.      |                    | 1 Pkt.      | 

Legende zur Evaluierung:
 - ++: Die Alternative ist bezüglich dem Kriterium sehr positiv zu bewerten. Diese Bewertung entspricht 3 Punkten.
 - +: Die Alternative ist bezüglich dem Kriterium positiv zu bewerten. Diese Bewertung entspricht 1 Punkt.
 - O: Die Alternative ist bezüglich dem Kriterium neutral zu bewerten, eine Bewertung der Alternative hinsichtlich dieses Kriteriums ist nicht sinnvoll oder nicht praktikabel oder wurde aus einem anderen Grund nicht vorgenommen. Diese Bewertung entspricht 0 Punkten.
 - \-: Die Alternative ist bezüglich dem Kriterium negativ zu bewerten. Diese Bewertung entspricht -1 Punkt.
 - \-\-: Die Alternative ist bezüglich dem Kriterium sehr negativ zu bewerten. Diese Bewertung entspricht -3 Punkten.
Die Gesamtbewertung ist die Summe der gewichteten Evaluierungen über alle Kriterien, die keine Ausschlusskriterien sind. Alternativen, die bezüglich mindestens einem Ausschlusskriterium negativ bewertet wurden, erhalten keine Gesamtbewertung und werden nicht weiter betrachet.

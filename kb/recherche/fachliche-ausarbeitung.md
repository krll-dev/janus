# Fachliche Domänen-Ausarbeitung: Private Hausrat-Bestandsführung

## TL;DR
- Die private Hausratversicherung versichert bewegliches Eigentum am Versicherungsort zum **Neuwert (Wiederbeschaffungswert)** gegen die Standardgefahren Feuer/Brand, Einbruchdiebstahl/Raub/Vandalismus, Leitungswasser sowie Sturm/Hagel; Elementargefahren, Glasbruch und Fahrraddiebstahl sind zubuchbare Bausteine. Referenzrahmen sind die GDV-Musterbedingungen VHB (2010/2016/2022).
- Für die Bestandsführung sind zwei Mechanismen fachlich zentral: **Wertsachen-Sublimits** (Wertsachen gesamt meist 20–30 % der Versicherungssumme; Bargeld ~1.500 €, Urkunden/Sparbücher ~7.500 €, Schmuck ~20.000 € außerhalb eines Wertschutzschranks) und die **Unterversicherungsprüfung** (Bestandswert vs. Versicherungssumme; Faustregel 650 €/m², Unterversicherungsverzicht bei ausreichender Summe).
- Diese Ausarbeitung liefert Fach-Substanz: Domain-Events entlang des gesamten Lebenszyklus (Tabelle), einzeln zitierbare Geschäftsregeln, ein alphabetisches Glossar und konkrete Dashboard-Kennzahlen mit fachlicher Begründung — bewusst ohne Epic/Story-Vorschläge.

## Key Findings
1. **Deckungsmodell**: Standardmäßig vier Gefahrengruppen (Brand/Blitz/Überspannung/Explosion; Einbruchdiebstahl/Raub/Vandalismus; Leitungswasser; Sturm/Hagel), Elementar nur optional. Entschädigung zum Neuwert.
2. **Wertsachen** sind ein eigenes Regelwerk mit prozentualen und absoluten Sublimits, die vom Aufbewahrungsort (Wertschutzschrank ja/nein) abhängen — ideal für abgestufte Geschäftsregeln.
3. **Unterversicherung** ist der fachlich reichhaltigste Regelmechanismus: anteilige Kürzung nach Verhältnis Versicherungssumme/Versicherungswert, abgemildert durch Unterversicherungsverzicht und 10 % Vorsorge.
4. **Schadenstatistik (GDV 2024)** liefert realistische Verteilungen und Beträge für Testdaten und Dashboards (Gesamtleistung 1.819 Mio. €, Combined Ratio der Sparte 82,8 %).
5. **Fristen** sind meist als „unverzüglich" (ohne schuldhaftes Verzögern) formuliert — als konkrete Frist im System modellierbar.

## Details

### 1. Fachliche Domänen-Grundlagen

**Vertragsgegenstand und Versicherungsort.** Die verbundene Hausratversicherung schützt vor den finanziellen Folgen von Sachschäden am Hausrat, also am gesamten beweglichen Eigentum eines privaten Haushalts. Als Faustregel gilt: Alles, was beim gedachten „Umdrehen der Wohnung" herausfiele, ist Hausrat — Möbel, Elektronik/Haushaltsgeräte, Kleidung, Geschirr, Sportgeräte, Wertsachen und (je nach Baustein) Fahrräder. Fest mit dem Gebäude verbundene Teile (Türen, Fenster, Einbauten) sind Sache der Wohngebäudeversicherung.

Der **Versicherungsort** ist die im Versicherungsschein bezeichnete Wohnung. Dazu zählen Balkone, Terrassen, Loggien, allein genutzte Keller-/Speicherräume, Nebengebäude auf dem Grundstück und nahegelegene Garagen sowie gemeinschaftlich genutzte, abschließbare Räume (z. B. Fahrradkeller, Waschküche). Die **Außenversicherung** erweitert den Schutz weltweit für Hausrat, der sich vorübergehend (in der Regel bis zu 3 Monate) außerhalb des Versicherungsortes befindet, meist begrenzt auf 10 % der Versicherungssumme.

**Entschädigungsprinzip.** Die Hausratversicherung ist eine **Neuwertversicherung**: Ersetzt wird der Wiederbeschaffungswert von Sachen gleicher Art und Güte in neuwertigem Zustand. Für nicht mehr zweckgemäß verwendbare Sachen gilt der erzielbare Verkaufswert; für Kunst/Antiquitäten der Betrag für Wiederbeschaffung gleicher Art und Güte. Der Zeitwert (Neuwert abzüglich Abschreibung für Alter/Abnutzung) spielt nur bei stark abgenutzten Sachen oder abweichenden Bedingungen eine Rolle — im Gegensatz zur Haftpflichtversicherung, die grundsätzlich den Zeitwert ersetzt.

**GDV-Musterbedingungen (Referenzrahmen).** Die Allgemeinen Hausrat Versicherungsbedingungen (VHB) werden vom Gesamtverband der Deutschen Versicherungswirtschaft (GDV) als unverbindliche Musterbedingungen herausgegeben; aktuelle Versionsstände sind VHB 2010, 2016 und 2022 (Muster teils mit Stand Juni 2026). Sie sind für Versicherer rechtlich unverbindlich und zur fakultativen Verwendung; abweichende (meist verbraucherfreundlichere) Vereinbarungen sind üblich. Es gibt zwei Modellvarianten: das **Quadratmetermodell** (Versicherungssumme = Wohnfläche × Pauschale) und das **Versicherungssummenmodell** (individuell ermittelte Summe). Für ein Fachmodell reicht es, die VHB als marktüblichen Rahmen zu kennen; ein eigener juristischer Abschnitt ist nicht nötig.

**Deckungsbausteine.** Standard (Grunddeckung) nach VHB:
- **Brand, Blitzschlag, Überspannung durch Blitz, Explosion/Verpuffung, Implosion, Anprall/Absturz Luftfahrzeug, Fahrzeuganprall, Seng-, Rauch-/Rußschäden**
- **Einbruchdiebstahl, Diebstahl (definierte Fälle), Vandalismus nach Einbruch, Raub**
- **Leitungswasser**
- **Sturm (ab Windstärke 8) und Hagel**

Zubuchbare Bausteine/Klauseln (fachlich relevant für Bestand & Schaden):
- **Elementarschäden/weitere Naturgefahren**: Überschwemmung, Rückstau, Erdbeben, Erdsenkung, Erdrutsch, Schneedruck, Lawinen, Vulkanausbruch. Häufig mit Selbstbehalt (oft 10 % des Schadens, mindestens 500 €).
- **Fahrraddiebstahl**: erweitert den Schutz auf Diebstahl außerhalb verschlossener Räume; Entschädigung typisch als Prozentsatz der Versicherungssumme (marktüblich 1 %, erhöhbar auf 5–10 %) oder feste Summe; teils Nachtzeitklausel (22–6 Uhr) in Altverträgen.
- **Glasbruch (Glasversicherung)**: Gebäude- und Mobiliarverglasung.
- **Überspannungsschäden** über den Blitz hinaus: oft als Prozentsatz der Versicherungssumme begrenzt (z. B. 5 %).
- **Fahrrad-/Elektronikschutz, Schutzbrief/Assistance, unbenannte Gefahren (Allgefahrendeckung)** in Premium-Tarifen.

**Generelle Ausschlüsse** (VHB): Krieg, innere Unruhen, Kernenergie; ferner Vorsatz und (quotal) grobe Fahrlässigkeit.

### 2. Bestandsführung: Wertsachen und Gegenstände

**Kategorisierung von Hausrat-Gegenständen.** Für ein Bestandsmodell bewährt sich die Unterteilung in „normalen Hausrat" und „Wertsachen". Nachstehende Kategorien mit marktüblichen Preis-/Wertrahmen dienen als Grundlage für realistische Testdaten (Neuwerte pro Einzelstück, Richtwerte):

| Kategorie | Beispiele | Neuwert-Rahmen je Stück (Richtwert) |
|---|---|---|
| Möbel | Sofa, Schrank, Bett, Tisch | 200 – 3.000 € |
| Unterhaltungselektronik | Fernseher, Hi-Fi, Konsole | 300 – 2.500 € |
| IT/Kommunikation | Laptop, Smartphone, Tablet | 300 – 2.000 € |
| Haushaltsgroßgeräte | Waschmaschine, Kühlschrank, Herd | 400 – 1.500 € |
| Kleidung/Textilien | Garderobe, Schuhe, Vorhänge | 20 – 500 € |
| Sportgeräte | Fahrrad, E-Bike, Ski, Fitness | 300 – 5.000 € |
| Küche/Geschirr | Geschirr, Kleingeräte, Besteck | 10 – 400 € |
| Wertsachen: Schmuck/Uhren | Gold, Platin, Edelsteine, Sammleruhren | 200 – 20.000 €+ |
| Wertsachen: Bargeld/Geldkarten | Bargeld, Prepaid-Guthaben | — |
| Wertsachen: Urkunden/Wertpapiere | Sparbücher, Wertpapiere | — |
| Wertsachen: Kunst/Antiquitäten | Gemälde, Antiquitäten (>100 Jahre), Teppiche, Pelze | 500 – hoch offen |

Der durchschnittliche Hausratwert eines Vier-Personen-Haushalts wird auf einen Betrag im mittleren fünfstelligen Bereich geschätzt; die Quadratmeter-Pauschale von 650 €/m² spiegelt diesen Durchschnitt wider (z. B. 80 m² → 52.000 €).

**Besondere Behandlung von Wertsachen.** Als Wertsachen gelten nach VHB: Bargeld und auf Geldkarten geladene Beträge; Urkunden einschließlich Sparbücher und Wertpapiere; Schmuck, Edelsteine, Perlen, Briefmarken, Münzen, Medaillen sowie Sachen aus Gold und Platin; Pelze, handgeknüpfte Teppiche, Gobelins, Kunstgegenstände; Antiquitäten (älter als 100 Jahre, außer Möbel). Für sie gelten zwei gestaffelte Grenztypen:

- **Allgemeine Wertsachengrenze** (prozentual): Wertsachen insgesamt meist **20 %** der Versicherungssumme (marktüblich; erhöhbar auf 30/40/50 %). In den VHB-2010-Muster-Beispielen sind auch 30 % vereinbart.
- **Absolute Sublimits außerhalb eines anerkannten, verschlossenen Wertschutzschranks** (Richtwerte, je Versicherungsfall):
  - Bargeld/Geldkarten: **1.500 €** (marktüblich 1.000–3.500 €)
  - Urkunden, Sparbücher, Wertpapiere: **7.500 €** (marktüblich 2.500–5.000 €)
  - Schmuck, Edelsteine, Perlen, Briefmarken, Münzen, Gold/Platin: **20.000 €**

Ein **Wertschutzschrank** im Sinne der VHB ist ein anerkanntes Sicherheitsbehältnis (durch anerkannte Prüfstelle zertifiziert) mit Mindestgewicht 200 kg oder fachmännisch verankert/eingemauert. Bei ordnungsgemäßer Aufbewahrung darin entfallen die niedrigen Sublimits; es gilt dann die höhere prozentuale Wertsachengrenze. Einzelstücke über ~5.000 € verlangen viele Versicherer im Tresor. Diese Staffelung ist ideal für abgestufte Geschäftsregeln (Aufbewahrungsort als Attribut je Wertsache).

**Unterversicherung / Vorsorgegrenze.** Eine Unterversicherung liegt vor, wenn der tatsächliche Wert des gesamten Hausrats (Versicherungswert) die vereinbarte Versicherungssumme (einschließlich Vorsorgebetrag) übersteigt. Im Schadenfall darf der Versicherer dann anteilig kürzen — auch bei Teilschäden:

> Entschädigung = Schadenbetrag × (Versicherungssumme ÷ Versicherungswert)

Beispiel: Hausratwert 100.000 €, Versicherungssumme 50.000 € → 50 % Unterversicherung → bei 10.000 € Schaden nur 5.000 € Erstattung.

Abmildernde Mechanismen:
- **Unterversicherungsverzicht**: Bei Ansatz von mind. 650 €/m² (marktüblich 600–750 €/m²) verzichtet der Versicherer auf die Unterversicherungsprüfung; er zahlt bis zur vereinbarten Summe abzugsfrei. Bei einem Totalschaden schützt der Verzicht dennoch nicht über die Summe hinaus.
- **Vorsorgeversicherungssumme**: in der Regel **10 %** Aufschlag auf die Versicherungssumme, um unterjährige Neuanschaffungen/Preissteigerungen abzudecken. Die Vorsorge gilt auch für prozentuale Grenzen (Wertsachen, Fahrrad, Überspannung).
- **Summenanpassung**: jährliche Indexanpassung der Versicherungssumme nach Preisindex.

Aus diesem Mechanismus lässt sich unmittelbar eine Geschäftsregel „Unterversicherungs-Warnung" ableiten: laufender Vergleich Bestandswert vs. Versicherungssumme + Vorsorge.

### 3. Domain-Events

Die folgenden Events decken den gesamten Lebenszyklus ab. Namen in Vergangenheitsform, fachlich (nicht technisch) beschrieben. „Konsequenz" beschreibt eine mögliche nachgelagerte fachliche Reaktion.

| Event-Name | Trigger | Fachliche Beschreibung | Mögliche fachliche Konsequenz |
|---|---|---|---|
| `ApplicationSubmitted` | Interessent stellt Antrag | Antrag auf Hausratpolice mit Wohnfläche, Adresse, Bausteinen eingereicht | Risiko-/Plausibilitätsprüfung wird angestoßen |
| `ApplicationAssessed` | Antragsprüfung abgeschlossen | Antrag fachlich bewertet (Vorschäden, Versicherungssumme, Tarifierung) | Annahme, Ablehnung oder Nachfrage |
| `PolicyIssued` | Antrag angenommen | Vertrag policiert; Versicherungssumme, Vorsorge, Bausteine, Selbstbehalt festgelegt | Versicherungsschutz aktiv; Beitragsstellung |
| `CoverageStarted` | Versicherungsbeginn erreicht | Materieller Versicherungsschutz beginnt (nach Zahlung Erstbeitrag) | Ab hier sind Schäden dem Grunde nach gedeckt |
| `PolicyAmended` | Vertragsänderung | Änderung von Summe, Baustein, Selbstbehalt, Bankverbindung | Neuberechnung Beitrag; ggf. Unterversicherungsstatus neu |
| `CoverageAddOnAdded` | Baustein zugebucht | Ergänzung z. B. Elementar, Fahrraddiebstahl, Glas | Neue Deckung/Grenzen aktiv; Beitragsanpassung |
| `SumInsuredAdjusted` | Summenanpassung/Index | Versicherungssumme an Preisindex/Neuanschaffungen angepasst | Unterversicherungsrisiko neu bewertet |
| `AddressChanged` | Wohnungswechsel | Umzug gemeldet; Versicherungsort wechselt (Übergangsfrist) | Prüfung Tarifzone/Beitrag; ggf. Sonderkündigungsrecht |
| `PolicyRenewed` | Ablauf Versicherungsjahr ohne Kündigung | Vertrag verlängert sich stillschweigend um ein Jahr | Neue Beitragsperiode; Indexanpassung |
| `PolicyCancelled` | Kündigung (ordentlich/außerordentlich) | Vertrag durch VN oder Versicherer gekündigt (Ablauf, Schadenfall, Umzug) | Ende Versicherungsschutz zum Stichtag |
| `PremiumPaid` / `PremiumOverdue` | Beitragszahlung / Zahlungsverzug | Beitrag eingegangen bzw. ausgeblieben | Bei Verzug: Mahnung, ggf. Leistungsfreiheit |
| `ItemAddedToInventory` | Gegenstand erfasst | Neuer Hausrat-Gegenstand mit Kategorie, Neuwert, Beleg erfasst | Bestandswert steigt; Unterversicherungsprüfung |
| `ItemValued` / `ItemRevalued` | Bewertung/Neubewertung | Neuwert eines Gegenstands ermittelt oder aktualisiert (Gutachten, Index) | Bestandswert und Wertsachenanteil neu berechnet |
| `ItemRemovedFromInventory` | Gegenstand entfernt | Verkauf, Entsorgung, Verschenken erfasst | Bestandswert sinkt |
| `ItemCategorizedAsValuable` | Einordnung als Wertsache | Gegenstand als Wertsache klassifiziert (Schmuck, Bargeld etc.) | Wertsachen-Sublimit-Prüfung |
| `ValuableStorageChanged` | Aufbewahrungsort geändert | Wertsache in/aus Wertschutzschrank verlagert | Anwendbares Sublimit ändert sich |
| `InventoryValueRecalculated` | Bestandsänderung/periodisch | Gesamter Bestandswert neu summiert | Vergleich mit Versicherungssumme |
| `UnderinsuranceDetected` | Bestandswert > Versicherungssumme+Vorsorge | Unterversicherung fachlich erkannt | Warnung an VN; Empfehlung Summenerhöhung |
| `ValueLimitExceeded` | Kategoriewert > Sublimit | Wertgrenze einer Kategorie (z. B. Bargeld) überschritten | Hinweis auf ungedeckten Teil; Tresor-/Zusatzempfehlung |
| `ClaimFiled` | Schadenmeldung eingegangen | VN meldet Schaden mit Ursache, Datum, betroffenen Gegenständen | Plausibilitäts- und Deckungsprüfung startet |
| `PoliceReportRegistered` | Anzeige bei Diebstahl/Vandalismus | Polizeiliche Anzeige/Stehlgutliste erfasst | Voraussetzung für Regulierung bei Einbruch/Raub |
| `ClaimAcknowledged` | Eingangsbestätigung | Schaden formal aufgenommen, Schadennummer vergeben | Bearbeiter/Prüfung zugewiesen |
| `ClaimPlausibilityChecked` | Automatische/fachliche Prüfung | Prüfung auf Deckung, Vertragsstatus, Bestandszugehörigkeit, Frist | Freigabe zur Bewertung oder Verdachtsfall |
| `ClaimAssessed` | Schadenhöhe ermittelt | Wiederbeschaffungswert, Selbstbehalt, Sublimits, Unterversicherung berechnet | Entscheidungsvorlage |
| `ExpertAssessmentRequested` | Streit über Schadenhöhe | Sachverständigenverfahren eingeleitet | Neutrale Wertermittlung, ggf. Obmann |
| `ClaimApproved` | Positive Entscheidung | Anspruch dem Grunde und der Höhe nach anerkannt | Auszahlung wird veranlasst |
| `ClaimRejected` | Ablehnung | Schaden abgelehnt (kein Deckungsfall, Obliegenheitsverletzung, Vorsatz) | Begründung an VN; Widerspruch/Ombudsmann möglich |
| `ClaimPartiallyApproved` | Teilanerkennung | Kürzung wegen Unterversicherung/Sublimit/grober Fahrlässigkeit | Teilzahlung; Kürzungsbegründung |
| `DeductibleApplied` | Auszahlungsberechnung | Vereinbarter Selbstbehalt vom Schaden abgezogen | Reduzierte Auszahlungssumme |
| `ClaimPaid` | Auszahlung | Entschädigung an VN überwiesen | Schaden geschlossen; Schadenquote aktualisiert |
| `ClaimReopened` | Nachforderung/neue Fakten | Bereits geschlossener Schaden wieder aufgenommen | Erneute Bewertung |
| `RecoveredItemReported` | Wiederbeschaffung Diebesgut | Gestohlene Sache wieder aufgetaucht | Rückabwicklung/Anrechnung der Entschädigung |

### 4. Fachliche Geschäftsregeln

Nummeriert und einzeln zitierbar. Prozentwerte/Beträge sind marktübliche Richtwerte (siehe Caveats), im System als konfigurierbare Parameter zu führen.

**Wertgrenzen und Sublimits**
1. Der Gesamtwert aller als Wertsachen klassifizierten Gegenstände ist auf den vereinbarten Prozentsatz der Versicherungssumme begrenzt (Standard 20 %, konfigurierbar bis 50 %).
2. Bargeld und Geldkarten-Guthaben außerhalb eines anerkannten Wertschutzschranks sind auf einen absoluten Betrag begrenzt (Richtwert 1.500 €; Bandbreite 1.000–3.500 €).
3. Urkunden, Sparbücher und Wertpapiere außerhalb eines Wertschutzschranks sind absolut begrenzt (Richtwert 7.500 €; verbreitet 2.500–5.000 €).
4. Schmuck, Edelsteine, Perlen, Briefmarken, Münzen sowie Gold-/Platinsachen außerhalb eines Wertschutzschranks sind absolut begrenzt (Richtwert 20.000 €).
5. Bei nachgewiesener Aufbewahrung in einem anerkannten, verschlossenen Wertschutzschrank (≥200 kg oder fachmännisch verankert/eingemauert) entfallen die absoluten Sublimits; es gilt die prozentuale Wertsachengrenze.
6. Für Fahrraddiebstahl (Zusatzbaustein) ist die Entschädigung auf einen Prozentsatz der Versicherungssumme begrenzt (Standard 1 %, erhöhbar bis 5–10 %) oder auf eine feste Summe.
7. Überspannungsschäden (über den Blitz hinaus) sind je Versicherungsfall begrenzt (Richtwert 5 % der Versicherungssumme).
8. Für Hausrat in der Außenversicherung gilt eine eigene Grenze (Richtwert 10 % der Versicherungssumme, Dauer bis 3 Monate).
9. Jede prozentuale Grenze erhöht sich anteilig um die Vorsorge (Richtwert 10 %), da die Vorsorge auf die Versicherungssumme aufschlägt.

**Unterversicherung**
10. Unterversicherung liegt vor, wenn Versicherungswert (Summe aller Neuwerte des Bestands) > Versicherungssumme + Vorsorgebetrag.
11. Ohne Unterversicherungsverzicht wird die Entschädigung anteilig gekürzt: Entschädigung = Schaden × (Versicherungssumme ÷ Versicherungswert) — auch bei Teilschäden.
12. Bei vereinbartem Unterversicherungsverzicht (Voraussetzung: Ansatz ≥ Pauschale je m², Richtwert 650 €/m², korrekte Wohnfläche) unterbleibt die Kürzung; Auszahlung maximal bis Versicherungssumme + Vorsorge.
13. Eine Unterversicherungs-Warnung ist auszulösen, sobald der laufende Bestandswert die Versicherungssumme (+ Vorsorge) übersteigt.

**Selbstbehalt, Schadenhöhe, Deckungssumme**
14. Ein vereinbarter Selbstbehalt (marktüblich 150 €, teils 300/500/1.000 €) wird je Versicherungsfall von der berechneten Entschädigung abgezogen.
15. Die Entschädigung je Versicherungsfall ist auf die Versicherungssumme (+ Vorsorge, + versicherte Kosten) begrenzt.
16. Grundlage der Entschädigung ist der Neuwert/Wiederbeschaffungswert; bei nicht mehr zweckgemäß nutzbaren Sachen der erzielbare Verkaufswert.
17. Bei Reparaturfähigkeit sind die Reparaturkosten (ggf. abzüglich Restwert/Wertminderung) maßgeblich, sofern günstiger als Wiederbeschaffung.
18. Elementarschäden (Zusatzbaustein) können einen eigenen Selbstbehalt tragen (Richtwert 10 % des Schadens, mind. 500 €).

**Fristen**
19. Schäden sind unverzüglich (ohne schuldhaftes Verzögern, praktisch „sofort") zu melden; als Systemfrist praktikabel z. B. 3 Tage nach Kenntnis, konfigurierbar.
20. Bei Einbruchdiebstahl, Raub und Vandalismus ist unverzüglich Anzeige bei der Polizei zu erstatten und eine Stehlgutliste bei Polizei und Versicherer einzureichen; Versäumnis kann zu Leistungskürzung/-freiheit führen.
21. Für die Benennung von Sachverständigen im Sachverständigenverfahren gilt eine Frist von 2 Wochen nach Aufforderung der Gegenseite.
22. Die Regulierungs-/Prüffrist beträgt praxisüblich 4–6 Wochen ab Vorliegen aller Unterlagen; verzögert sich die Zahlung deutlich, können Verzugszinsen entstehen.
23. Die ordentliche Kündigungsfrist beträgt in der Regel 3 Monate zum Ende des Versicherungsjahres; nach einem Schadenfall oder bei Umzug besteht ein außerordentliches Kündigungsrecht (Frist meist 1 Monat).
24. Ein Widerrufsrecht besteht nach Vertragsschluss 2 Wochen in Textform (§§ 8, 9 VVG).

**Plausibilitätsregeln für Schadenmeldungen**
25. Ein gemeldetes Schadendatum vor Versicherungsbeginn (bzw. vor Erstbeitragszahlung) begründet keinen Deckungsanspruch (Plausibilitätsverstoß).
26. Ein gemeldetes Schadendatum nach Vertragsende ist kein Deckungsfall.
27. Betrifft ein Diebstahlschaden einen Gegenstand, der nicht im Bestand geführt/nachweisbar ist, ist der Nachweis (Beleg, Foto, Zeugen) erforderlich; ohne Nachweis droht Kürzung/Ablehnung.
28. Eine gemeldete Schadenursache muss durch die vereinbarten Bausteine gedeckt sein (z. B. Überschwemmung nur mit Elementar-Baustein; Fahrraddiebstahl außerhalb verschlossener Räume nur mit Fahrradbaustein).
29. Die Schadenhöhe eines Einzelgegenstands sollte plausibel zum erfassten/marktüblichen Neuwert passen; grobe Abweichungen sind zu prüfen (Betrugsindikator).
30. Wertsachenschäden sind gegen die anwendbaren Sublimits (abhängig vom Aufbewahrungsort) zu prüfen; der übersteigende Teil ist nicht gedeckt.
31. Vorsätzlich herbeigeführte Schäden sind ausgeschlossen; grob fahrlässig verursachte Schäden können quotal nach Schwere des Verschuldens gekürzt werden (sofern kein Einschluss „grobe Fahrlässigkeit").

### 5. Glossar (alphabetisch)

- **Allgefahrendeckung (unbenannte Gefahren)**: Deckungsform, die alle nicht ausdrücklich ausgeschlossenen Gefahren einschließt; meist Premium-Baustein.
- **Außenversicherung**: Erweiterung des Versicherungsschutzes auf Hausrat, der sich vorübergehend (i. d. R. bis 3 Monate) außerhalb des Versicherungsortes befindet, weltweit, begrenzt (Richtwert 10 % der Versicherungssumme).
- **Bausteine/Deckungserweiterungen**: Optional zubuchbare Zusatzdeckungen (z. B. Elementar, Fahrraddiebstahl, Glas, Überspannung).
- **Combined Ratio (Schaden-Kosten-Quote)**: Summe aus Schadenquote und Kostenquote; unter 100 % versicherungstechnischer Gewinn. In der verbundenen Hausratversicherung lag sie laut GDV 2024 bei 82,8 %.
- **Einbruchdiebstahl**: In den VHB definierter Diebstahl nach Eindringen/Aufbrechen (Einbrechen, Einsteigen, falscher Schlüssel etc.); Abgrenzung zum einfachen Diebstahl, der nur eingeschränkt gedeckt ist.
- **Elementarschäden**: Schäden durch weitere Naturgefahren (Überschwemmung, Rückstau, Erdbeben, Erdsenkung/-rutsch, Schneedruck, Lawinen, Vulkanausbruch); nur mit Zusatzbaustein gedeckt.
- **Entschädigungsgrenze / Sublimit**: Betragliche oder prozentuale Obergrenze der Leistung für bestimmte Sachen/Gefahren (z. B. Wertsachen, Bargeld, Fahrrad).
- **Grobe Fahrlässigkeit**: Schweres Außerachtlassen der Sorgfalt; erlaubt dem Versicherer quotale Leistungskürzung, sofern nicht vertraglich eingeschlossen.
- **Hausrat**: Gesamtheit der beweglichen Sachen eines Haushalts zum Gebrauch, Verbrauch oder zur Ausstattung.
- **Neuwert (Wiederbeschaffungswert)**: Betrag zur Wiederbeschaffung einer Sache gleicher Art und Güte in neuwertigem Zustand; Basis der Entschädigung.
- **Obliegenheiten**: Verhaltenspflichten des VN vor/während/nach dem Schaden (z. B. Meldung, Schadenminderung, Anzeige, Stehlgutliste); Verletzung gefährdet den Versicherungsschutz.
- **Selbstbehalt (Selbstbeteiligung)**: Vom VN je Schadenfall selbst getragener Betrag; senkt den Beitrag (marktüblich 150 €).
- **Stehlgutliste**: Verzeichnis der entwendeten/beschädigten Gegenstände (mit Neuwert), unverzüglich bei Polizei und Versicherer einzureichen.
- **Sturm**: Wetterbedingte Luftbewegung ab Windstärke 8 (Beaufort); darunter kein Versicherungsschutz.
- **Summenanpassung (Index)**: Jährliche Anpassung der Versicherungssumme nach Preisindex zum Schutz vor Unterversicherung.
- **Unterversicherung**: Zustand, in dem der Versicherungswert die Versicherungssumme (+ Vorsorge) übersteigt; führt zu anteiliger Leistungskürzung.
- **Unterversicherungsverzicht**: Klausel, mit der der Versicherer bei ausreichender Summenermittlung (Richtwert 650 €/m²) auf die Unterversicherungsprüfung verzichtet.
- **Versicherungsfall**: Ereignis, für das der Versicherer Entschädigung leistet.
- **Versicherungsort**: Räumlicher Geltungsbereich (Wohnung + zugehörige Räume/Nebengebäude/Garage).
- **Versicherungssumme**: Vereinbarte Höchstentschädigung; Grundlage für Beitrag und prozentuale Grenzen.
- **Versicherungswert**: Tatsächlicher Wert des gesamten Hausrats (i. d. R. Neuwert); Vergleichsgröße zur Versicherungssumme.
- **Vorsorge(-versicherungssumme)**: Automatischer Aufschlag (Richtwert 10 %) auf die Versicherungssumme für unterjährige Wertsteigerungen/Neuanschaffungen.
- **Wertsachen**: Besonders werthaltige Sachkategorien (Bargeld, Urkunden/Wertpapiere, Schmuck/Edelmetalle, Kunst/Antiquitäten, Pelze, Teppiche) mit eigenen Sublimits.
- **Wertschutzschrank (Tresor)**: Anerkanntes Sicherheitsbehältnis (≥200 kg oder verankert/eingemauert); hebt die niedrigen Wertsachen-Sublimits auf.
- **Wiederbeschaffungswert**: siehe Neuwert.
- **Zeitwert**: Neuwert abzüglich Wertminderung für Alter/Abnutzung; in der Hausrat nur bei stark abgenutzten Sachen relevant.
- **Schadenquote (Loss Ratio)**: Verhältnis Schadenaufwand zu (verdienten) Beiträgen; zentrale Rentabilitätskennzahl der Schaden-/Unfallversicherung; grober Zielrichtwert ~70 %.

### 6. Dashboard-Kennzahlen

Konkrete Vorschläge mit fachlicher Begründung und geeigneter Visualisierung.

1. **Schadenquote (Loss Ratio)** — Schadenaufwand ÷ (verdiente) Beiträge × 100. Zentrale Rentabilitätskennzahl; unter 100 % profitabel, grober Zielrichtwert ~65–70 %. Zur Einordnung: Die Combined Ratio (Schaden + Kosten) der verbundenen Hausratversicherung lag laut GDV 2024 bei 82,8 % (rund ein Prozentpunkt höher als im Vorjahr). Visualisierung: KPI-Kachel + Zeitreihe (Liniendiagramm). Aussagekräftig, weil sie Bestand und Schaden in einer Zahl verdichtet.
2. **Schaden-Kosten-Quote (Combined Ratio)** — Schadenquote + Kostenquote. Zeigt das vollständige technische Ergebnis; Schwelle 100 %. Als Branchen-Referenzrahmen: Über alle Schaden-/Unfallsparten verbesserte sich die Combined Ratio 2024 laut GDV von 98,8 % auf 96,1 %. KPI-Kachel mit Ampel (Schwelle 100 %).
3. **Durchlaufzeiten** — Median/Ø-Zeit je Phase: Meldung → Entscheidung, Entscheidung → Auszahlung, sowie Gesamt Meldung → Auszahlung. Prozessqualität; Benchmark Prüffrist 4–6 Wochen. Visualisierung: Balkendiagramm je Phase + Verteilungs-Histogramm, optional gestapelt.
4. **Bestandsentwicklung (Gesamtwert über Zeit)** — Summe der Neuwerte des versicherten Bestands im Zeitverlauf, optional gestapelt nach Kategorie. Zeigt Wertdrift und Unterversicherungsrisiko. Visualisierung: gestapeltes Flächendiagramm.
5. **Anteil Unterversicherungsfälle** — Anteil der Policen/Bestände mit Versicherungswert > Versicherungssumme + Vorsorge. Frühindikator für Leistungskürzungsrisiko. Visualisierung: KPI + Balken nach Tarif/Region.
6. **Verteilung Schadenursachen** — Anzahl und Aufwand je Gefahr (Einbruchdiebstahl, Feuer, Leitungswasser, Sturm/Hagel, Elementar, Glas). Steuert Produkt-/Bausteinstrategie. Visualisierung: Doughnut (Anzahl) + Balken (Aufwand). Realistische Kalibrierung nach GDV 2024 (siehe unten).
7. **Durchschnittliche Schadenhöhe je Gefahr** — Aufwand ÷ Fallzahl je Ursache. Zeigt „teure" vs. „häufige" Gefahren. Visualisierung: Balkendiagramm; Feuer/Elementar typischerweise hoch, Glas niedrig.
8. **Ablehnungs-/Kürzungsquote** — Anteil abgelehnter bzw. gekürzter Schäden (nach Grund: Unterversicherung, Sublimit, Obliegenheit, grobe Fahrlässigkeit, Plausibilität). Qualitäts- und Betrugsindikator. Visualisierung: gestapelter Balken nach Ablehnungsgrund.
9. **Wertsachenanteil je Police** — Wert der Wertsachen ÷ Versicherungssumme, gegen das 20-%-Limit. Zeigt Deckungslücken. Visualisierung: Streudiagramm/Histogramm mit Grenzlinie.
10. **Schadenhäufigkeit / Schadenbedarf** — Anteil Verträge mit Schaden bzw. Ø-Schadenaufwand je Vertrag. Kalkulationsgrundlage. Visualisierung: KPI + Trend.

**Realistische Kalibrierungsdaten (GDV, verbundene Hausratversicherung 2024)** für Testdaten/Dashboards:
- Gesamtleistung 2024: **1.819 Mio. €** (Zuwachs um „ein knappes Zehntel"; nur einmal seit 2000 höher — 2021 mit annähernd 2 Mrd. €). Ø-Schaden je Fall 2024 rund **2.170 €** (2023: 1.980 €). Kumulierte Leistungen seit 2000: rund 33,5 Mrd. €.
- Verteilung nach Gefahr (Fälle / Leistung): Einbruchdiebstahl ~270.000 / **550 Mio. €**; Leitungswasser ~170.000 / **410 Mio. €**; Feuer ~150.000 / **440 Mio. €** (Ø je Fall ~3.110 €, wörtlich ausgewiesen); Sturm/Hagel ~110.000 / **100 Mio. €** (Vorjahr 110 Mio. €); erweiterte Elementar ~50.000 / **280 Mio. €** (2023: 100; 2022: 30; 2021: 860); Glas ~50.000 / **30 Mio. €** (unverändert).
- Separate GDV-Wohnungseinbruch-Statistik 2024: rund **90.000** versicherte Wohnungseinbrüche, Gesamtschaden **350 Mio. €** (20 Mio. € mehr als im Vorjahr), Ø-Schaden je Wohnungseinbruch **3.800 €** (von 3.600 € gestiegen; höchster Wert der letzten 20 Jahre).

## Recommendations
- **Datenmodell zuerst auf Wertsachen-Sublimits und Unterversicherung ausrichten** — das sind die fachlich reichsten Regelbereiche. Wertsachen-Kategorie und Aufbewahrungsort (Wertschutzschrank ja/nein) als First-Class-Attribute je Gegenstand modellieren; alle Grenzen als konfigurierbare Parameter (kein Hardcoding), da anbieterabhängig.
- **Alle Prozent-/Betragsgrenzen als Konfiguration** mit den hier genannten Richtwerten vorbelegen (Wertsachen 20 %, Bargeld 1.500 €, Urkunden/Sparbücher 7.500 €, Schmuck 20.000 €, Fahrrad 1 %, Vorsorge 10 %, Selbstbehalt 150 €, 650 €/m²).
- **Schaden-Lebenszyklus als Zustandsmaschine** mit den Events aus Abschnitt 3 abbilden; Plausibilitätsregeln (25–31) als Vorprüfung vor der Bewertung — sie passen ideal zu einer event-getriebenen Architektur mit Transactional Outbox.
- **Testdaten anhand der GDV-2024-Verteilung generieren** (Ursachenmix und Ø-Schadenhöhen aus dem Kalibrierungsblock), damit Dashboards realistisch wirken und die Kennzahlen plausible Werte zeigen.
- **Benchmarks/Schwellen für Dashboards** setzen: Schadenquote-Ampel bei 70 %/100 % (Sparten-Combined-Ratio 82,8 % als Referenz), Regulierungszeit-Ziel 4–6 Wochen, Unterversicherungswarnung ab Bestandswert > Summe + Vorsorge, Wertsachenwarnung ab Kategoriewert > Sublimit.

## Caveats
- **Wertgrenzen variieren je Anbieter/Tarif** und sind hier als marktübliche Richtwerte, nicht als harte Fakten zu verstehen. Insbesondere: Wertsachen-Gesamtgrenze 20 % (Bandbreite 20–50 %), Bargeld außerhalb Tresor 1.000–3.500 € (Muster 1.500 €), Urkunden/Sparbücher 2.500–7.500 €, Schmuck ~20.000 €, Fahrraddiebstahl 1–10 %.
- **VHB-Versionsstände** unterscheiden sich (2010/2016/2022); Paragraphenverweise variieren. Der GDV-Charakter ist unverbindlich; reale Verträge weichen (meist verbraucherfreundlich) ab.
- **Fristen sind meist als „unverzüglich" formuliert**, nicht als feste Tageszahl; die im System gewählten konkreten Fristen (z. B. 3 Tage) sind eine praktikable Modellierungsentscheidung, kein Bedingungswortlaut.
- **GDV-2024-Zahlen sind gerundet** (Fallzahlen auf 10.000, Leistungen auf 10 Mio. €). Die Ø-Schadenhöhen je Gefahr sind teils aus Leistung/Fallzahl berechnet (nur Gesamt 2.170 € und Feuer 3.110 € sind wörtlich ausgewiesen). Für die erweiterten Elementarschäden 2024 nennt die Quelle zwei abweichende Leistungswerte (280 vs. 230 Mio. €); 280 Mio. € ist plausibler (Summenkonsistenz: 550+440+410+280+100+30 ≈ 1.810 Mio. € ≈ Gesamt 1.819 Mio. €).
- **Einbruchdiebstahl (Hausrat-Kategorie, ~270.000/550 Mio. €) ≠ Wohnungseinbruch-Statistik (~90.000/350 Mio. €)** — erstere umfasst auch Raub und Diebstahl aus Hotels/Krankenhäusern. Bei Dashboard-Beschriftung nicht vermischen.
- Durchschnittlicher Hausratwert eines Vier-Personen-Haushalts und Kategorie-Preisrahmen sind Orientierungswerte für Testdaten, keine normierten Größen.
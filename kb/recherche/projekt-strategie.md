# Portfolio-Projekt-Strategie 2026 für einen Senior Java-Entwickler (Spring Boot + Angular + Events)

## TL;DR
- **Ja, das Projekt lohnt sich** — aber nur, wenn es Tiefe statt Umfang zeigt: ein fachlich glaubwürdiges, gut dokumentiertes Event-getriebenes System aus deiner Domäne (Zeitwirtschaft/Versicherung) schlägt ein breites Feature-Sammelsurium. Der geplante Full-Scope (Spring Boot + Angular + Keycloak + SonarQube + Events + Dashboards + CI/CD) ist in 3 Monaten bei 2–3 Std/Tag **nur mit klarer Priorisierung (Muss/Soll/Kann)** machbar; Keycloak und SonarQube gehören ins „Soll/Kann".
- **Setze auf einen modularen Monolithen mit Spring Modulith 2.0**, nicht auf Microservices. Der Event Publication Registry liefert das Transactional-Outbox-Pattern „gratis" und demonstriert REST + Events glaubwürdig ohne Kafka-Overhead. Over-Engineering (Microservices, Kafka, K8s) ist im Solo-Projekt ein Interview-Rotflag.
- **Mache die KI-Nutzung transparent, aber framet sie als Werkzeug unter deiner Kontrolle.** Der DACH-Markt ist skeptisch (Deutschland hat mit 22 % kombiniertem KI-Vertrauen den niedrigsten Wert der Top-10-Länder der Stack Overflow 2025-Umfrage), gleichzeitig wird KI-Kompetenz zunehmend erwartet — laut JetBrains State of Developer Ecosystem 2025 rechnen 68 % der Entwickler damit, dass KI-Kompetenz zur Jobvoraussetzung wird. Dokumentiere KI in README/ADRs/CLAUDE.md und zeige nachweislich, wo du KI-Vorschläge kritisch geprüft und abgelehnt hast.

## Key Findings

- Recruiter scannen ein GitHub-Profil in Sekunden; entscheidend sind angepinnte Repos, README-Qualität, Architektur-Diagramme und Commit-Historie, nicht die Menge der Repos.
- Für Senior-Portfolios gilt: „Documentation is what separates junior and senior portfolios." Architektur-Docs, ADRs und sichtbare Entscheidungsfindung sind die eigentlichen Senior-Signale.
- Der aktuelle Java-Baseline-Stack 2026: **JDK 25 LTS, Spring Boot 4.0 (GA 20. November 2025, aufbauend auf Spring Framework 7.0 vom 13. November 2025), Jakarta EE 11, Jackson 3**. Spring Boot 4 bietet erstklassige Java-25-Unterstützung bei erhaltener Java-17-Kompatibilität.
- Angular ist 2026 bei **Version 21 (GA 19. November 2025)** mit Standalone Components und zoneless Change Detection als Default (Vitest ersetzt Karma/Jasmine als Standard-Test-Runner); **PrimeNG** ist für datenlastige Dashboards mit Tabellen/Charts die beste Wahl für einen Backend-Entwickler ohne Styling-Ambitionen.
- **Spring Modulith 2.0** (GA 21. November 2025) ist der ideale „modularer Monolith"-Ansatz: verifizierbare Modulgrenzen via ArchUnit und ein Event Publication Registry, das das Transactional-Outbox-Pattern ohne Message-Broker liefert.
- KI-Adoption ist fast universell (JetBrains 2025: 85 % nutzen KI-Tools; Stack Overflow 2025: 84 % nutzen oder planen KI-Nutzung, gegenüber 76 % in 2024), aber das Vertrauen sinkt (laut Stack Overflow Blog vom 29.12.2025 von 40 % auf nur 29 %; 46 % misstrauen aktiv, nur 3 % „highly trust", positive Grundhaltung fiel von 72 % auf 60 %). Hiring-Manager wollen Kandidaten, die KI wie einen „Junior-Pair-Programmer" behandeln, dessen Output sie verantworten.

---

## 1. Marktstandard für Portfolio-Projekte 2026

### Was Recruiter und technische Interviewer erwarten

Zunächst eine ehrliche Einordnung, die sich durch die Recherche zieht: **Für einen Senior mit 8 Jahren Berufserfahrung ist ein Portfolio-Projekt kein Pflichtdokument, sondern ein Differenzierungs- und Gesprächswerkzeug.** In Entwickler-Communities (Blind, r/ExperiencedDevs) herrscht Konsens, dass reine „CRUD-App-Portfolios" bei erfahrenen Entwicklern wenig zählen und Recruiter selten tief in den Code schauen. Der Wert deines Projekts liegt woanders:

1. **Es macht deinen Wechsel glaubwürdig.** Du hast eine Spring-Boot-Zertifizierung, aber kein arbeitsrelevantes Spring-Boot-Projekt und keine Frontend-Praxis. Das Projekt schließt genau diese Lücke sichtbar.
2. **Es liefert Gesprächsstoff für das technische Interview.** Ein interviewbarer Kandidat kann über Architekturentscheidungen, Trade-offs und Fehler reden — genau das, was Senior-Interviews prüfen.
3. **Es zeigt „Projektleiter-Kompetenzen"** (Planung, Entscheidungsdokumentation, Roadmap) für deine zweite Zielposition.

### Überzeugend vs. „Tutorial-Abklatsch"

| Überzeugend (Senior-Signal) | „Tutorial-Abklatsch" (Rotflag) |
|---|---|
| Fachlich nicht-triviale Domäne mit echten Geschäftsregeln | ToDo-App, Webshop, Blog, Weather-App |
| Bewusste Architekturentscheidungen, dokumentiert in ADRs | Alles in einem „God-Service", keine Struktur |
| Modularer Monolith mit klaren Grenzen (ArchUnit-verifiziert) | Microservices ohne Begründung / Over-Engineering |
| Aussagekräftige Tests (Unit, Integration mit Testcontainers, E2E) | Keine Tests oder nur trivialer Happy-Path |
| Saubere Commit-Historie, PR-basiert, Conventional Commits | „final fix", „asdf", „wip" Commits |
| README mit Problemstellung, Architektur-Diagramm, Setup in einem Befehl | Nur `npm install`, sonst leer |
| Ehrliche Reflexion über Grenzen/Trade-offs | Marketing-Sprache, überzogene Claims |

### Umfang vs. Tiefe

**Tiefe schlägt Umfang eindeutig.** Ein Projekt, das eine Domäne sauber, getestet und gut dokumentiert umsetzt, ist wertvoller als fünf halbfertige Repos. Für den DACH-Raum kommt hinzu: Der deutsche Java-Markt ist ein Arbeitnehmermarkt (auf eine offene Java-Vakanz kommen nur wenige qualifizierte Bewerbungen), Versicherung/Finanzdienstleistung ist eine der tiefsten Java-Domänen — deine fachliche Erfahrung ist ein echter Wettbewerbsvorteil, den das Projekt sichtbar machen sollte. Deutsche Tech-Recruiter achten laut Recruiting-Blogs besonders auf einen fokussierten (nicht „Buzzword-Bingo"-)Skill-Nachweis, konkrete Metriken (Testabdeckung, Build-Zeit) und Nachweise moderner Engineering-Praktiken (CI/CD, Testing, Code Reviews).

---

## 2. Technische Best Practices für das Setup (Stand 2026)

### 2.1 Spring Boot Backend — Versionen & Architektur

**Empfohlener Baseline-Stack 2026:**

| Komponente | Empfehlung 2026 | Begründung |
|---|---|---|
| JDK | **Java 25 LTS** (GA Sep 2025, Support bis 2033) | Längster Support-Horizont; Java 21 Oracle-Free-Support endet Sep 2026 |
| Framework | **Spring Boot 4.0** (GA 20. Nov 2025) / Spring Framework 7 (GA 13. Nov 2025) | Aktueller Major-Release; erstklassige Java-25-Unterstützung bei erhaltener Java-17-Kompatibilität, Jakarta EE 11, Jackson 3 |
| Persistenz-Migration | **Flyway** (Default für Solo-Projekt) | SQL-first, erstklassige Spring-Boot-Integration, minimaler Setup; Liquibase nur bei Rollback-/Multi-DB-Bedarf |
| DTO-Mapping | **MapStruct 1.6.3** (stabil seit 9. Nov 2024; 1.7 noch Beta) | Compile-time, keine Reflection |
| Validierung | **Hibernate Validator 9.x** (Jakarta Validation 3.1) | RI für Jakarta EE 11, verlangt Java 17+ |
| Fehler-Responses | **RFC 9457 ProblemDetail** | Moderner Standard für REST-Fehler |
| Integrationstests | **Testcontainers + @ServiceConnection** | Seit Spring Boot 3.1, ersetzt @DynamicPropertySource-Boilerplate |

**Architekturmuster — die zentrale Empfehlung:** Baue einen **modularen Monolithen mit Spring Modulith 2.0** (GA 21. November 2025). Das ist das stärkste Signal, das du senden kannst: In Interviews gilt „modularer Monolith als Default, Microservices als Eskalation". Spring Modulith gibt dir:

- **Verifizierbare Modulgrenzen:** Standardmäßig ist jedes direkte Unterpaket des Hauptpakets ein Anwendungsmodul. `ApplicationModules.of(Application.class).verify()` wirft bei zyklischen Abhängigkeiten oder Zugriff auf interne Typen einen Fehler — ArchUnit-basiert. Spring Modulith 2.0 kann die Struktur sogar beim Startup verifizieren (#1287).
- **Transactional Outbox „gratis":** Das Event Publication Registry persistiert unveröffentlichte Events in der DB (JDBC/JPA). Stürzt die App zwischen Publish und Handling ab, wird das Event beim Neustart erneut zugestellt.

Innerhalb der Module kannst du optional Ports-and-Adapters (Hexagonal) andeuten, aber übertreibe es nicht — für ein 3-Monats-Projekt reicht eine saubere Schichtung pro Modul mit ArchUnit-Regeln.

**RFC 9457 Problem Details** (Fehler-Handling): Support kam mit Spring Framework 6.0 (Spring Boot 3.0). Die `ProblemDetail`-Klasse plus ein `@ControllerAdvice`, das `ResponseEntityExceptionHandler` erweitert, ist 2026 Best Practice für REST-Fehlerantworten (Content-Type `application/problem+json`). Aktivierung über `spring.mvc.problemdetails.enabled=true` (per Default `false`, opt-in). **Wichtiger Fallstrick zum Dokumentieren (z.B. in einem ADR):** Das Property ändert NICHT die Ausgabe des `BasicErrorController`/`DefaultErrorAttributes` — Fehler, die nicht über den `ResponseEntityExceptionHandler` laufen, liefern weiter das Legacy-Format (`timestamp/status/error/path`). Ein bewusster Umgang damit (einheitliches Fehler-Format erzwingen) ist ein Senior-Signal.

### 2.2 Angular mit UI-Framework

**Aktuelle Version:** Angular **21** (GA 19. November 2025) — Standalone Components als Default überall, zoneless Change Detection als Default für neue Projekte (bereits mid-2024 bei über der Hälfte neuer Angular-Apps intern bei Google genutzt), Signal Forms experimentell, **Vitest ersetzt Karma/Jasmine** als Standard-Test-Runner. Signals sind seit Angular 20 stabil.

**UI-Framework-Bewertung für einen Backend-Entwickler ohne Frontend-Erfahrung:**

| Framework | Komponenten | Dashboards/Tabellen/Charts | Lernkurve | Empfehlung |
|---|---|---|---|---|
| **PrimeNG** | 80+ | **Sehr stark** — DataTable mit Sortierung/Filter/Export, Charts eingebaut | Mittel | **Erste Wahl** für datenlastige Dashboards |
| Angular Material | ~40 | Schwächer — keine fertigen Data-Grids/Charts, viel Eigenbau via CDK | Niedrig-mittel | Gut wenn Konsistenz/Zugänglichkeit wichtiger als Feature-Tiefe |
| ng-zorro (Ant Design) | 70+ | Stark (Enterprise) | Mittel | Solide Alternative |
| Taiga UI | 50+ | Modern (Signals/standalone), wächst | Mittel | „Modernstes Angular", aber kleinere Community |

**Klare Empfehlung: PrimeNG.** Für dein Dashboard-Szenario (Event-basierte Statistik-Auswertungen mit Tabellen und Charts) sparst du damit Wochen an Eigenentwicklung, die du mit Angular Materials `mat-table` + CDK selbst bauen müsstest. PrimeNGs `p-table` und die eingebauten Charts decken deinen Bedarf ohne Styling-Arbeit ab.

### 2.3 REST + Event-Handling kombinieren

**Realistisch und interview-kompetent für ein Solo-Projekt:**

1. **REST-API** für synchrone Queries und Commands (mit RFC 9457, Bean Validation, OpenAPI/springdoc).
2. **Interne Events via Spring Application Events** + Spring Modulith `@ApplicationModuleListener` (kombiniert `@Transactional`, `@TransactionalEventListener`, `@Async`) für Nebeneffekte und eventual consistency zwischen Modulen.
3. **Transactional Outbox** über das Spring Modulith Event Publication Registry — persistiert Events in der Tabelle `event_publication` innerhalb derselben Transaktion.

**Über-Engineering-Risiko (vermeiden!):** Kafka, RabbitMQ oder Microservices sind für ein Solo-Portfolio ein Rotflag, wenn nicht sauber begründet. Interviewer filtern gezielt nach der Reaktion „Klar, Microservices sind der moderne Standard" (Rotflag). **Wenn du ein Broker zeigen willst,** dann als optionale, dokumentierte Erweiterung: Spring Modulith kann Events nach Kafka externalisieren — aber die Kernarchitektur bleibt der Monolith. **Wichtige Regel zum Dokumentieren:** Die publizierende Methode MUSS `@Transactional` sein, sonst greift die Outbox-Garantie nicht.

### 2.4 Keycloak & SonarQube — lohnt sich das?

**Keycloak:** Sinnvoll als Docker-Compose-Service, der als OAuth2/OIDC-Authorization-Server dient, während dein Spring-Boot-Backend als **OAuth2 Resource Server** (JWT-Validierung via Spring Security) und Angular als Client fungiert. Das ist ein realistisches, in Interviews gut erklärbares Enterprise-Muster. **Aufwand-Nutzen:** mittlerer Aufwand (Realm-Konfiguration, Realm-Export als JSON ins Repo für Reproduzierbarkeit), hoher Signalwert für Versicherungs-/Enterprise-Kontext. **Priorität: Soll.** Alternative bei Zeitdruck: Spring Boot als Resource Server mit einem einfacheren OAuth2-Setup.

**SonarQube:** Für ein Solo-Projekt ist die lokale SonarQube-Instanz im Docker Compose Overkill in der Wartung. **Besser: SonarQube Cloud (ehemals SonarCloud)** — kostenlos für öffentliche Repos, direkt in GitHub Actions integrierbar, liefert ein sichtbares Quality-Gate-Badge im README. **Priorität: Soll/Kann.** Der Signalwert (Badge + Quality Gate) ist hoch bei niedrigem Wartungsaufwand.

### 2.5 Test-Strategie (deine Stärke sichtbar machen)

Du hast Playwright- und JUnit5-Erfahrung — das ist ein echter Trumpf, den viele Backend-Entwickler nicht haben. Mache ihn sichtbar:

| Ebene | Tool | Zweck |
|---|---|---|
| Unit | JUnit 5 (+ Mockito) | Geschäftslogik isoliert |
| Integration | **Testcontainers + @ServiceConnection** | Echte PostgreSQL statt H2 — Senior-Signal |
| Architektur | **ArchUnit** (via Spring Modulith `verify()`) | Modulgrenzen erzwingen, keine Zyklen |
| E2E | **Playwright** | Angular-Frontend gegen laufendes Backend — deine Stärke! |

**Coverage-Erwartung:** Keine Fixierung auf eine Prozentzahl, aber ein sichtbares Coverage-Badge (z.B. via JaCoCo + SonarQube Cloud) und Fokus auf sinnvolle Tests statt trivialer Getter-Tests. In Anschreiben/README wirkt eine konkrete Aussage wie „85 % Coverage in der Domänenschicht" stärker als eine pauschale. Wichtig: Playwright-E2E-Tests in die CI einbinden zeigt echte Testautomatisierungs-Kompetenz.

---

## 3. KI-Sichtbarkeit im Portfolio (2026)

### Die Datenlage: Adoption hoch, Vertrauen niedrig — besonders in DACH

- **Adoption:** JetBrains State of Developer Ecosystem 2025: 85 % nutzen KI-Tools, 62 % mindestens einen Coding-Assistenten; zugleich rechnen 68 % damit, dass KI-Kompetenz zur Jobvoraussetzung wird. Stack Overflow 2025: 84 % nutzen oder planen KI-Nutzung (2024: 76 %).
- **Vertrauen sinkt:** Stack Overflow Blog (29.12.2025): Vertrauen in die Genauigkeit von KI-Output fiel von 40 % auf 29 %; 46 % misstrauen aktiv, nur 3 % „highly trust"; positive Grundhaltung fiel von 72 % auf 60 %. Erfahrene Entwickler sind am skeptischsten (höchste „highly distrust"-Rate).
- **DACH-spezifisch:** Deutschland hat mit 22 % kombiniertem KI-Vertrauen den niedrigsten Wert der Top-10-Länder der Stack Overflow 2025-Umfrage (49.000+ Antworten aus 177 Ländern; USA 28 %, Polen 26 %, Kanada/Frankreich 25 %, UK 23 %, Deutschland 22 %). Das ist für deine Zielgruppe hochrelevant.
- **„AI slop"-Backlash:** Recruiter berichten von einer Flut generischer KI-Bewerbungen; perfekt-generisch wirkende Artefakte werden misstrauisch beäugt.

### Die Synthese: KI zeigen — aber als kontrolliertes Werkzeug

Gleichzeitig gilt: KI-Kompetenz wird zunehmend erwartet. Recruiting-Analysen beschreiben KI-Verweigerung als Rotflag und den idealen Kandidaten als jemanden, der KI „wie einen Junior-Pair-Programmer behandelt, dessen Output er verantwortet — keine Blackbox, keine Bedrohung, ein Junior". Interviews prüfen zunehmend, ob du weißt, **wann du KI NICHT einsetzt.**

**Deine Strategie:** Transparente, aber selbstbewusste Dokumentation, die Kompetenz statt Abhängigkeit vermittelt. Konkret:

**1. `AI-USAGE.md` oder ein README-Abschnitt „KI im Entwicklungsprozess"** — Struktur-Empfehlung:

```markdown
## KI-Nutzung in diesem Projekt

Dieses Projekt nutzt Claude Code bewusst als Werkzeug im Entwicklungsprozess —
nicht als Feature im Produkt. Transparenz-Prinzip: Jeder KI-Beitrag wird
von mir fachlich geprüft und verantwortet.

### Wofür ich KI eingesetzt habe
- **Story-Schnitt:** Vorschläge zum Zerlegen von Epics in Stories inkl.
  Akzeptanzkriterien (finale Entscheidung + Priorisierung durch mich)
- **Code-Review:** KI als erster Review-Pass; Fehlerhinweise, die ich
  bewertet, angenommen oder begründet abgelehnt habe (siehe PR-Kommentare)
- **Dokumentation:** Erstentwürfe für JavaDoc/README, von mir überarbeitet

### Wo ich KI-Vorschläge abgelehnt habe (bewusste Entscheidungen)
- ADR-004: KI schlug Kafka vor — abgelehnt zugunsten Spring Modulith
  Event Registry (Begründung: Solo-Projekt, kein Broker-Overhead nötig)
- PR #23: KI-generierter Mapper umging Bean Validation — manuell korrigiert

### Was ich NICHT von KI habe machen lassen
- Architekturentscheidungen (nur nach eigener Abwägung, dokumentiert in ADRs)
- Sicherheitskritische Auth-Konfiguration (Keycloak/JWT manuell verifiziert)
```

**2. `CLAUDE.md`** — als Instruktions-Datei für den KI-Agenten (nicht Projektbeschreibung!). Faustregel: README beantwortet „Was ist das?", CLAUDE.md „Wie soll daran gearbeitet werden?". Nur umsetzbare Anweisungen: Architekturregeln, Business-Constraints, Workflow — keine Linter-Regeln (die liest das Tool selbst). Unter ~200 Zeilen halten. Optional auf den `AGENTS.md`-Standard verweisen (seit Mitte 2025, von 60.000+ Repos adaptiert).

**3. ADRs, die KI-Vorschläge dokumentieren** — der stärkste Kompetenznachweis: zeige eine Entscheidung, bei der du einen KI-Vorschlag *begründet verworfen* hast. Das beweist kritisches Urteilsvermögen — genau das, was skeptische DACH-Interviewer sehen wollen.

**Warnung:** Vermeide es, das gesamte Repo wie KI-generiert wirken zu lassen (generische READMEs, Emoji-Overload, identische Formulierungen). Deine 8 Jahre Domänenerfahrung und persönliche Stimme müssen durchscheinen.

---

## 4. CI/CD-Erwartungen (GitHub Actions)

Klar gegliedert nach Erwartungshaltung:

### Minimum (Pflicht — sonst wirkt es unfertig)
- **Build + Test bei jedem Push/PR** (Maven/Gradle, `mvn verify`)
- **Automatisierte Tests laufen in CI** (JUnit5, Testcontainers — Docker ist in GitHub-Actions-Runnern verfügbar)
- **Branch Protection auf `main`:** PR-Pflicht, Status-Checks müssen grün sein
- **Dependabot** aktiviert (Dependency-Updates — Ein-Klick-Setup)
- **`.gitignore`, LICENSE, README** vorhanden

### Pluspunkt (hebt dich klar ab)
- **Linting/Formatierung** (Spotless/Checkstyle für Java, ESLint/Prettier für Angular)
- **SonarQube Cloud-Integration** mit Quality-Gate-Badge
- **Code-Coverage-Report** (JaCoCo) + Badge
- **Security-Scanning:** Trivy (Container-Image-Scan) und/oder OWASP Dependency-Check / `dependency-review-action`
- **Container-Build** (Dockerfile-Build + optional Push, Buildpacks via `bootBuildImage`)
- **Playwright-E2E in CI** (mit Caching der Browser)
- **Conventional Commits** + commitlint-Check im PR
- **Dependency-Caching** (Maven/npm) für schnellere Builds
- **Actions auf Commit-SHA/Tag pinnen** (Supply-Chain-Sicherheit) — Senior-Detail

### Over-Engineering / unnötig für ein Solo-Projekt
- **Matrix-Builds über viele JDK-Versionen** (eine LTS reicht; Matrix nur wenn du Multi-Version-Support demonstrieren willst)
- **Semantic-Release mit vollautomatischem Versioning/Changelog** (nett, aber Aufwand > Nutzen bei Solo)
- **Self-hosted Runner** (die von SonarQube-Tutorials empfohlene EC2-Instanz ist für dich unnötig — nutze GitHub-hosted Runner + SonarQube Cloud)
- **Deployment-Pipelines zu K8s/Cloud** (du hast bewusst kein Hosting geplant — das ist völlig legitim; lokales Docker Compose genügt)
- **Nexus/Artifactory-Artifact-Repository**

**Konkrete Empfehlung:** Eine einzige, saubere `ci.yml` (Build → Lint → Test → Coverage → Sonar → Container-Build) plus Dependabot + Branch Protection ist genau das richtige Niveau. Ein sichtbares grünes Badge-Set (Build, Coverage, Quality Gate) im README-Kopf ist mehr wert als eine überladene Pipeline.

---

## 5. Umgang mit fehlender Praxiserfahrung

### Ehrlichkeit: klug oder schädlich?

**Kluge Ehrlichkeit (im Projekt):** In ADRs und Learning-Notes offen dokumentieren, *warum* du eine Technologie so eingesetzt hast und was du dabei gelernt hast, ist ein **Stärke-Signal** — es zeigt Reflexionsfähigkeit und Lernkompetenz. Formulierungen wie „Erste bewusste Anwendung von Spring Modulith; Entscheidung X nach Abwägung Y getroffen" wirken souverän.

**Schädliche Ehrlichkeit (im Bewerbungskontext):** Selbstabwertung („Ich kann eigentlich kein Angular", „mein erstes richtiges Spring-Projekt") gehört NICHT ins README oder Anschreiben. Framing ist alles:

| Statt (schädlich) | Besser (souverän) |
|---|---|
| „Ich habe keine Frontend-Erfahrung" | „Fokus des Projekts liegt auf Backend-Architektur; Frontend bewusst mit PrimeNG umgesetzt, um Styling-Aufwand zu minimieren" |
| „Mein erstes Spring-Boot-Projekt" | „Umsetzung meiner Spring-Professional-Zertifizierung in einem produktionsnahen Projekt" |
| „Ich bin schlecht in Doku" | (nicht erwähnen — stattdessen gute Doku zeigen) |

Deine **8 Jahre Java, Docker, Testautomatisierung und Domänenerfahrung** sind die Grundlage — das Projekt ist der *Transfer* dieser Stärken in einen modernen Stack, nicht ein Neuanfang. Genau so solltest du es rahmen.

### README-Struktur-Vorlage

```markdown
# [Projektname] — z.B. "ZeitwerkFlow: Event-getriebene Zeitwirtschaft"

[Badges: Build | Coverage | Quality Gate | License]

## Das Problem
1–2 Sätze: Welches fachliche Problem aus Zeitwirtschaft/Versicherung löst das?

## Warum dieses Projekt
Kontext: Backend-Entwickler mit 8 J. Java-/Domänenerfahrung, demonstriert
modernen Spring-Boot-4-/Angular-Stack mit Event-getriebener Architektur.

## Architektur
[C4-/Modul-Diagramm] — Modularer Monolith (Spring Modulith), REST + Events
Kurze Erklärung der Module und ihrer Grenzen.

## Tech-Stack
Java 25 · Spring Boot 4 · Spring Modulith · PostgreSQL · Flyway ·
Angular 21 · PrimeNG · Keycloak · Docker Compose

## Quick Start (ein Befehl)
```
docker compose up
```
→ App unter http://localhost:4200, API unter :8080, Keycloak unter :8180

## Architektur-Entscheidungen
Siehe [docs/adr/](docs/adr/) — u.a. Modulith statt Microservices,
Event Registry statt Kafka, PrimeNG statt Material.

## Tests
Unit (JUnit5) · Integration (Testcontainers) · Architektur (ArchUnit) ·
E2E (Playwright). Ausführen: `mvn verify` / `npm run e2e`

## KI im Entwicklungsprozess
Siehe [AI-USAGE.md](AI-USAGE.md)

## Roadmap / Projektplanung
Siehe [GitHub Projects Board](link) — Epics, Stories, Sprints
```

### Commit-Historie & Workflow

- **Conventional Commits** durchgängig: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`. Ermöglicht automatische Changelogs und wirkt professionell.
- **PR-basiertes Arbeiten auch solo:** Feature-Branch → PR gegen `main` → CI grün → Merge (squash für saubere Historie). Nutze die PR-Beschreibung, um Entscheidungen und KI-Reviews zu dokumentieren. Das simuliert Team-Workflow und ist in Interviews vorzeigbar.
- **Branch Protection** auf `main`: erzwingt den Workflow und verhindert Direkt-Commits.
- **Keine** „final final fix"-, „asdf"-, „wip"-Commits. Squashe/rebase vor dem Merge.
- **GitHub Issues/Projects aktiv nutzen:** Epics als Milestones/Labels, Stories als Issues mit Akzeptanzkriterien, Board mit Spalten (Backlog/In Progress/Review/Done), Sprints als Iterationen. Das ist gerade für die **Projektleiter-Zielposition** Gold wert.

---

## Zusatz: Projektdomänen-Vorschläge (passend zu deiner Erfahrung)

Alle drei rechtfertigen REST + Events + Dashboards natürlich und meiden den Tutorial-Charakter:

1. **„ZeitwerkFlow" — Zeitwirtschaft/Workforce:** Mitarbeiter erfassen Zeitbuchungen (REST). Events wie `TimeBookingRecorded`, `OvertimeThresholdExceeded`, `AbsenceRequested` triggern nachgelagerte Verarbeitung (Saldoberechnung, Genehmigungs-Workflow, Benachrichtigung). Dashboard: Überstunden-Trends, Abwesenheitsquoten, Saldo-Verteilung. **Stärkste Wahl** — nutzt deine Zeitwirtschafts-Domäne direkt.

2. **„ClaimStream" — Kfz-Unfall-Schadenmeldung:** Schadenmeldung anlegen (REST), Statusübergänge als Events (`ClaimReported` → `ClaimUnderReview` → `ClaimSettled`/`ClaimRejected`). Event-getriebene Regeln (z.B. automatische Deckungsprüfung). Dashboard: Durchlaufzeiten, Schadenquote, offene vs. abgeschlossene Fälle. Nutzt deine Versicherungs-/Unfall-Kfz-Erfahrung.

3. **„PolicyLedger" — Bestandsverwaltung leichtgewichtig:** Verträge/Bestände mit Zustandsänderungen als Events, Beitragsberechnung, Kündigungs-/Verlängerungs-Workflows. Dashboard: Bestandsentwicklung, Storno-Quoten.

Der Domänen-Vorteil: Ein Interviewer aus der Versicherungsbranche erkennt sofort, dass du das Geschäft verstehst — das differenziert dich stark von generischen Bewerbern.

## Zusatz: Machbarkeit in 3 Monaten (2–3 Std/Tag)

**Realistische Einschätzung:** Bei ~180–270 Gesamtstunden ist der volle Scope **ambitioniert, aber machbar — wenn du priorisierst.** Das Frontend (Angular, für dich neu) ist der größte Zeitrisiko-Faktor. Priorisierung:

| Priorität | Umfang |
|---|---|
| **MUSS** | Spring Boot 4 Backend, modularer Monolith mit Spring Modulith, REST-API mit RFC 9457, PostgreSQL + Flyway, interne Events + Event Registry (Outbox), JUnit5 + Testcontainers + ArchUnit, Docker Compose, GitHub Actions CI (Build/Test), README + ADRs + Issues/Projects, Conventional Commits/PR-Workflow |
| **SOLL** | Angular 21 + PrimeNG Frontend mit Dashboard, Playwright-E2E, SonarQube Cloud + Coverage-Badge, saubere KI-Dokumentation (AI-USAGE.md, CLAUDE.md) |
| **KANN** | Keycloak-Auth (OAuth2 Resource Server), Container-Security-Scan (Trivy), Event-Externalisierung nach Kafka als dokumentierte Erweiterung |
| **WEGLASSEN** | Microservices, K8s, Cloud-Deployment, Matrix-Builds, Semantic-Release, self-hosted Runner |

**Empfohlener Zeitplan:** Monat 1 = Backend-Kern (Module, REST, Events, Tests, CI). Monat 2 = Angular/PrimeNG-Frontend + Dashboard + E2E. Monat 3 = Keycloak, Sonar, Doku-Politur, ADRs, Roadmap. **Wenn die Zeit knapp wird, opfere Keycloak zuerst, dann reduziere den Frontend-Umfang auf ein Dashboard + eine CRUD-Ansicht** — Backend-Tiefe und Doku sind wichtiger als Frontend-Breite.

## Zusatz: Rolle für die Zielposition „Projektleiter kleinerer technischer Projekte"

Hier überzeugt zusätzlich die **sichtbare Planung und Steuerung**, nicht nur der Code:
- **GitHub Projects Board** mit Epics/Stories/Sprints als Beweis für agile Planungskompetenz
- **ADRs** als Beweis für strukturierte Entscheidungsfindung und Trade-off-Bewusstsein
- **Roadmap** im README (was ist umgesetzt, was wäre der nächste Schritt)
- **Retrospektive/Learnings-Dokument** am Projektende (was lief gut, was würdest du anders machen)
- Die **KI-Nutzung als Prozess-Governance** (wie du KI-Reviews in den Workflow integriert und Qualität gesichert hast) ist genau die Art von Prozessdenken, die eine Projektleiter-Rolle verlangt.

## Recommendations

1. **Sofort (Woche 1):** Repo aufsetzen mit modularem Monolith-Skelett (Spring Boot 4, Spring Modulith), Docker Compose (PostgreSQL), GitHub Actions Basis-CI, Branch Protection, Conventional Commits, GitHub Projects Board. Wähle „ZeitwerkFlow" (Zeitwirtschaft) als Domäne.
2. **Monat 1:** Backend-Kern fertig — REST + Events + Outbox + Tests (inkl. ArchUnit). Erste ADRs (Modulith statt Microservices, Registry statt Kafka).
3. **Monat 2:** Angular 21 + PrimeNG Frontend, ein solides Dashboard mit Charts/Tabelle, Playwright-E2E in CI. Beginne AI-USAGE.md parallel zu pflegen.
4. **Monat 3:** SonarQube Cloud + Badges, Keycloak (falls Zeit), Doku-Politur, Retrospektive, Roadmap.
5. **Benchmark zum Umsteuern:** Wenn Ende Monat 2 das Frontend nicht steht, streiche Keycloak und reduziere das Frontend auf Dashboard + eine Ansicht. Backend-Tiefe + Doku haben Vorrang.

## Caveats

- **Quellenlage:** Viele Portfolio-/Recruiting-„2026"-Artikel stammen aus SEO-Blogs mit teils widersprüchlichen Zahlen (z.B. „11 vs. 30 vs. 90 Sekunden" Scan-Zeit) — diese sind als Richtungsindikatoren, nicht als harte Fakten zu lesen. Die Kernaussagen (Tiefe > Umfang, Doku als Senior-Signal) sind aber konsistent.
- **DACH-spezifische Portfolio-Daten** sind dünn; die DACH-Aussagen stützen sich auf deutsche Recruiting-Blogs und die länderaufgeschlüsselten Stack-Overflow-/JetBrains-Surveys, nicht auf eine dedizierte Studie.
- **Versionsangaben** für Flyway/Liquibase-Release-Trains 2026 stammen teils aus vendor-nahen Blogs und sind als ungefähr zu behandeln; die Spring-/Angular-/Modulith-Versionen sind über offizielle Quellen bestätigt.
- **MapStruct 1.7** war Anfang 2026 noch Beta — nutze die stabile 1.6.3, sofern 1.7 bis zum Projektstart nicht GA ist.
- Die Einschätzung „KI transparent zeigen" ist eine abgewogene Empfehlung: In einem sehr konservativen Umfeld (manche Versicherer) kann übermäßige KI-Betonung auch Skepsis wecken — halte den AI-USAGE-Abschnitt sachlich und betone durchgängig deine Verantwortung und Prüfung.
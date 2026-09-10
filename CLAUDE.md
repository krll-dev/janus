# CLAUDE.md

Diese Datei gibt Claude Code Kontext für die Arbeit in diesem Repository.

## Projekt

**janus** — Event-getriebene Bestandsführung für die private Hausratversicherung: Verträge,
Wertsachen-Inventar mit Sublimits, Unterversicherungsprüfung und Schadenregulierung.

Solo-Portfolio-Projekt eines Senior-Java-Entwicklers (Wechselziel Spring Boot / Angular).
Fachliche und strategische Grundlagen liegen unter `kb/recherche/` (siehe unten) — bei
fachlichen Fragen (Geschäftsregeln, Domänenbegriffe, Sublimits, Fristen) dort zuerst nachsehen,
nicht raten oder erfinden.

Geplanter Tech-Stack (noch keine Implementierung vorhanden):

- Backend: Spring Boot 4, Spring Modulith (modularer Monolith, Event Publication Registry statt
  Message-Broker), PostgreSQL
- Frontend: Angular 21, PrimeNG
- Module (fachlich): `policy`, `inventory`, `claim`, `shared`

## Aktueller Stand

Das Projekt befindet sich in der Ersteinrichtung. Es existiert noch kein Anwendungscode.
Vorhanden sind:

- `.github/ISSUE_TEMPLATE/` — Issue-Templates (bug, chore, story, adr-proposal) für die spätere
  Arbeit am Backlog
- `docs/adr/` — Architecture Decision Records
- `kb/recherche/` — Rechercheergebnisse (fachliche Ausarbeitung, Projektstrategie)
- `README.md` — bewusst noch leer, wird vom Nutzer selbst befüllt
- `LICENSE` — MIT

GitHub Actions Workflows gibt es noch nicht; sie werden erst angelegt, wenn die Implementierung
beginnt. Schlage sie nicht ungefragt vor.

## Arbeitsweise / Konventionen

- **Sprache:** Projektdokumentation (ADRs, Issues, Kommentare, Commit-Nachrichten) ist auf
  Deutsch. Code, Identifier und technische Begriffe bleiben Englisch.
- **Kanban statt Sprints** (siehe [0002-github-board.md](docs/adr/0002-github-board.md)): Aufgaben
  werden über das GitHub-Board gezogen, wenn Zeit ist — keine Sprint-Planung.
- **Architekturentscheidungen als ADR dokumentieren.** Format: siehe
  [docs/adr/000X-adr-template.md](docs/adr/000X-adr-template.md). Bei nicht-trivialen
  Entscheidungen (auch wenn Claude sie vorschlägt) einen ADR-Entwurf anbieten, nicht einfach
  stillschweigend umsetzen.
- **KI-Transparenz ist ein bewusstes Projektziel** (siehe `kb/recherche/projekt-strategie.md`):
  KI-Beteiligung an Entscheidungen soll nachvollziehbar bleiben. Das ADR-Template und das
  Issue-Template `adr-proposal.yml` haben dafür ein eigenes Feld. Wenn ein Vorschlag von Claude
  kommt, das im ADR/Issue auch so benennen statt es zu verschleiern.
- **Issues über die bestehenden Templates anlegen** (`bug`, `chore`, `story`, `adr-proposal`),
  nicht freihändig. Neue Story-/Bug-Issues sollen, wo sinnvoll, auf die fachliche Ausarbeitung in
  `kb/recherche/fachliche-ausarbeitung.md` verweisen.
- **Keine Workflows, CI/CD oder Tooling-Konfiguration anlegen, bevor nicht explizit danach
  gefragt wird** — das kommt bewusst erst mit dem Start der Implementierung.

## Struktur

```
docs/adr/            Architecture Decision Records
kb/recherche/         Recherche-/Strategiedokumente (Hintergrundwissen, keine Entscheidungen)
.github/ISSUE_TEMPLATE Issue-Vorlagen für Backlog-Arbeit
```

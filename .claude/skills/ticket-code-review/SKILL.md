---
name: ticket-code-review
description: >
  Führt für den aktuellen Feature-Branch ein Code-Review mit /code-review high
  durch und postet jeden Vorschlag als eigenen Kommentar-Thread auf dem
  zugehörigen PR. Bezieht dafür das verlinkte GitHub-Issue (aus der
  Branch-Namenskonvention "<issue-nr>-...") als fachlichen Kontext mit ein.
  Nutze diesen Skill, wenn im janus-Projekt ein Review des aktuellen
  Feature-Branch gegen den PR gewünscht ist — auch bei Formulierungen wie
  "review den PR", "schau dir die Änderungen im PR an" oder "mach ein
  Ticket-Review". Voraussetzung ist ein existierender PR für den aktuellen
  Branch; ohne PR bricht der Skill sofort ab, ohne ein Review zu starten.
---

# Ticket-bezogenes PR-Review

Dieser Skill kombiniert `/code-review high` mit dem fachlichen Kontext aus dem
GitHub-Issue, das dem aktuellen Feature-Branch zugrunde liegt, und postet jeden
gefundenen Vorschlag als eigenen Kommentar-Thread auf dem PR (`--comment`).

## Ablauf

1. **PR zum aktuellen Branch suchen.** Aktuellen Branch ermitteln (`git branch
   --show-current`) und prüfen, ob dazu ein PR existiert:

   ```bash
   gh pr list --repo krll-dev/janus --head <branch> --state all --json number,url,state
   ```

   - **Kein PR gefunden:** Dem Nutzer kurz mitteilen ("Kein PR für Branch
     `<branch>` gefunden — Review wird nicht gestartet.") und **abbrechen**.
     Keinen PR anlegen, keinen Review-Lauf starten.
   - PR gefunden: PR-Nummer für die weiteren Schritte merken. Bevorzugt einen
     offenen PR; falls nur ein geschlossener/gemergter existiert, kurz beim
     Nutzer nachfragen, ob trotzdem darauf reviewt werden soll.

2. **Zugehöriges Issue ermitteln.** Die Branch-Namenskonvention dieses Repos
   ist `<issue-nr>-<kurzbeschreibung>` (z. B. `3-chore-backend-skelett...` →
   Issue #3). Die führende Zahl extrahieren.

   - Keine führende Zahl im Branch-Namen gefunden: Dem Nutzer kurz mitteilen,
     dass kein Issue automatisch zugeordnet werden konnte, und ohne
     Ticket-Kontext mit Schritt 4 fortfahren (Review nicht deswegen
     abbrechen).

3. **Ticket lesen.** Das Issue über die GitHub CLI lesen — das ist ohne
   Rückfrage erlaubt:

   ```bash
   gh issue view <issue-nr> --repo krll-dev/janus --json title,body,labels,url
   ```

   Daraus die fachliche Anforderung kurz zusammenfassen (worum geht es, welche
   Akzeptanzkriterien/Geschäftsregeln sind relevant). Diese Zusammenfassung
   dient als Kontext für das Review — nicht raten oder ergänzen, was nicht im
   Issue steht.

4. **Review starten.** `/code-review` mit Level `high` und `--comment` auf den
   PR laufen lassen, ergänzt um die Ticket-Zusammenfassung aus Schritt 3 als
   Kontext (z. B. als kurzer Hinweis vor dem eigentlichen Review-Aufruf: "Zum
   fachlichen Hintergrund: Issue #<n> verlangt ..."). Der Review soll damit
   auch beurteilen können, ob die Änderungen die Ticket-Anforderung erfüllen,
   nicht nur, ob der Code für sich genommen korrekt ist.

   `--comment` sorgt dafür, dass jeder Befund als eigener Inline-Kommentar
   (= eigener Thread) auf dem PR landet, wie vom Nutzer gewünscht. Der Inhalt
   der einzelnen Threads folgt dem Standardformat von `/code-review` — das
   wird hier bewusst nicht angepasst (kann später bei Bedarf verfeinert
   werden).

5. **Ergebnis melden.** Nach Abschluss kurz zusammenfassen: PR-Link, Anzahl
   geposteter Kommentare, ob das Issue als Kontext einbezogen werden konnte.

## Hinweise

- Voraussetzung ist ein eingeloggtes `gh` (`gh auth status`). Wenn nicht
  eingeloggt, den Nutzer darauf hinweisen statt selbst einen Login-Flow zu
  starten.
- Dieser Skill schreibt nur PR-Kommentare (über `/code-review --comment`),
  keine Commits, keine Änderungen am Code, kein Merge.
- Repo ist fest `krll-dev/janus` — dieser Skill gilt nur für dieses Projekt
  (siehe CLAUDE.md, Konvention: keine Workflows/Tooling ungefragt anlegen —
  dieser Skill selbst zählt nicht dazu, da er nur bestehende Skills/CLI-Tools
  kombiniert).

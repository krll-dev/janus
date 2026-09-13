---
name: github-issue
description: >
  Legt GitHub Issues im Repo krll-dev/janus über die bestehenden Issue-Templates
  (.github/ISSUE_TEMPLATE/bug.yml, chore.yml, story.yml, adr-proposal.yml) mit der
  GitHub CLI (gh) an. Nutze diesen Skill immer, wenn im janus-Projekt eine Story,
  ein Bug, ein Chore oder ein ADR-Vorschlag als GitHub Issue angelegt werden soll —
  auch wenn nur beiläufig "leg dafür ein Issue an", "mach daraus eine Story",
  "das sollten wir als Bug tracken" oder ähnliches gesagt wird, nicht nur bei
  expliziter Nennung von "gh issue create". Gilt nicht für Issues in anderen
  Repos und nicht fürs freihändige Anlegen ohne Template (siehe CLAUDE.md).
---

# GitHub Issues für janus anlegen

Dieses Repo verlangt laut [CLAUDE.md](../../../CLAUDE.md), dass Issues über die
bestehenden Templates unter `.github/ISSUE_TEMPLATE/` angelegt werden, nicht
freihändig. Dieser Skill baut aus einem Template + den Antworten des Nutzers
den passenden `gh issue create`-Aufruf.

## Ablauf

1. **Template wählen.** Vier Typen stehen zur Verfügung:
   - `bug.yml` — Fehlverhalten in bestehendem Code
   - `chore.yml` — Aufgaben ohne fachlichen Bezug (CI/CD, Doku, Tooling, Deps)
   - `story.yml` — fachliche/technische Arbeitseinheit ("Als ... möchte ich ...")
   - `adr-proposal.yml` — Architekturentscheidung, die später als ADR dokumentiert wird

   Wenn aus dem Kontext nicht eindeutig hervorgeht, welches Template passt, kurz
   nachfragen statt zu raten.

2. **Template lesen.** Lies die gewählte Datei unter `.github/ISSUE_TEMPLATE/`
   direkt — nicht aus dem Gedächtnis rekonstruieren. Die Felder (Reihenfolge,
   Pflichtfelder, Dropdown-Optionen) können sich ändern; das Template ist die
   einzige Quelle der Wahrheit dafür.

3. **Antworten sammeln.** Gehe die Felder des Templates durch und sammle die
   Werte — entweder aus dem, was der Nutzer bereits in der Konversation gesagt
   hat, oder durch gezielte Rückfrage bei den `required: true`-Feldern. Leere
   optionale Felder sind ok und werden im Body weggelassen.

   Bei `story` und `bug` gilt die Konvention aus CLAUDE.md: wo sinnvoll, im
   Feld "Fachlicher Kontext" auf die fachliche Ausarbeitung verweisen
   (`kb/recherche/fachliche-ausarbeitung.md`, z. B. eine konkrete Geschäftsregel
   oder ein Event-Name). Prüfe kurz dort nach statt einen Verweis zu erfinden —
   wenn nichts Passendes drinsteht, das Feld einfach ohne Verweis füllen.

   Bei `adr-proposal` ist das Dropdown "KI-Beteiligung an diesem Vorschlag"
   Pflicht und dient der KI-Transparenz (siehe CLAUDE.md-Projektziel). Beantworte
   es ehrlich danach, ob die Idee für dieses Issue von Claude oder vom Nutzer kam.

4. **Body zusammenbauen** mit dem Helper-Script, statt den YAML-Aufbau von Hand
   nachzubilden:

   ```bash
   python3 .claude/skills/github-issue/scripts/build_issue.py \
     .github/ISSUE_TEMPLATE/<template>.yml \
     <answers.json>
   ```

   `answers.json` ist ein einfaches `{"<field-id>": "<antwort>"}`-Mapping (Feld-IDs
   stehen im Template als `id:`). Das Script gibt JSON mit `title_prefix`,
   `labels`, `body` und `warnings` zurück. Wenn `warnings` nicht leer ist, fehlt
   noch ein Pflichtfeld — vor dem Anlegen nachliefern.

5. **Vorschau zeigen und bestätigen lassen.** Zeige dem Nutzer den fertigen
   Titel (Prefix + eigener Teil, z. B. `[Story] Unterversicherungs-Warnung`),
   die Labels und den Body kurz an und warte auf ein klares Go, bevor das Issue
   tatsächlich angelegt wird — ein Issue ist öffentlich sichtbarer Inhalt, das
   wird nicht ungefragt veröffentlicht. Kleine Korrekturwünsche direkt einbauen.

6. **Issue anlegen:**

   ```bash
   gh issue create --repo krll-dev/janus \
     --title "<title_prefix><eigener Titel>" \
     --body-file <pfad-zur-body-datei> \
     --label "<label1>" --label "<label2>"
   ```

   `--body-file` verwenden (nicht `--body` mit Inline-String), damit Zeilenumbrüche
   und Sonderzeichen im Markdown-Body nicht kaputtgehen. Labels kommen 1:1 aus dem
   `labels`-Feld des Template-Outputs.

7. **Ergebnis melden.** Gib dem Nutzer die zurückgegebene Issue-URL. Erwähne
   kurz, dass die Custom Fields (Priority, Module, Type) auf dem Project-Board
   noch manuell gesetzt werden müssen (siehe
   [docs/adr/0002-github-board.md](../../../docs/adr/0002-github-board.md)) —
   das automatisiert dieser Skill nicht.

## Hinweise

- Voraussetzung ist ein eingeloggtes `gh` (`gh auth status`). Wenn nicht
  eingeloggt, den Nutzer darauf hinweisen statt selbst einen Login-Flow zu
  starten.
- Dieser Skill ist bewusst an die vier bestehenden Templates dieses Repos
  gebunden. Ändert sich ein Template oder kommt ein neues hinzu, reicht es,
  Schritt 1–2 entsprechend anzupassen — das Build-Script liest das YAML
  ohnehin dynamisch.

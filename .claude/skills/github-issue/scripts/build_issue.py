#!/usr/bin/env python3
"""
Baut Titel, Labels und Markdown-Body für ein GitHub-Issue aus einem
GitHub-Issue-Form-Template (.github/ISSUE_TEMPLATE/*.yml) und den dazu
gesammelten Antworten.

Nutzung:
    python3 build_issue.py <template.yml> <answers.json>

answers.json: {"<field-id>": "<antwort>", ...}
  - Fehlt ein Feld oder ist der Wert leer/None, wird der Abschnitt im Body
    weggelassen (außer bei required Feldern, da wird eine Warnung ausgegeben).
  - Für "dropdown"-Felder den gewählten Options-Text als String übergeben.
  - Für "checkboxes"-Felder eine Liste der angehakten Options-Labels übergeben.

Ausgabe (JSON auf stdout):
    {"title_prefix": "...", "labels": [...], "body": "...", "warnings": [...]}
"""
import json
import sys

import yaml


def build(template_path: str, answers: dict) -> dict:
    with open(template_path, encoding="utf-8") as f:
        template = yaml.safe_load(f)

    title_prefix = template.get("title", "")
    labels = template.get("labels", []) or []
    warnings = []
    body_parts = []

    for item in template.get("body", []):
        item_type = item.get("type")
        if item_type == "markdown":
            continue  # nur Hinweistext im Formular, gehört nicht ins Issue

        field_id = item.get("id")
        attrs = item.get("attributes", {})
        label = attrs.get("label", field_id)
        required = item.get("validations", {}).get("required", False)
        value = answers.get(field_id)

        if item_type == "checkboxes":
            options = attrs.get("options", [])
            checked = set(value or [])
            lines = [
                f"- [{'x' if opt.get('label') in checked else ' '}] {opt.get('label')}"
                for opt in options
            ]
            value_text = "\n".join(lines)
        else:
            value_text = (value or "").strip() if value else ""

        if not value_text:
            if required:
                warnings.append(f"Pflichtfeld '{label}' (id={field_id}) ist leer.")
            continue

        body_parts.append(f"## {label}\n\n{value_text}")

    return {
        "title_prefix": title_prefix,
        "labels": labels,
        "body": "\n\n".join(body_parts),
        "warnings": warnings,
    }


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    template_file, answers_file = sys.argv[1], sys.argv[2]
    with open(answers_file, encoding="utf-8") as f:
        answers_data = json.load(f)

    result = build(template_file, answers_data)
    print(json.dumps(result, ensure_ascii=False, indent=2))

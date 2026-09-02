#!/usr/bin/env python3
"""Render a Literature Scout email from JSON using the persistent HTML template."""

import argparse
import html
import json
from pathlib import Path


REQUIRED_TOP_LEVEL = (
    "subject", "preheader", "date_line", "run_summary", "sources_searched",
    "findings", "coverage", "deduplication", "limitations", "review_note",
)
REQUIRED_FINDING = (
    "title", "creator", "date", "type", "material_examined", "summary",
    "manifesto_connection", "potential_value", "caveats", "priority",
)


def escaped(value):
    if isinstance(value, list):
        value = "; ".join(str(item) for item in value)
    return html.escape(str(value), quote=True)


def replace_tokens(text, values):
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def validate(data):
    missing = [key for key in REQUIRED_TOP_LEVEL if key not in data]
    if missing:
        raise ValueError("Missing top-level fields: " + ", ".join(missing))
    for number, finding in enumerate(data["findings"], start=1):
        absent = [key for key in REQUIRED_FINDING if key not in finding]
        if absent:
            raise ValueError(f"Finding {number} is missing: " + ", ".join(absent))
        if not finding.get("url") and not finding.get("identifier"):
            raise ValueError(f"Finding {number} requires url or identifier")


def source_link(finding):
    label = finding.get("identifier") or "Open source"
    if finding.get("url"):
        return (
            '<div style="margin-top:12px;"><a href="'
            + escaped(finding["url"])
            + '" style="display:inline-block;background:#2f6fed;color:#ffffff;'
              'text-decoration:none;font-size:13px;font-weight:700;padding:9px 14px;'
              'border-radius:7px;">'
            + escaped(label)
            + "</a></div>"
        )
    return '<div style="margin-top:10px;font-size:13px;color:#486581;">' + escaped(label) + "</div>"


def render(template, data):
    validate(data)
    start_marker = "<!-- BEGIN FINDING -->"
    end_marker = "<!-- END FINDING -->"
    before, remainder = template.split(start_marker, 1)
    finding_template, after = remainder.split(end_marker, 1)

    cards = []
    for number, finding in enumerate(data["findings"], start=1):
        byline_parts = [finding["creator"], finding["date"], finding["type"]]
        values = {
            "NUMBER": str(number),
            "PRIORITY": escaped(finding["priority"]),
            "FINDING_TITLE": escaped(finding["title"]),
            "BYLINE": " · ".join(escaped(part) for part in byline_parts),
            "SOURCE_LINK": source_link(finding),
            "MATERIAL_EXAMINED": escaped(finding["material_examined"]),
            "FINDING_SUMMARY": escaped(finding["summary"]),
            "MANIFESTO_CONNECTION": escaped(finding["manifesto_connection"]),
            "POTENTIAL_VALUE": escaped(finding["potential_value"]),
            "CAVEATS": escaped(finding["caveats"]),
        }
        cards.append(replace_tokens(finding_template, values))

    inaccessible = data.get("inaccessible_sources", [])
    inaccessible_html = ""
    if inaccessible:
        inaccessible_html = (
            '<div style="margin-top:8px;font-size:13px;line-height:20px;color:#9b2c2c;">'
            "<strong>Inaccessible:</strong> " + escaped(inaccessible) + "</div>"
        )

    empty_findings = ""
    if not cards:
        empty_findings = (
            '<tr><td style="background:#ffffff;padding:12px 32px;">'
            '<div style="border:1px solid #d9e2ec;border-radius:10px;padding:18px;'
            'font-size:14px;line-height:22px;color:#486581;">'
            "No candidates met the configured threshold in this run.</div></td></tr>"
        )

    page = before + "".join(cards) + after
    return replace_tokens(page, {
        "SUBJECT": escaped(data["subject"]),
        "PREHEADER": escaped(data["preheader"]),
        "DATE_LINE": escaped(data["date_line"]),
        "RUN_SUMMARY": escaped(data["run_summary"]),
        "SOURCES_SEARCHED": escaped(data["sources_searched"]),
        "INACCESSIBLE_SOURCES": inaccessible_html,
        "EMPTY_FINDINGS": empty_findings,
        "COVERAGE": escaped(data["coverage"]),
        "DEDUPLICATION": escaped(data["deduplication"]),
        "LIMITATIONS": escaped(data["limitations"]),
        "REVIEW_NOTE": escaped(data["review_note"]),
    })


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, type=Path)
    parser.add_argument("--template", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    data = json.loads(args.data.read_text(encoding="utf-8"))
    template = args.template.read_text(encoding="utf-8")
    result = render(template, data)
    if "{{" in result or "}}" in result:
        raise ValueError("Unresolved template token remains in rendered output")
    args.output.write_text(result, encoding="utf-8")


if __name__ == "__main__":
    main()

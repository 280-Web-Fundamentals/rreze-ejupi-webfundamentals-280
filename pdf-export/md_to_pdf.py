#!/usr/bin/env python3
"""
Convert a jCoders lesson-guide Markdown file (Ora-N-Topic-Udhezues.md) into a
styled PDF, matching the "Rifreskim i Bazave te JavaScript" reference guide:
a cover block (eyebrow label / title / subtitle / rule) on page 1, numbered
section headings with a thin underline, dark rounded code blocks, pill-style
inline code, tip/warning callouts, and a centered page-number footer.

The cover title drops the internal "Aktiviteti <n>" activity reference
entirely and shows only "Ora <N> — <Topic>" (the class-hour number, taken
from the file/folder name) — these files are student-facing, so nothing
about the curriculum's internal activity numbering, Drive, or how the file
was produced belongs on the page.

Usage:
    python3 md_to_pdf.py <input.md> <output.pdf> [--eyebrow "JCODERS — WEB FUNDAMENTALS"]
"""
import argparse
import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

HERE = Path(__file__).parent
CSS_PATH = HERE / "style.css"

WARNING_PREFIX_RE = re.compile(r"^>\s*⚠️\s*\*\*Shënim:?\*\*", re.MULTILINE)


def split_source(md_text: str):
    """Pull the two-line cover header (and an optional leading warning
    blockquote) off the top of the file; return (warning_md, title, subtitle,
    remaining_md)."""
    lines = md_text.splitlines()
    i = 0

    # Optional leading "> ⚠️ **Shënim:** ..." blockquote (may wrap several lines)
    warning_lines = []
    while i < len(lines) and lines[i].startswith(">"):
        warning_lines.append(lines[i])
        i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1

    if i >= len(lines) or not lines[i].startswith("# "):
        raise ValueError("Expected a top-level '# Aktiviteti ...' heading near the top of the file")
    title = lines[i][2:].strip()
    i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1

    subtitle = ""
    if i < len(lines) and lines[i].startswith("## "):
        subtitle = lines[i][3:].strip()
        i += 1

    remainder = "\n".join(lines[i:])
    # Drop a leading '---' right after the header, the cover rule already
    # draws that divider.
    remainder = re.sub(r"^\s*\n?-{3,}\s*\n", "", remainder, count=1)

    warning_md = "\n".join(warning_lines)
    return warning_md, title, subtitle, remainder


ORA_NUMBER_RE = re.compile(r"Ora-(\d+)", re.IGNORECASE)


def extract_ora_number(input_path: Path) -> str:
    """Pull the lesson-hour number out of the file/folder name (e.g.
    'Ora-7-CSS-Udhezues.md' or its parent 'Ora-7-CSS' folder -> '7')."""
    for part in (input_path.stem, input_path.parent.name):
        m = ORA_NUMBER_RE.search(part)
        if m:
            return m.group(1)
    return ""


def cover_title(original_title: str, ora_number: str) -> str:
    """Build the cover title as 'Ora <N> — <Topic>', dropping the
    'Aktiviteti <n>' activity reference entirely -- students track lessons
    by class hour (Ora), not by the internal curriculum activity number."""
    topic = original_title.split("—", 1)[-1].strip() if "—" in original_title else original_title
    if ora_number:
        return f"Ora {ora_number} — {topic}"
    return topic


def render_markdown(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists"],
        output_format="html5",
    )


EMOJI_TIP = "\U0001F4A1"  # 💡
EMOJI_WARN = "⚠️"  # ⚠️


def tag_callouts(html: str) -> str:
    """Give <blockquote> elements a .tip / .warn class based on their
    leading emoji, so the CSS can style them as colored callouts."""

    def repl(m):
        block = m.group(0)
        inner_start = m.start(0)
        first_p = re.search(r"<p>(.*?)</p>", block, re.DOTALL)
        cls = ""
        if first_p:
            text = first_p.group(1)
            if text.strip().startswith(EMOJI_TIP):
                cls = " class=\"tip\""
            elif text.strip().startswith(EMOJI_WARN):
                cls = " class=\"warn\""
        return f"<blockquote{cls}>" + block[len("<blockquote>"):]

    return re.sub(r"<blockquote>.*?</blockquote>", repl, html, flags=re.DOTALL)


def build_html(warning_md: str, title: str, subtitle: str, body_md: str, eyebrow: str) -> str:
    cover = f"""
    <div class="cover">
      <p class="eyebrow">{eyebrow}</p>
      <h1>{title}</h1>
      {f'<p class="subtitle">{subtitle}</p>' if subtitle else ''}
      <hr class="cover-rule">
    </div>
    """

    warning_html = ""
    if warning_md.strip():
        warning_html = tag_callouts(render_markdown(warning_md))

    body_html = tag_callouts(render_markdown(body_md))

    return f"""<!DOCTYPE html>
<html lang="sq">
<head>
<meta charset="utf-8">
<title>{title}</title>
</head>
<body>
{cover}
{warning_html}
{body_html}
</body>
</html>
"""


def convert(input_path: Path, output_path: Path, eyebrow: str):
    md_text = input_path.read_text(encoding="utf-8")
    warning_md, title, subtitle, body_md = split_source(md_text)
    ora_number = extract_ora_number(input_path)
    title = cover_title(title, ora_number)
    html_doc = build_html(warning_md, title, subtitle, body_md, eyebrow)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html_doc, base_url=str(HERE)).write_pdf(
        str(output_path), stylesheets=[str(CSS_PATH)]
    )
    print(f"wrote {output_path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", type=Path, help="source .md file")
    ap.add_argument("output", type=Path, help="destination .pdf file")
    ap.add_argument(
        "--eyebrow",
        default="JCODERS — WEB FUNDAMENTALS",
        help="small caps label shown above the title on the cover",
    )
    args = ap.parse_args()
    convert(args.input, args.output, args.eyebrow)


if __name__ == "__main__":
    sys.exit(main())

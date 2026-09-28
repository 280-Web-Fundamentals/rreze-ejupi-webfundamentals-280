# PDF export for lesson guides

Converts an `Ora-N-Topic-Udhezues.md` file into a styled PDF, matching the
look of the reference guide Rreze shared ("Rifreskim i Bazave të JavaScript"):
a cover block on page 1 (eyebrow label / title / subtitle / rule), numbered
`##` sections with a thin underline, dark rounded code blocks, pill-style
inline code, colored tip/warning callouts (from `> 💡` / `> ⚠️` blockquotes),
and a centered page-number footer.

**Font:** Poppins throughout (headings and body); code blocks use DejaVu Sans
Mono. Poppins is a Google Font — its `.ttf` files need to be present on
whichever machine renders the PDF (already available in the Claude cloud
session used to generate these).

**Page margins:** page 1 uses a tighter top margin since the cover block
already carries visual weight; every page after it uses a wider top *and*
bottom margin so continuation pages open and close with real empty space
instead of feeling cramped. This is the `@page` / `@page :first` split in
`style.css`.

## Requirements

Python 3 with `weasyprint` and `markdown`:

```
pip install weasyprint markdown --break-system-packages
```

This only runs where those packages (and the Poppins font) are installed —
in practice, Claude runs it inside its own cloud session when asked to
export a lesson to PDF, not on Rreze's machine directly.

## Usage

```
python3 md_to_pdf.py "Ora-7-CSS/Ora-7-CSS-Udhezues.md" "Ora-7-CSS/Ora-7-CSS-Udhezues.pdf"
```

Optional `--eyebrow "JCODERS — WEB FUNDAMENTALS"` overrides the small caps
label shown above the title (this is the default for this repo).

## Notes for future lessons

- The script expects the file's first two lines to be exactly
  `# Aktiviteti <n> — <Topic>` and `## Udhëzues`, per the group's normal
  Udhezues format — it turns those into the cover block automatically.
- **The cover title never shows the activity number.** It strips
  `Aktiviteti <n> — ` off the first line and keeps only the topic, then
  prefixes it with `Ora <N>` (the class-hour number, read from the
  `Ora-<N>-Topic` file/folder name) — e.g. `# Aktiviteti 10 — Njoftimi me
  CSS` in `Ora-7-CSS-Udhezues.md` becomes the cover title `Ora 7 — Njoftimi
  me CSS`. Students track lessons by class hour, not by the curriculum's
  internal activity numbering.
- **These files are student-facing and must never mention Drive, slide
  decks, or how the file was produced.** A lesson reconstructed from a
  missing/unreadable source deck gets flagged to Rreze in conversation (and
  in this repo's `LESSON-PLAN-WORKFLOW.md`, which is gitignored) — never as
  a note inside the `.md` itself. The script will still pick up and render
  a leading `> ⚠️ **Shënim:** ...` blockquote as a callout if one exists
  (for legitimate content warnings), but this must not be used for
  production/sourcing notes going forward.
- If the style needs to change (colors, font sizes, margins), edit
  `style.css` — the script itself shouldn't need touching for style tweaks.

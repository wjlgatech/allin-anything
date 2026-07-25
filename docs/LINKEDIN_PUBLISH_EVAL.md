# LinkedIn Article Pre-Publish Eval — allin-anything
## Run this BEFORE clicking Publish. Every item is a hard gate.

---

### GATE 1 — COVER IMAGE
- [ ] Thumbnail uploaded via "Upload from computer"
  - Requires: computer-use access to Chrome (request FIRST, before writing content)
  - If computer-use denied → STOP. Do not publish without cover image.

### GATE 2 — IN-BODY IMAGES
- [ ] Infographic or diagram embedded at correct section break (if applicable)
  - Verify: screenshot showing image rendered inside the article

### GATE 3 — SPACING
- [ ] Screenshot the rendered article BEFORE publishing
- [ ] Paragraphs are tight (single line gap, not double/triple)
- [ ] If off → run `prepForLinkedIn()` from LINKEDIN_POSTING_GUIDE.md and re-inject

### GATE 4 — CONTENT COMPLETENESS
- [ ] Title matches intended title
- [ ] All sections present (verify via `get_page_text`)
- [ ] CTA present at bottom
- [ ] Hashtags present and relevant to allin-anything audience

### GATE 5 — PUBLISH FLOW
- [ ] Click "Next" → publish dialog appears
- [ ] Teaser text added in "Tell your network..." field
- [ ] Screenshot publish dialog to confirm card preview
- [ ] Click "Publish" only after all above are ✓

### GATE 6 — POST-PUBLISH VERIFY
- [ ] Screenshot the live article
- [ ] Thumbnail visible, spacing correct, images embedded
- [ ] URL captured and saved to `docs/ARTICLE_LOG.md`

---

## Root Cause Log

| Date | Issue | Root Cause | Fix |
|------|-------|------------|-----|
| Apr 7, 2026 | Excess spacing | `<p>` HTML injection adds margins in ProseMirror | `insertText` with `\n` |
| Apr 7, 2026 | No thumbnail | Chrome extension can't reach native file picker | Request computer-use before editor |

---

## The Rule
**Computer-use access must be requested and granted BEFORE starting the article editor.**

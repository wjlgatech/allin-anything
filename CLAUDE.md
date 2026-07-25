# CLAUDE.md — allin-anything Workspace Rules
## Read this at the start of every session. These are hard rules, not suggestions.

---

## PUBLISH PROTOCOL — Full autonomous sequence for "publish the article"

When Paul says "publish the article" (or any variation), execute this sequence completely.
**No clarifying questions. No stopping unless a hard blocker is hit.**

### PHASE 1 — PRE-FLIGHT (do before touching any browser)

1. Re-read `docs/LINKEDIN_POSTING_GUIDE.md` — mandatory every time, no exceptions.

2. Find the article to publish:
   - Scan `content/articles/` for `.md` files
   - Pick the most recently modified file NOT already listed in `docs/ARTICLE_LOG.md`
   - **If zero unpublished articles found** → stop and tell Paul: "No unpublished article found in `content/articles/`. Drop your `.md` file there and say 'publish' again."
   - **If multiple unpublished** → pick the most recently modified; state which one you're publishing.

3. Confirm thumbnail exists:
   - Look for: `assets/thumbnails/{article-slug}-thumbnail.png` (or .jpg)
   - The slug = article filename without `.md`, lowercased, spaces → hyphens
   - **If missing** → stop and tell Paul: "Thumbnail not found. Drop `{slug}-thumbnail.png` into `assets/thumbnails/` and say 'publish' again."

4. Note infographic (optional but preferred):
   - Look for: `assets/infographics/{article-slug}-infographic.png`
   - If missing → proceed without it; skip Gate 2 in the eval.

5. Run `prepForLinkedIn()` preprocessing on the article content.

### PHASE 2 — BROWSER SETUP

6. Call `mcp__computer-use__request_access` with `["Google Chrome"]`.
   - Wait for Paul's approval — this is the ONLY action required of Paul.
   - If denied or timed out → stop. Tell Paul: "Computer-use access needed. Please approve and say 'publish' again."

7. Navigate to `linkedin.com` and confirm Paul is logged in.
   - Logged-in signal: profile photo visible in top-right nav.
   - **If not logged in** → stop. Tell Paul: "Please log in to LinkedIn and say 'publish' again."

8. Navigate to LinkedIn article editor:
   - New article: click "Write article" from home feed
   - Edit draft: navigate to `linkedin.com/article/edit/{draft-id}/` if draft ID is known

### PHASE 3 — CONTENT INJECTION

9. Paste article title into title field.

10. Inject article body using `prepForLinkedIn()` + DataTransfer method:
    ```javascript
    const editor = document.querySelector('[contenteditable="true"]');
    editor.focus();
    const dt = new DataTransfer();
    dt.setData('text/plain', processedText);
    editor.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
    ```
    Do NOT use `insertHTML` — causes double-spacing.

11. If article has code blocks: use Tiptap ProseMirror transaction API (see `docs/LINKEDIN_POSTING_GUIDE.md`).

### PHASE 4 — ASSETS

12. Upload thumbnail via "Upload from computer" — use computer-use file picker.
13. If infographic exists: embed at section break using image toolbar.

### PHASE 5 — EVAL

14. Take a screenshot of the rendered article.
15. Run all 6 gates in `docs/LINKEDIN_PUBLISH_EVAL.md`. All must pass before proceeding.
    - Gate 3 (spacing): apply empty-paragraph fix if wrong.
    - Do NOT click Publish until all gates are green.

### PHASE 6 — PUBLISH & LOG

16. Click "Next" → fill teaser text → screenshot publish dialog → click "Publish".
17. Capture published article URL.
18. Append to `docs/ARTICLE_LOG.md`.
19. Report: "✅ Published: [{title}]({URL})"

---

## CONTENT STRUCTURE

```
allin-anything/
├── CLAUDE.md
├── content/
│   └── articles/          ← drop .md files here before saying "publish"
├── assets/
│   ├── thumbnails/        ← {article-slug}-thumbnail.png
│   └── infographics/      ← {article-slug}-infographic.png (optional)
└── docs/
    ├── LINKEDIN_POSTING_GUIDE.md
    ├── LINKEDIN_PUBLISH_EVAL.md
    └── ARTICLE_LOG.md
```

**Naming convention:** `my-post.md` → `my-post-thumbnail.png`

---

## HARD RULES

### RULE 1: READ THE POSTING GUIDE FIRST
Before any LinkedIn work, read `docs/LINKEDIN_POSTING_GUIDE.md`. Every time.

### RULE 2: COMPUTER-USE BEFORE BROWSER
Call `mcp__computer-use__request_access` with `["Google Chrome"]` before opening any browser window.

### RULE 3: EVAL BEFORE PUBLISH
Run all 6 gates in `docs/LINKEDIN_PUBLISH_EVAL.md` before clicking Publish.

### RULE 4: CONTENT BRIEF BEFORE WRITING
Before drafting any new article:
1. Theme — which allin-anything pillar?
2. Proof — concrete story, metric, or moment?
3. Takeaway — what does the reader do differently?
4. CTA — what action next?

### RULE 5: LOG EVERY PUBLISHED ARTICLE
After every publish, update `docs/ARTICLE_LOG.md`. This is how Claude knows what's already published.

---

## ACTIVE VENTURE

**allin-anything** — All-in interaction with the digital and physical world — one super-repo composing the -anything/-os agent family
Landing page: https://agentic-portfolio-lovat.vercel.app
LinkedIn profile: linkedin.com/in/jialiang-wu
Content brand: love12xfuture (YouTube, LinkedIn newsletter)

Core content themes:
- Agentic super-repos
- Digital-physical interaction
- Build in public

Target audience: AI builders and physical-AI engineers

---

## SESSION PATTERN
Each article = BRIEF → BUILD (if technical) → WRITE (.md into content/articles/) → PUBLISH ("publish the article") → LOG (auto)

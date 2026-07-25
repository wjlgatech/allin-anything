# LinkedIn Article Posting Guide — Spacing Fix

## ⚠️ RECURRING BUG — Read before every session
This guide encodes hard-won fixes. The same bugs recur if this isn't read first.

---

## Root Cause: The Spacing Bug

LinkedIn's article editor treats every `\n` as a new paragraph block.
Markdown uses `\n\n` between paragraphs. When pasted: `\n\n` → two paragraph blocks → visible empty gap.

**Result:** Articles render like haiku on stilts.

---

## Prevention: Preprocess Before Pasting

```javascript
// Run BEFORE pasting into LinkedIn editor
function prepForLinkedIn(text) {
  return text
    .replace(/---+/g, '')           // Remove markdown hr lines
    .replace(/^#{1,6}\s+/gm, '')     // Strip ## headers (space after # required — preserves #hashtags)
    .replace(/\*\*(.*?)\*\*/g, '$1') // Strip **bold**
    .replace(/\*(.*?)\*/g, '$1')     // Strip *italic*
    .replace(/\n{3,}/g, '\n\n')     // Collapse 3+ blank lines → 2
    .replace(/\n\n/g, '\n')         // Collapse double blank lines → single
    .trim();
}
```

Paste using DataTransfer:
```javascript
const editor = document.querySelector('[contenteditable="true"]');
editor.focus();
const text = prepForLinkedIn(rawMarkdown);
const dt = new DataTransfer();
dt.setData('text/plain', text);
editor.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
```

---

## Code Block Fix — Tiptap ProseMirror API

LinkedIn uses Tiptap (ProseMirror). Insert code via transaction API, not individual `<pre>` elements.

```javascript
const tiptap = document.querySelector('[contenteditable="true"]').editor;
const { view } = tiptap;
const { state } = view;
const { schema, tr } = state;

const code = `line1\nline2\nline3`;
const codeNode = schema.nodes.codeBlock.create(null, schema.text(code));
tr.insert(insertPosition, codeNode);
view.dispatch(tr);
```

**Rules:**
- Insert in reverse position order for multiple blocks
- `\n` inside code, not `\n\n`
- ❌ Never `insertAdjacentElement` per line — one box per line = broken rendering

---

## Post-Publish Spacing Fix

```javascript
const editor = document.querySelector('[contenteditable="true"]');
const emptyPs = Array.from(editor.querySelectorAll('p')).filter(p => !p.textContent.trim());
emptyPs.forEach(p => p.remove());
editor.dispatchEvent(new Event('input', { bubbles: true }));
```
Then click **Update**.

---

## Article ID Lookup

Edit URL: `linkedin.com/article/edit/{numeric-id}/`
Find via: "Edit article" link on published article page.

## allin-anything Article IDs

| # | Title | Article ID | Published |
|---|-------|-----------|-----------|
| 1 |       |           |           |

# Phase 6 – Project Testing

## 1. Automated Tests
```bash
pip install -r requirements-test.txt
pip install -r ../05_Project_Development_Phase/requirements.txt
pytest -v
```
| File | What it checks |
|------|----------------|
| `tests/test_formatters.py` | Sanitising, term parsing, title/heading detection, HTML escaping, DOCX contents (logo, table, footer), PDF validity |
| `tests/test_routes.py` | `/`, `/health`, `POST /generate` success, validation errors (422), error mapping (500 / 502) – Gemini is faked, so no API key is needed |

## 2. Manual Test Cases (real Gemini)
Fill in **Actual result / Status** after running each case and attach screenshots in Phase 8.

| ID | Test | Input / Steps | Expected result | Actual result | Status |
|----|------|---------------|-----------------|---------------|--------|
| TC-01 | Freelance contract | *Freelance Work Contract*; *Jane Doe (Service Provider), TechNova Inc. (Client)*; terms from the doc; *April 15, 2025* | Structured contract with numbered sections | | |
| TC-02 | NDA | Freelancer + client, confidentiality terms | NDA with confidentiality, term, governing law | | |
| TC-03 | Lease | Landlord/tenant, address in terms | Lease with rent, deposit, duration clauses | | |
| TC-04 | Preview | After generation | Dark scrollable card, bold headings, no `##` | | |
| TC-05 | Edit | Open *Click to Edit Document*, change text, Ctrl+Enter | Preview and downloads show the edit | | |
| TC-06 | TXT download | Click *Download as .TXT* | Clean text file | | |
| TC-07 | DOCX download | Click *Download as .DOCX* | Logo, title, terms table, Times New Roman, footer | | |
| TC-08 | PDF download | Click *Download as .PDF* | Logo + footer on every page, bold headings | | |
| TC-09 | Empty fields | Submit with a blank Document Type | Warning, no request sent | | |
| TC-10 | Backend stopped | Stop uvicorn, click Generate | Message explaining how to start the backend | | |
| TC-11 | Missing API key | Remove `GEMINI_API_KEY` | Clear "API key is missing" error | | |
| TC-12 | Special characters | Terms with quotes, `&`, `<b>` | No broken layout or injected HTML | | |

## 3. Issues Found in the Original Version & Fixes
| # | Problem | Cause | Fix |
|---|---------|-------|-----|
| 1 | `404 model not found` | `gemini-1.5-pro` retired | Configurable model list with fallback |
| 2 | `ModuleNotFoundError: ai_core` in Streamlit | Streamlit only adds `frontend/` to `sys.path` | Project root added to `sys.path` in `app.py` |
| 3 | `## Heading` shown in documents | Markdown from the model | Prompt forbids markdown + `sanitize_text` |
| 4 | PDF crash / old API | `fpdf` (old) instead of `fpdf2`; cursor handling | `fpdf2` with explicit `new_x` / `new_y` |
| 5 | Edits lost on rerun | Streamlit drops state of widgets not rendered | Editor kept in an always-rendered expander |
| 6 | Unsafe HTML in preview | AI text rendered with `unsafe_allow_html` | Text is `html.escape`d first |
| 7 | Connection errors on Windows | `localhost` resolves to IPv6 first | Default `API_URL` is `127.0.0.1` |
| 8 | Huge `requirements.txt` | Full `pip freeze` (chromadb, etc.) | Minimal list of real dependencies |
| 9 | Crash when key missing | Generator created at import time | Lazy creation + clear 500 error |

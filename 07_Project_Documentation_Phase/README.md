# Phase 7 – Project Documentation

## 1. Overview
LegalEase generates editable, branded legal documents with Gemini. A Streamlit UI collects the inputs,
a FastAPI service calls Gemini, and formatter modules export TXT / DOCX / PDF.

## 2. Folder Structure (Phase 5)
```text
05_Project_Development_Phase/
├── ai_core/
│   ├── gemini_generator.py   # prompt + Gemini call (model fallback)
│   └── formatters.py         # sanitize, HTML preview, DOCX, PDF
├── legalEaseAPI/
│   ├── main.py               # FastAPI app
│   └── routes.py             # POST /generate
├── frontend/app.py           # Streamlit UI
├── Image/                    # Logo.png, inverseLogo.png
├── assets/fonts/             # DejaVu fonts (PDF)
├── config.py
├── requirements.txt
├── .env.example
├── run.bat / run.sh
```

## 3. Installation
```bash
cd 05_Project_Development_Phase
python -m venv venv
venv\Scripts\activate                 # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
copy .env.example .env                # then add GEMINI_API_KEY
```

## 4. Running
**One command:** `run.bat` (Windows) or `./run.sh` (macOS/Linux).

**Or two terminals (from `05_Project_Development_Phase`):**
```bash
uvicorn legalEaseAPI.main:app --reload          # backend  -> http://127.0.0.1:8000/docs
streamlit run frontend/app.py                   # frontend -> http://localhost:8501
```

## 5. Configuration (`.env`)
| Variable | Meaning | Default |
|----------|---------|---------|
| `GEMINI_API_KEY` | Google AI Studio key (required) | – |
| `GEMINI_MODELS` | Models tried in order | `gemini-3.1-pro-preview,gemini-2.5-pro,gemini-3-flash-preview,gemini-2.5-flash` |
| `API_URL` | Backend address used by the frontend | `http://127.0.0.1:8000` |

## 6. Usage Guide
1. **Document Type** – e.g. *Freelance Work Contract*, *NDA*, *Lease Agreement*.
2. **Parties Involved** – names and roles, e.g. *Jane Doe (Service Provider), TechNova Inc. (Client)*.
3. **Terms & Conditions** – separate clauses with semicolons, e.g.
   *Work delivered by May 15, 2025; Payment within 7 days of invoice*.
4. **Effective Date** – e.g. *April 15, 2025*.
5. Click **Generate Document**, review the preview, optionally open **Click to Edit Document**,
   then download **.TXT / .DOCX / .PDF**.

Missing details (addresses, amounts, jurisdiction) appear as `[placeholders]` – fill them in via the edit box.

## 7. API Reference
`POST /generate`
```json
{ "document_type": "NDA", "parties": "A (Disclosing), B (Receiving)",
  "terms": "Keep secrets; 2 year term", "dates": "April 15, 2025" }
```
Response `200`: `{ "document": "<generated text>" }` · Errors: `422` invalid input, `500` configuration, `502` AI failure.

## 8. Troubleshooting
| Symptom | Fix |
|---------|-----|
| `No module named ai_core` | Run commands from `05_Project_Development_Phase` |
| "Cannot reach the backend" | Start `uvicorn legalEaseAPI.main:app --reload` |
| "GEMINI_API_KEY is missing" | Create `.env` from `.env.example` and add the key |
| `404` / model not found | Update `GEMINI_MODELS` in `.env` |
| `429` quota exceeded | Wait, or put a Flash model first in `GEMINI_MODELS` |
| Edits not in the download | Press Ctrl+Enter in the edit box first |

## 9. Limitations & Future Work
Single user, no storage, English-oriented prompt. Planned: multilingual output, clause highlighting and
plain-language summaries, saved documents, cloud deployment.

## 10. Disclaimer
Generated documents are drafts for guidance and **are not legal advice**. Have a qualified lawyer review them
before use.

## 11. Conclusion
LegalEase shows how a Gemini model plus simple document tooling can make first drafts of common legal
documents fast and accessible, while keeping the user in control through editing and clear export formats.

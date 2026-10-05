# Phase 2 – Requirement Analysis

## 1. Functional Requirements
| ID | Requirement |
|----|-------------|
| FR-1 | User enters document type, parties, terms (semicolon-separated) and effective date |
| FR-2 | Backend endpoint `POST /generate` validates the input and returns the document text |
| FR-3 | Gemini drafts a formal document with numbered sections and placeholders for missing details |
| FR-4 | Document is shown in a styled, scrollable preview |
| FR-5 | User can edit the text before exporting |
| FR-6 | Export as **.TXT** |
| FR-7 | Export as **.DOCX** – logo, title, Times New Roman, terms table, footer |
| FR-8 | Export as **.PDF** – logo + title header and footer on every page, bold section headings, bullet terms |
| FR-9 | Clear error messages (backend offline, missing key, model failure, timeout) |

## 2. Non-Functional Requirements
| ID | Requirement |
|----|-------------|
| NFR-1 | API key kept in `.env`, never committed to Git |
| NFR-2 | AI text is HTML-escaped before it is shown in the preview (no script injection) |
| NFR-3 | Input length limits on the API to prevent abuse |
| NFR-4 | Model names configurable, with automatic fallback to the next model |
| NFR-5 | Runs locally on Windows / macOS / Linux; frontend and backend can be started with one script |

## 3. Software Requirements
| Item | Detail |
|------|--------|
| Python | 3.10+ |
| Backend | FastAPI, Uvicorn, Pydantic |
| Frontend | Streamlit, requests |
| AI | `google-genai` (Gemini) |
| Documents | `python-docx`, `fpdf2`, Pillow |
| Config | `python-dotenv` |

## 4. Hardware Requirements
Any modern laptop (4 GB RAM is enough – the AI runs in Google's cloud). Internet connection required.

## 5. External Requirements
A Gemini API key from Google AI Studio.

## 6. Constraints & Assumptions
- Single user, local deployment, no database or login.
- Output quality depends on the clarity of the user's inputs.
- Not a replacement for professional legal advice.

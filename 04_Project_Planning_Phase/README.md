# Phase 4 – Project Planning

## 1. Milestones
| Milestone | Activities | Deliverable |
|-----------|-----------|-------------|
| M1 – Model & architecture | Choose Gemini, define Streamlit + FastAPI architecture, set up environment | Architecture, venv, `.env` |
| M2 – Core functionality | Document generation, formatters (HTML / DOCX / PDF / TXT) | `ai_core/` modules |
| M3 – API logic | `main.py`, `routes.py`, `DocumentRequest`, error handling | Working `/generate` |
| M4 – Frontend | Streamlit form, preview, editing, downloads | `frontend/app.py` |
| M5 – Deployment & testing | Run locally, test all formats and inputs | Running app |
| M6 – Documentation & demo | Phase documents, screenshots, video | This repository |

## 2. Task Breakdown
| Task | Owner | Status |
|------|-------|--------|
| Select model, design prompt | [Name] | ✅ Done |
| Build backend | [Name] | ✅ Done |
| Build formatters | [Name] | ✅ Done |
| Build Streamlit UI | [Name] | ✅ Done |
| Testing & bug fixing | [Name] | ✅ Done |
| Documentation & GitHub upload | [Name] | 🔄 In progress |

## 3. Risks & Mitigation
| Risk | Impact | Mitigation |
|------|--------|-----------|
| Gemini model retired (404) | App fails | Model list in `.env` with fallback |
| API quota (429) | Generation fails | Fallback to a Flash model; clear error |
| Incorrect legal content | User harm | Disclaimer + editable output + lawyer review advice |
| Markdown symbols in output | Ugly documents | Prompt forbids markdown + `sanitize_text` |
| Backend not running | Frontend errors | Friendly connection error + `run.bat` / `run.sh` |
| API key leaked to GitHub | Security | `.env` in `.gitignore`, only `.env.example` committed |

## 4. Future Scope (Phase 4 backlog – not implemented yet)
Multiple languages, clause highlighting and plain-language summaries, user accounts and saved documents,
cloud deployment (Render / Railway for the API, Streamlit Community Cloud for the UI).

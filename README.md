# ⚖️ LegalEase – AI-Powered Legal Document Generator

LegalEase turns a few inputs (document type, parties, key terms, effective date) into a complete,
professionally structured legal draft using **Google Gemini**. Users can preview it, edit it, and download it
as **.TXT, .DOCX (logo, terms table, footer) or .PDF (logo header + footer on every page)**.

> ⚠️ AI-generated drafts are for guidance only and are **not legal advice**. Have a qualified lawyer review any
> document before it is signed.

## 📁 Project Phases

| # | Phase | Folder |
|---|-------|--------|
| 1 | Brainstorming & Ideation | [`01_Brainstorming_Ideation_Phase`](01_Brainstorming_Ideation_Phase) |
| 2 | Requirement Analysis | [`02_Requirement_Analysis_Phase`](02_Requirement_Analysis_Phase) |
| 3 | Project Design | [`03_Project_Design_Phase`](03_Project_Design_Phase) |
| 4 | Project Planning | [`04_Project_Planning_Phase`](04_Project_Planning_Phase) |
| 5 | Project Development (source code) | [`05_Project_Development_Phase`](05_Project_Development_Phase) |
| 6 | Project Testing | [`06_Project_Testing_Phase`](06_Project_Testing_Phase) |
| 7 | Project Documentation | [`07_Project_Documentation_Phase`](07_Project_Documentation_Phase) |
| 8 | Project Demonstration | [`08_Project_Demonstration_Phase`](08_Project_Demonstration_Phase) |

## ⚙️ Tech Stack
Streamlit (frontend) · FastAPI + Uvicorn (backend) · Google Gemini (`google-genai`) · python-docx · fpdf2

## 🚀 Quick Start
```bash
git clone https://github.com/<your-username>/LegalEase-AI-Legal-Document-Generator.git
cd LegalEase-AI-Legal-Document-Generator/05_Project_Development_Phase
python -m venv venv
venv\Scripts\activate            # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
copy .env.example .env           # macOS/Linux: cp .env.example .env  -> add your GEMINI_API_KEY
run.bat                          # macOS/Linux: ./run.sh   (starts backend + frontend)
```
Frontend: <http://localhost:8501> · Backend API docs: <http://127.0.0.1:8000/docs>

## 👥 Team
- [Your Name] – [Roll no. / Role]

> Built as part of the SmartBridge / SmartInternz program.

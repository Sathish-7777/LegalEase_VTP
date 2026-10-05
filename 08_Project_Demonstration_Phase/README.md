# Phase 8 – Project Demonstration

## 1. Demo Video
🎥 **Link:** _add your YouTube / Google Drive video link here_

## 2. Demo Script (about 3 minutes)
1. Explain the problem and idea (Phase 1) and show the architecture (Phase 3).
2. Start the app (`run.bat`), open <http://localhost:8501>.
3. Enter: **Freelance Work Contract** · **Jane Doe (Service Provider), TechNova Inc. (Client)** ·
   terms *Work must be delivered by May 15, 2025; Payment will be made within 7 days of invoice;
   The client retains intellectual property rights; Confidentiality must be maintained at all times* ·
   **April 15, 2025**.
4. Click **Generate Document** and show the preview.
5. Open **Click to Edit Document**, change a line, press Ctrl+Enter.
6. Download TXT, DOCX (show logo, terms table, footer) and PDF (logo + footer on every page).
7. Show `/docs` and call `POST /generate` directly.
8. Mention the disclaimer and the tests (Phase 6).

## 3. Screenshots
Save your screenshots in `screenshots/` with these names:

| Screen | File |
|--------|------|
| Home / empty form | `screenshots/01_home.png` |
| Filled form | `screenshots/02_form_filled.png` |
| Generated document | `screenshots/03_generated.png` |
| Editing | `screenshots/04_editing.png` |
| DOCX output | `screenshots/05_docx.png` |
| PDF output | `screenshots/06_pdf.png` |

![Home](screenshots/01_home.png)
![Generated](screenshots/03_generated.png)
![PDF](screenshots/06_pdf.png)

## 4. Sample Outputs
Put one generated `.txt`, `.docx` and `.pdf` in `sample_outputs/` (e.g. `freelance_work_contract.pdf`).

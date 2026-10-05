# Phase 1 – Brainstorming & Ideation

## 1. Problem Statement
Legal documents (contracts, NDAs, leases) are expensive to draft and hard to write without legal knowledge.
Free templates are rigid, full of blanks, and rarely match the user's real situation.

## 2. Idea
**LegalEase** asks for four simple inputs – document type, parties, key terms, effective date – and uses
Generative AI to draft a complete, structured legal document. The user previews it, edits the wording, and
downloads a branded **.TXT / .DOCX / .PDF**.

## 3. Target Users
| User | Example |
|------|---------|
| Startup founders | Employment contract for a new hire |
| Freelancers | NDA or work contract for a client |
| Landlords / tenants | Residential lease agreement |
| Small businesses | Service agreements, offer letters |

## 4. Ideas Considered
| Idea | Decision | Reason |
|------|----------|--------|
| Static template library | ❌ Rejected | Not tailored to the user's terms |
| Chatbot answering legal questions | ❌ Rejected | Different goal; higher risk of wrong advice |
| **Form-driven AI drafting + editable preview + multi-format export** | ✅ Selected | Personalised, fast, and gives a ready-to-use file |

## 5. Model Selection
**Google Gemini** (Pro-class model) – strong at long, formal, structured writing and following formatting
instructions. Model names are configurable because Google retires models regularly.

## 6. Unique Value
- Terms typed once appear as clauses **and** as a summary table / bullet list in the export.
- Editable before download – the user stays in control.
- Branding: logo, Times New Roman (DOCX), header/footer (PDF).

## 7. Responsible-Use Note
AI drafts can contain mistakes. The app shows a disclaimer: *drafts are not legal advice and should be
reviewed by a qualified lawyer before signing.*

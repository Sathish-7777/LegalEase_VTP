"""Streamlit frontend. Run from the project root:  streamlit run frontend/app.py"""
import sys
from pathlib import Path

# Streamlit puts only frontend/ on sys.path - add the project root so `config` and `ai_core` import
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import requests
import streamlit as st

from ai_core.formatters import (
    format_docx, format_html_preview, format_pdf, safe_filename, sanitize_text,
)
from config import API_URL, LOGO_INVERSE_PATH, REQUEST_TIMEOUT

st.set_page_config(page_title="LegalEase", layout="centered")

# ---- header ---------------------------------------------------------------
_, mid, _ = st.columns([1, 2, 1])
with mid:
    if LOGO_INVERSE_PATH.exists():
        st.image(str(LOGO_INVERSE_PATH), use_container_width=True)
st.markdown("<h2 style='text-align:center;'>AI Legal Document Generator</h2>", unsafe_allow_html=True)

# ---- input form -------------------------------------------------------------
with st.form("doc_form"):
    document_type = st.text_input("Document Type (Ex: Agreement, Contract, NDA)",
                                  placeholder="Freelance Work Contract")
    parties = st.text_area("Parties Involved",
                           placeholder="Jane Doe (Service Provider), TechNova Inc. (Client)")
    terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)",
                         placeholder="Work must be delivered by May 15, 2025; Payment within 7 days of invoice")
    dates = st.text_input("Effective Date", placeholder="April 15, 2025")
    submitted = st.form_submit_button("Generate Document")

if submitted:
    if not (document_type.strip() and parties.strip() and dates.strip()):
        st.warning("Please fill in Document Type, Parties Involved and Effective Date.")
    else:
        try:
            with st.spinner("Drafting your document..."):
                resp = requests.post(
                    f"{API_URL}/generate",
                    json={"document_type": document_type.strip(), "parties": parties.strip(),
                          "terms": terms.strip(), "dates": dates.strip()},
                    timeout=REQUEST_TIMEOUT,
                )
            if resp.ok:
                st.session_state["editor_text"] = sanitize_text(resp.json()["document"])
                st.session_state["doc_type"] = document_type.strip()
                st.session_state["terms"] = terms
                st.success("Document generated successfully!")
            else:
                try:
                    detail = resp.json().get("detail", resp.text)
                except ValueError:
                    detail = resp.text
                st.error(f"Backend error ({resp.status_code}): {detail}")
        except requests.exceptions.ConnectionError:
            st.error(f"Cannot reach the backend at {API_URL}. "
                     "Start it with:  uvicorn legalEaseAPI.main:app --reload")
        except requests.exceptions.Timeout:
            st.error("The request timed out. Please try again.")

# ---- preview / edit / download ------------------------------------------------
if st.session_state.get("editor_text"):
    doc_type = st.session_state.get("doc_type", "Legal Document")
    doc_terms = st.session_state.get("terms", "")
    current = st.session_state["editor_text"]          # always the latest (edited) text

    preview = format_html_preview(current, doc_type)    # HTML-escaped, safe to render
    st.markdown(
        "<div style='background:#10172a;color:#e6e9f2;padding:18px;border-radius:10px;"
        f"max-height:420px;overflow-y:auto;'>{preview}</div>",
        unsafe_allow_html=True,
    )

    with st.expander("✏️ Click to Edit Document"):
        st.text_area("Edit Document Below:", key="editor_text", height=320)
        st.caption("Press Ctrl+Enter to apply your changes.")

    st.download_button("📄 Download as .TXT", data=current.encode("utf-8"),
                       file_name=safe_filename(doc_type, "txt"), mime="text/plain")
    try:
        st.download_button("📝 Download as .DOCX", data=format_docx(current, doc_type, doc_terms),
                           file_name=safe_filename(doc_type, "docx"),
                           mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        st.download_button("📕 Download as .PDF", data=format_pdf(current, doc_type, doc_terms),
                           file_name=safe_filename(doc_type, "pdf"), mime="application/pdf")
    except Exception as exc:                            # never crash the page on export problems
        st.error(f"Could not build the DOCX/PDF file: {exc}")

    st.caption("⚖️ AI-generated drafts are for guidance only and are not legal advice. "
               "Have a qualified lawyer review any document before you sign it.")
else:
    st.info("Click 'Generate Document' to start")

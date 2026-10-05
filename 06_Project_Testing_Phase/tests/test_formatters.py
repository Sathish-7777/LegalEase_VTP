import io
import zipfile

import pytest

from ai_core import formatters as f

RAW = ('## Freelance Work Contract\n\nAgreement made \u201cthis\u201d 15th day of April, 2025\n\n'
       '**1. Services:**\nThe provider will work.\n\n2. Payment:\n* Paid in 7 days')


def test_sanitize_removes_markdown_and_smart_quotes():
    clean = f.sanitize_text(RAW)
    assert "#" not in clean and "**" not in clean and "\u201c" not in clean
    assert "- Paid in 7 days" in clean


def test_parse_terms_splits_on_semicolons_and_newlines():
    assert f.parse_terms("A; B ;\n C;;") == ["A", "B", "C"]
    assert f.parse_terms("") == []


def test_title_is_taken_from_first_line():
    title, _ = f.split_title(f.sanitize_text(RAW), "ignored")
    assert title == "Freelance Work Contract"


def test_title_falls_back_to_document_type():
    title, _ = f.split_title("1. Services: do the work.\nMore text here.", "nda")
    assert title == "Nda"


def test_headings_detected():
    assert f.is_heading("1. Services:") and not f.is_heading("The provider shall pay.")


def test_html_preview_escapes_html():
    html = f.format_html_preview("Title\n<script>alert(1)</script>")
    assert "<script>" not in html and "&lt;script&gt;" in html


def test_safe_filename():
    assert f.safe_filename("Freelance Work Contract!", "pdf") == "freelance_work_contract.pdf"
    assert f.safe_filename("", "txt") == "document.txt"


def test_docx_has_logo_table_footer_and_title():
    data = f.format_docx(f.sanitize_text(RAW), "Freelance Work Contract", "Pay in 7 days; Deliver by May 15")
    z = zipfile.ZipFile(io.BytesIO(data))
    xml = z.read("word/document.xml").decode()
    assert "<w:tbl>" in xml and "Freelance Work Contract" in xml
    assert any("media" in n for n in z.namelist())          # logo embedded
    assert any("footer" in n for n in z.namelist())


def test_pdf_is_valid():
    pytest.importorskip("fpdf")
    data = f.format_pdf(f.sanitize_text(RAW), "Freelance Work Contract", "Pay in 7 days")
    assert data[:4] == b"%PDF" and len(data) > 1000

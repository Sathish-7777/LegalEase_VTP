"""Central configuration: absolute paths + environment variables."""
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# --- Gemini -------------------------------------------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODELS = [
    m.strip()
    for m in os.getenv(
        "GEMINI_MODELS",
        "gemini-3.1-pro-preview,gemini-2.5-pro,gemini-3-flash-preview,gemini-2.5-flash",
    ).split(",")
    if m.strip()
]

# --- Frontend -> backend ---------------------------------------------------
# 127.0.0.1 (not "localhost") avoids slow IPv6 lookups on Windows
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000").rstrip("/")
REQUEST_TIMEOUT = 180          # seconds; long legal documents take a while

# --- Branding / assets -------------------------------------------------------
LOGO_PATH = BASE_DIR / "Image" / "Logo.png"                  # dark logo (Word / PDF)
LOGO_INVERSE_PATH = BASE_DIR / "Image" / "inverseLogo.png"   # white logo (dark web UI)
FONT_REGULAR = BASE_DIR / "assets" / "fonts" / "DejaVuSans.ttf"
FONT_BOLD = BASE_DIR / "assets" / "fonts" / "DejaVuSans-Bold.ttf"
FOOTER_TEXT = "LegalEase Inc. | contact@legalease.com | All Rights Reserved."

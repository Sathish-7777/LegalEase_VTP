"""Gemini integration: builds the prompt and returns the legal document text."""
from google import genai
from google.genai import types

from config import GEMINI_API_KEY, GEMINI_MODELS


class ConfigError(RuntimeError):
    """Missing / invalid configuration (e.g. no API key)."""


class GenerationError(RuntimeError):
    """Gemini could not produce a document."""


class GeminiDocumentGenerator:
    def __init__(self, models: list[str] | None = None):
        self.models = models or GEMINI_MODELS
        self._client = None

    def _get_client(self) -> "genai.Client":
        if not GEMINI_API_KEY:
            raise ConfigError(
                "GEMINI_API_KEY is missing. Copy .env.example to .env and add your key."
            )
        if self._client is None:
            self._client = genai.Client(api_key=GEMINI_API_KEY)
        return self._client

    @staticmethod
    def build_prompt(document_type: str, parties: str, terms: str, dates: str) -> str:
        return f"""You are an experienced legal drafter. Draft a complete, professional
"{document_type}" using ONLY the details below.

PARTIES: {parties}
EFFECTIVE DATE: {dates}
KEY TERMS (separated by semicolons; each one must appear as a clear clause):
{terms or "None provided - use standard, balanced clauses."}

FORMAT RULES (important):
- Plain text only. Do NOT use markdown: no #, no **, no bullet symbols like *.
- Line 1: the document title only.
- Then an opening paragraph naming the parties and the effective date.
- Number every section as "1. Heading:" on its own line, followed by its paragraph(s).
- Include standard sections for this document type (e.g. definitions, term and
  termination, confidentiality, liability, governing law, entire agreement,
  severability) and one clause for every key term above.
- Where a detail is missing (addresses, amounts, jurisdiction), write a clear
  placeholder in [square brackets]. Never invent names, amounts or addresses.
- End with a signature block for each party (name line, signature line, date line).
"""

    def generate_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        client = self._get_client()
        prompt = self.build_prompt(document_type, parties, terms, dates)
        config = types.GenerateContentConfig(temperature=0.4)

        errors = []
        for model in self.models:
            try:
                response = client.models.generate_content(
                    model=model, contents=prompt, config=config
                )
                text = (response.text or "").strip()
                if text:
                    return text
                errors.append(f"{model}: empty response (possibly blocked by safety filters)")
            except Exception as exc:       # 404 retired model, 429 quota, network ...
                errors.append(f"{model}: {exc}")
        raise GenerationError("All Gemini models failed:\n" + "\n".join(errors))

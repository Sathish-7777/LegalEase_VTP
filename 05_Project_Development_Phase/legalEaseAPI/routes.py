"""API routes. Plain `def` so FastAPI runs the blocking Gemini call in a thread pool."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ai_core.gemini_generator import ConfigError, GeminiDocumentGenerator, GenerationError

router = APIRouter()
_generator: GeminiDocumentGenerator | None = None


def get_generator() -> GeminiDocumentGenerator:
    """Created lazily so the server can start (and show a clear error) without an API key."""
    global _generator
    if _generator is None:
        _generator = GeminiDocumentGenerator()
    return _generator


class DocumentRequest(BaseModel):
    document_type: str = Field(..., min_length=2, max_length=100)
    parties: str = Field(..., min_length=2, max_length=1000)
    terms: str = Field("", max_length=5000)
    dates: str = Field(..., min_length=2, max_length=100)


@router.post("/generate")
def generate_legal_document(request: DocumentRequest):
    try:
        document = get_generator().generate_document(
            request.document_type, request.parties, request.terms, request.dates
        )
    except ConfigError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    except GenerationError as exc:
        raise HTTPException(status_code=502, detail=str(exc))
    return {"document": document}

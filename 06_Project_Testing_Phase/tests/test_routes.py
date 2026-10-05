"""Backend tests with a fake Gemini generator - no API key or internet needed."""
import pytest
from fastapi.testclient import TestClient

from ai_core.gemini_generator import ConfigError, GenerationError
from legalEaseAPI import routes
from legalEaseAPI.main import app

client = TestClient(app)
PAYLOAD = {"document_type": "NDA", "parties": "A (Disclosing), B (Receiving)",
           "terms": "Keep secrets; 2 year term", "dates": "April 15, 2025"}


class FakeGenerator:
    def generate_document(self, *args):
        return "Non-Disclosure Agreement\n\n1. Purpose:\nText."


def test_root_and_health():
    assert "Welcome" in client.get("/").json()["message"]
    assert client.get("/health").json() == {"status": "ok"}


def test_generate_returns_document(monkeypatch):
    monkeypatch.setattr(routes, "get_generator", lambda: FakeGenerator())
    r = client.post("/generate", json=PAYLOAD)
    assert r.status_code == 200 and r.json()["document"].startswith("Non-Disclosure")


def test_missing_field_is_422():
    assert client.post("/generate", json={"document_type": "NDA"}).status_code == 422


def test_too_short_field_is_422():
    assert client.post("/generate", json={**PAYLOAD, "parties": ""}).status_code == 422


@pytest.mark.parametrize("error, code", [(ConfigError("no key"), 500), (GenerationError("failed"), 502)])
def test_errors_are_mapped(monkeypatch, error, code):
    class Boom:
        def generate_document(self, *a):
            raise error
    monkeypatch.setattr(routes, "get_generator", lambda: Boom())
    r = client.post("/generate", json=PAYLOAD)
    assert r.status_code == code and str(error) in r.json()["detail"]

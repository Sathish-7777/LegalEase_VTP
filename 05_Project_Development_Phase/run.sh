#!/usr/bin/env bash
# Starts the FastAPI backend (port 8000) and the Streamlit frontend (port 8501)
cd "$(dirname "$0")"
uvicorn legalEaseAPI.main:app --reload --port 8000 &
BACKEND=$!
trap 'kill $BACKEND' EXIT
streamlit run frontend/app.py

@echo off
REM Starts the FastAPI backend in a new window, then the Streamlit frontend
cd /d "%~dp0"
start "LegalEase API" cmd /k uvicorn legalEaseAPI.main:app --reload --port 8000
streamlit run frontend/app.py

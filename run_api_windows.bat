@echo off
call .venv\Scripts\activate
uvicorn app.api.routes:api --reload
pause

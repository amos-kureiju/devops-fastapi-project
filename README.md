DevSecOps FastAPI Demo

REST API sederhana menggunakan FastAPI dengan endpoint /health dan /metrics untuk pipeline CI/CD DevOps.

Menjalankan proyek secara lokal:
1. pip install -r requirements.txt
2. python -m pytest -v
3. uvicorn app.main:app --reload
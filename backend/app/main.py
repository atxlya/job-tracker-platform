from fastapi import FastAPI

from app.api.routes.company import router as company_router
from app.db.init_db import init_db

app = FastAPI(title="Job Tracker API")

app.include_router(company_router)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
from fastapi import FastAPI

app = FastAPI(title="Job Tracker API")


@app.get("/")
def root():
    return {
        "message": "Job Tracker API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
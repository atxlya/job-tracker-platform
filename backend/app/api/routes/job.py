from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.job import Job
from app.schemas.job import (
    JobCreate,
    JobUpdate,
    JobResponse,
)

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = Job(**job.model_dump())

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job


@router.get("/", response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()


@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.get(Job, job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return job


@router.patch("/{job_id}", response_model=JobResponse)
def update_job(
    job_id: int,
    job_data: JobUpdate,
    db: Session = Depends(get_db),
):
    job = db.get(Job, job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    job.title = job_data.title
    job.location = job_data.location
    job.category = job_data.category
    job.employment_type = job_data.employment_type
    job.url = job_data.url
    job.status = job_data.status
    job.enabled = job_data.enabled

    db.commit()
    db.refresh(job)

    return job


@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.get(Job, job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    db.delete(job)
    db.commit()

    return {"message": "Job deleted successfully"}
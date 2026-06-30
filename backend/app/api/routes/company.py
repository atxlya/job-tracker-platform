from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.db.session import get_db
from app.models.company import Company
from app.schemas.company import (
    CompanyCreate,
    CompanyUpdate,
    CompanyResponse,
)

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.post("/", response_model=CompanyResponse)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company(
        name=company.name,
        career_url=company.career_url,
    )

    try:
        db.add(db_company)
        db.commit()
        db.refresh(db_company)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Company already exists",
        )

    return db_company


@router.get("/", response_model=list[CompanyResponse])
def get_companies(db: Session = Depends(get_db)):
    return db.query(Company).all()


@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(company_id: int, db: Session = Depends(get_db)):
    company = db.get(Company, company_id)

    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    return company


@router.patch("/{company_id}", response_model=CompanyResponse)
def update_company(
    company_id: int,
    company_data: CompanyUpdate,
    db: Session = Depends(get_db),
):
    company = db.get(Company, company_id)

    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    company.name = company_data.name
    company.career_url = company_data.career_url
    company.enabled = company_data.enabled

    db.commit()
    db.refresh(company)

    return company


@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    company = db.get(Company, company_id)

    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    db.delete(company)
    db.commit()

    return {"message": "Company deleted successfully"}
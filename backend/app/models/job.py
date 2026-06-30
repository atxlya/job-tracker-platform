from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    title = Column(String, nullable=False)

    location = Column(String)

    url = Column(String, unique=True)

    status = Column(String, default="NEW")

    company = relationship("Company")
    
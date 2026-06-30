from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(String(255))
    location: Mapped[str] = mapped_column(String(255))
    category: Mapped[str] = mapped_column(String(100))
    employment_type: Mapped[str] = mapped_column(String(100))

    url: Mapped[str] = mapped_column(String(500), unique=True)

    status: Mapped[str] = mapped_column(
        String(50),
        default="NEW",
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )
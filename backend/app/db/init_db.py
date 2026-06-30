from app.db.database import Base, engine

# Import all models here
from app.models.company import Company
from app.models.job import Job


def init_db():
    Base.metadata.create_all(bind=engine)
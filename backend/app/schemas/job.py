from pydantic import BaseModel


class JobCreate(BaseModel):
    company_id: int
    title: str
    location: str
    category: str
    employment_type: str
    url: str


class JobUpdate(BaseModel):
    title: str
    location: str
    category: str
    employment_type: str
    url: str
    status: str
    enabled: bool


class JobResponse(BaseModel):
    id: int
    company_id: int
    title: str
    location: str
    category: str
    employment_type: str
    url: str
    status: str
    enabled: bool

    model_config = {
        "from_attributes": True
    }
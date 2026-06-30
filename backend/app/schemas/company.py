from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    career_url: str


class CompanyUpdate(BaseModel):
    name: str
    career_url: str
    enabled: bool


class CompanyResponse(BaseModel):
    id: int
    name: str
    career_url: str
    enabled: bool

    model_config = {
        "from_attributes": True
    }
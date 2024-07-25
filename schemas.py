from pydantic import BaseModel, Field


class DeviceModel(BaseModel):
    name: str = Field(..., min_length=3)
    type: str
    login: str
    password: str = Field(..., min_length=8)
    location_id: int = None  # Foreign key reference
    api_user_id: int = None  # Foreign key reference

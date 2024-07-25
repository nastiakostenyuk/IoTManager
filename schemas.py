from pydantic import BaseModel, Field


class DeviceModel(BaseModel):
    """
    Pydantic model representing a device.

    Attributes:
        name (str): The name of the device (required, min length 3).
        type (str): The type of the device.
        login (str): The login credentials for the device.
        password (str): The password for the device (required, min length 3).
        location_id (int, optional): The ID of the device's location (foreign key).
        api_user_id (int, optional): The ID of the API user associated with the device (foreign key).
    """

    name: str = Field(..., min_length=3)
    type: str
    login: str
    password: str = Field(..., min_length=3)
    location_id: int = None  # Foreign key reference
    api_user_id: int = None  # Foreign key reference

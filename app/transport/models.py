from pydantic import BaseModel, Field
from typing import List

class NewTransportation(BaseModel):
    car_number: str = Field(..., max_lenght = 40)
    packages: List[str] # list of object ids if needed
    current_driver: str = Field(..., description='UniqueId of user')
    current_location: list = Field(..., description='lon, lat')

    class Config:
        schema_extra = {
            "example": {
                "car_number": "AO1111AO",
                "packages": ["", ""],
                "current_driver": "",
                "current_location": [50.4501, 30.5234]
            }
        }

class ToDeleteTransportation(BaseModel):
    car_number: str = Field(..., max_lenght = 40)

    class Config:
        schema_extra = {
            "example": {
                "car_number": "AO1111AO"
            }
        }

class ToUpdateTransportation(BaseModel):
    car_number: str = Field(..., max_lenght = 40)
    packages: List[str] = []
    current_driver: str = ""
    current_location: list = []

    class Config:
        schema_extra = {
            "example": {
                "car_number": "AO1111AO",
                "packages": ["", ""],
                "current_driver": "",
                "current_location": [50.4501, 30.5234]
            }
        }


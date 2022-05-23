from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    Body
)
from typing import List

from numpy import double

router = APIRouter(tags=["transport"])
from . import models, logic


@router.post("/createTransportation")
def new_transport(tr: models.NewTransportation) -> dict:
    """
    endpoint for creating new transport
    """
    return logic.create_transportation(tr)


@router.delete("/deleteTransportation")
def delete_transport(tr: models.ToDeleteTransportation) -> dict:
    """
    endpoint for deleting transport
    """
    return logic.delete_transportation(tr)

@router.get("/transportation")
def get_transport(car_number: str = "", current_driver: str = "") -> dict:
    """
    endpoint for getting info about transport by car_number or driver
    """
    return logic.find_transportation(car_number, current_driver)

@router.get("/getTransportLocation")
def get_transport_location(car_number: str = "", current_driver: str = "") -> dict:
    """
    endpoint for getting current_location by car_number or driver
    """
    return {"current_location": logic.find_transportation(car_number, current_driver)["current_location"]}

@router.post("/updateLocation")
def update_transport_location(car_number: str = Body(...), location: List[float] = Body(...)) -> dict:
    """
    endpoint for updating location of transport 
    """
    return logic.update_location(car_number, location)

@router.post("/update")
def uodate_transport_fields(toUpdate: models.ToUpdateTransportation) -> dict:
    """
    endpoint for updating fields in transportation document 
    """
    return logic.update_transportation(toUpdate)



    
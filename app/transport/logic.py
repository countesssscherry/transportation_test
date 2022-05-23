from db.collections import transportations
from db.functions import createOne, deleteOne, findOne, updateOne
from .models import NewTransportation, ToDeleteTransportation, ToUpdateTransportation


def create_transportation(transportation: NewTransportation) -> dict:
    create = createOne({
        "car_number": transportation.car_number,
        "packages": transportation.packages,
        "current_driver": transportation.current_driver,
        "current_location": transportation.current_location,
        "prev_locations": []
    }, transportations)
    print(create)
    return create

def delete_transportation(toDelete: ToDeleteTransportation) -> dict:
    delete = deleteOne({"car_number": toDelete.car_number}, transportations)
    return delete

def find_transportation(car_number: str = "", current_driver: str = "") -> dict:
    filter = {}
    # filter can contain or car_number, or current_driver, or both
    if car_number != "": 
        filter['car_number'] = car_number
    if current_driver != "":
        filter['current_driver'] = current_driver
    find = findOne(filter, transportations)
    return find


def update_transportation(toUpdate: ToUpdateTransportation) -> dict:
    toUpdate = {k: v for k, v in toUpdate.__dict__.items() if v not in ["", (), [], None]}
    update = updateOne({"car_number": toUpdate['car_number']}, toUpdate, transportations)
    return update

def update_location(car_number: str, location: list) -> dict:
    find = findOne({"car_number": car_number}, transportations)
    find['prev_locations'].append(find['current_location'])
    return updateOne({"car_number": car_number}, {"current_location": location, "prev_locations": find['prev_locations']}, transportations)


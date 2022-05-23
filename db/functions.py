from datetime import datetime
import pymongo
from fastapi import HTTPException


def createOne(item: dict, collection) -> dict:
    item['createTime'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    res = collection.insert_one(item)
    res = {**{"_id" : str(res.inserted_id)}, **item}
    res['_id'] = str(res['_id'])
    return res

def deleteOne(filter: dict , collection) -> dict:
    res = collection.delete_one(filter)
    if res.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Transportation not found")
    return {"deleted": True}

def findOne(filter: dict, collection) -> dict:
    res = collection.find_one(filter)
    if res != None:
        res['_id'] = str(res['_id'])
    else:
        raise HTTPException(status_code=404, detail="Transportation not found")
    return res

def updateOne(filter: dict, toUpdate: dict, collection) -> dict:
    print(toUpdate)
    collection.update_one(filter, {"$set": toUpdate})
    return {"updated": True}




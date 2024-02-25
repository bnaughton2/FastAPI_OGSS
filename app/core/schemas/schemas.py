#schemas.py
from typing import Optional
from pydantic import BaseModel
from datetime import datetime,date

class StoreSalesSchema(BaseModel):
    id: str
    date: date
    storeSales: float
    storeMargin: float 
    storeMembers: int 
    updatedOn: datetime
    updatedBy: str
    addedOn: datetime
    addedBy: str

    class Config:
        orm_mode = True
#Pydantic's orm_mode will tell the Pydantic model to read the data #even if it is not a dict, 
#but an ORM model (or any other arbitrary #object with attributes).
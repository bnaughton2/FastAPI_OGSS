from sqlalchemy.orm import Session
from app.core.models.models import StoreSalesModel

def get_storedata(db: Session, skip: int=0,limit: int=1000):
    return db.query(StoreSalesModel).offset(skip).limit(limit).all()

def post_storedata(db: Session, data):
    actual = StoreSalesModel(** data.model_dump())
    db.add(actual)
    db.commit()
    return "Success"
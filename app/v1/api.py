from sqlalchemy.orm import Session
from app.core.schemas.schemas import StoreSalesSchema
from app.core.models.models import StoreSalesModel
from app.core.models.models import Base
from app.core.models.database import SessionLocal,engine
from fastapi import APIRouter, Depends
from app.v1.endpoints import storeData

Base.metadata.create_all(bind=engine)

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix='/api/v1'
)

@router.get('/hello')
def hello():
    return {"Message": "Hello World"}

@router.get("/store-data",response_model=list[StoreSalesSchema])
def read_storedata(skip: int=0, limit: int=1000, db: Session = Depends(get_db)):
    store_data = storeData.get_storedata(db, skip=skip,limit=limit)
    return store_data
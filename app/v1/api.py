from sqlalchemy.orm import Session
from app.core.schemas.schemas import StoreSalesSchema, PayrollSchema
from app.core.models.models import StoreSalesModel, PayrollModel
from app.core.models.models import Base, Request, ChecklistRequest
from app.core.models.database import SessionLocal,engine
from fastapi import APIRouter, Depends
from app.v1.endpoints import crud

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
    store_data = crud.get_storedata(db, skip=skip,limit=limit)
    return store_data

# @router.get("/payroll",response_model=list[PayrollSchema])
# def readPayData(skip: int=0, limit: int=1000, db: Session = Depends(get_db)):
#     payData = crud.get_paydata(db, skip=skip,limit=limit)
#     return payData

@router.post("/dashboard")
def getDashboardData(data: Request, db: Session = Depends(get_db)):
    return crud.queryDashboardData(db, data)

@router.post("/checklist")
def getChecklist(data: ChecklistRequest, db: Session = Depends(get_db)):
    return crud.getChecklistData(db, data)

@router.post("/store")
def getStoreData(data: Request, db: Session = Depends(get_db)):
    return crud.queryStoreSales(db, data)

@router.post("/fuel")
def getFuelData(data: Request, db: Session = Depends(get_db)):
    return crud.queryFuelSales(db, data)

@router.post("/oil")
def getOilData(data: Request, db: Session = Depends(get_db)):
    return crud.queryOilSales(db, data)

@router.post("/wash")
def getWashData(data: Request, db: Session = Depends(get_db)):
    return crud.queryWashSales(db, data)

@router.post("/damages")
def getDamageData(data: Request, db: Session = Depends(get_db)):
    return crud.queryDamages(db, data)

@router.post("/payroll")
def getPayrollData(data: Request, db: Session = Depends(get_db)):
    return crud.queryPayroll(db, data)
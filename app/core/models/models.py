#models.py
from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime,Float,Text
from app.core.models.database import Base
from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
#The __tablename__ attribute should be the actual name of the #database we are connecting to
class Request(BaseModel):
    startDate: date
    endDate: date

class ChecklistRequest(BaseModel):
    startDateTime: datetime
    endDateTime: datetime

class StoreSalesModel(Base):
    __tablename__ = "StoreSales"
    model_config = ConfigDict(from_attributes=True)

    id = Column(String, primary_key=True)
    date = Column(Date)
    storeSales = Column(Float)
    storeMargin = Column(Float)
    storeMembers = Column(Integer)
    vendingSales = Column(Float)
    memberSales = Column(Float)
    lotterySales = Column(Float)
    updatedOn = Column(DateTime)
    updatedBy = Column(String)
    addedOn = Column(DateTime)
    addedBy = Column(String)


class OilSalesModel(Base):
    __tablename__ = "RealTimeOilSales"
    model_config = ConfigDict(from_attributes=True)

    id = Column(String, primary_key=True)
    date = Column(Date)
    grossSales = Column(Float)
    promotionAmount = Column(Float)
    emmissionsDone = Column(Integer)
    vinChecksDone = Column(Integer)
    oilMargin = Column(Float)
    updatedOn = Column(DateTime)
    updatedBy = Column(String)
    addedOn = Column(DateTime)
    addedBy = Column(String)


class FuelSalesModel(Base):
    __tablename__ = "FuelSales"
    model_config = ConfigDict(from_attributes=True)

    id = Column(String, primary_key=True)
    date = Column(Date)
    fuelSales = Column(Float)
    fuelVolume = Column(Float)
    fuelMargin = Column(Float)
    updatedOn = Column(DateTime)
    updatedBy = Column(String)
    addedOn = Column(DateTime)
    addedBy = Column(String)


class ConnectTeamModel(Base):
    __tablename__ = "ConnectTeam"
    model_config = ConfigDict(from_attributes=True)

    id = Column(String, primary_key=True)
    date = Column(DateTime)
    person = Column(String)
    fullTask = Column(String)
    action = Column(String)
    updatedOn = Column(DateTime)
    updatedBy = Column(String)
    addedOn = Column(DateTime)
    addedBy = Column(String)


class CarwashModel(Base):
    __tablename__ = "Carwash"
    model_config = ConfigDict(from_attributes=True)

    id = Column(String, primary_key=True)
    date = Column(Date)
    washMembers = Column(Integer)
    washSales = Column(Float)
    washMargin = Column(Float)
    updatedOn = Column(DateTime)
    updatedBy = Column(String)
    addedOn = Column(DateTime)
    addedBy = Column(String)


class WaitTimesModel(Base):
    __tablename__ = "WaitTimes"
    model_config = ConfigDict(from_attributes=True)

    id = Column(String, primary_key=True)
    location = Column(String)
    department = Column(String)
    time = Column(DateTime)
    updatedOn = Column(DateTime)
    updatedBy = Column(String)
    addedOn = Column(DateTime)
    addedBy = Column(String)


class PayrollModel(Base):
    __tablename__ = "Payroll"
    model_config = ConfigDict(from_attributes=True)

    id = Column(String, primary_key=True)
    startDate = Column(Date)
    endDate = Column(Date)
    amount = Column(Float)
    updatedOn = Column(DateTime)
    updatedBy = Column(String)
    addedOn = Column(DateTime)
    addedBy = Column(String)


class AppParamsModel(Base):
    __tablename__ = "AppParams"
    model_config = ConfigDict(from_attributes=True)

    ID = Column(Integer, primary_key=True)
    OilMargin = Column(Float)
    WashMargin = Column(Float)
    StoreMargin = Column(Float)
    FuelMargin = Column(Float)
    lastUpdated = Column(DateTime)


class DamagesModel(Base):
    __tablename__ = "Damages"
    model_config = ConfigDict(from_attributes=True)

    id = Column(String, primary_key=True)
    department = Column(String)
    date = Column(Date)
    paymentMethod = Column(String)
    driverName = Column(String)
    cost = Column(Float)
    description = Column(Text)
    submittedBy = Column(String)
    updatedOn = Column(DateTime)
    updatedBy = Column(String)
    addedOn = Column(DateTime)
    addedBy = Column(String)

# class Scorecard(Base):
#     __tablename__ = "Scorecard"
#     model_config = ConfigDict(from_attributes=True)

#     id = Column(String, primary_key=True)
#     date = Column(Date)
#     csaToday = Column(String)
#     csaMonthly = Column(String)
#     prodToday = Column(String)
#     prodMonthly = Column(String)
#     store1Today = Column(String)
#     store1Monthly = Column(String)
#     store2Today = Column(String)
#     store2Monthly = Column(String)
#     updatedOn = Column(DateTime)
#     updatedBy = Column(String)
#     addedOn = Column(DateTime)
#     addedBy = Column(String)
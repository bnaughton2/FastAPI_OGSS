#models.py
from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime,Float,Text
from app.core.models.database import Base
#The __tablename__ attribute should be the actual name of the #database we are connecting to
class StoreSalesModel(Base):
    __tablename__ = "StoreSales"

    id = Column(Text, primary_key=True)
    date = Column(Date)
    storeSales = Column(Float)
    storeMargin = Column(Float)
    storeMembers = Column(Integer)
    updatedOn = Column(DateTime)
    updatedBy = Column(Text)
    addedOn = Column(DateTime)
    addedBy = Column(Text)

    class Config:
        orm_mode = True

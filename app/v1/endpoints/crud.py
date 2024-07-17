from sqlalchemy.orm import Session
from app.core.models.models import StoreSalesModel, PayrollModel, FuelSalesModel, CarwashModel, OilSalesModel, ConnectTeamModel, WaitTimesModel, PayrollModel, DamagesModel
from datetime import datetime

def get_storedata(db: Session, skip: int=0,limit: int=1000):
    return db.query(StoreSalesModel).offset(skip).limit(limit).all()

def post_storedata(db: Session, data):
    actual = StoreSalesModel(** data.model_dump())
    db.add(actual)
    db.commit()
    return "Success"

def get_paydata(db: Session, skip: int=0, limit: int=1000):
    return db.query(PayrollModel).offset(skip).limit(limit).all()


def queryFuelSales(db: Session, data):
    numDays = abs((data.endDate - data.startDate).days) + 1
    profit = 0
    volume = 0
    sales = 0
    margin = 0
    fuelData = db.query(FuelSalesModel).filter(FuelSalesModel.date.between(data.startDate, data.endDate)).all()
    if len(fuelData) >= 1:
        updatedOn = fuelData[0].__dict__['updatedOn']
        for x in fuelData:
            row = x.__dict__
            updatedOn = row['updatedOn'] if updatedOn < row['updatedOn'] else updatedOn
            profit += (row['fuelVolume'] * row['fuelMargin'])
            margin += row['fuelMargin']
            sales += row['fuelSales']
            volume += row['fuelVolume']
            #Reformat last mod later
        out = {
            "lastMod": updatedOn,
            "sales": round(sales, 2),
            "profit": round(profit, 2),
            "volume": round(volume, 2),
            "margin": round((margin / numDays), 4)
        }
        return out
    else:
        return {"response": "No Data available"}

def queryStoreSales(db: Session, data):
    LOTTERY_PROF_MULT = .05
    profit = 0
    sales = 0
    storeMembers = 0
    vendingSales = 0
    lotterySales = 0
    memberSales = 0
    storeData = db.query(StoreSalesModel).filter(StoreSalesModel.date.between(data.startDate, data.endDate)).all()
    if len(storeData) >= 1:
        updatedOn = storeData[0].__dict__['updatedOn']
        for x in storeData:
            row = x.__dict__
            if row['updatedOn'] > updatedOn:
                updatedOn = row['updatedOn']
                storeMembers = row['storeMembers']
            profit += (row['storeSales'] * row['storeMargin'])
            sales += row['storeSales']
            vendingSales += row['vendingSales']
            lotterySales += row['lotterySales']
            memberSales += row['memberSales']
            #Reformat last mod later
        lotteryProfit = (lotterySales*LOTTERY_PROF_MULT)
        out = {
            "lastMod": updatedOn,
            "sales": sales,
            "profit": round((profit + vendingSales + lotteryProfit), 2),
            "vendingSales": round(vendingSales, 2),
            "lotterySales": round(lotteryProfit, 2),
            "memberSales": round(memberSales, 2),
            "members": storeMembers
        }
        return out
    else:
        return {"response": "No Data available"}

def queryWashSales(db: Session, data):
    profit = 0
    sales = 0
    washMembers = 0
    washData = db.query(CarwashModel).filter(CarwashModel.date.between(data.startDate, data.endDate)).all()
    if len(washData) >= 1:
        updatedOn = washData[0].__dict__['updatedOn']
        for x in washData:
            row = x.__dict__
            if row['updatedOn'] > updatedOn:
                updatedOn = row['updatedOn']
                washMembers = row['washMembers']
            profit += (row['washSales'] * row['washMargin'])
            sales += row['washSales']
            #Reformat last mod later
        out = {
            "lastMod": updatedOn,
            "sales": round(sales, 2),
            "profit": round(profit, 2),
            "washMembers": washMembers,
        }
        return out
    else:
        return {"response": "No Data available"}

def queryOilSales(db: Session, data):
    EMISSIONS_PROF_MULT = 14
    VINCHECK_PROF_MULT = 10
    profit = 0
    sales = 0
    emissionsDone = 0
    vinChecksDone = 0
    oilData = db.query(OilSalesModel).filter(OilSalesModel.date.between(data.startDate, data.endDate)).all()
    if len(oilData) >= 1:
        updatedOn = oilData[0].__dict__['updatedOn']
        for x in oilData:
            row = x.__dict__
            updatedOn = row['updatedOn'] if updatedOn < row['updatedOn'] else updatedOn
            profit += (row['grossSales'] * row['oilMargin'])
            sales += row['grossSales']
            emissionsDone += row['emmissionsDone']
            vinChecksDone += row['vinChecksDone']
            #Reformat last mod later
        emissionsProfit = (emissionsDone * EMISSIONS_PROF_MULT)
        vinChecksProfit = (vinChecksDone * VINCHECK_PROF_MULT)
        out = {
            "lastMod": updatedOn,
            "sales": round(sales, 2),
            "profit": round((profit + emissionsProfit + vinChecksProfit), 2),
            "emissions": round(emissionsProfit, 2),
            "vinChecks": round(vinChecksProfit, 2)
        }
        return out
    else:
        return {"response": "No Data available"}

def queryDamages(db: Session, data):
    damagesWash = 0
    damagesOil = 0
    damageData = db.query(DamagesModel).filter(DamagesModel.date.between(data.startDate, data.endDate)).all()
    if len(damageData) >= 1:
        updatedOn = damageData[0].__dict__['updatedOn']
        for x in damageData:
            row = x.__dict__
            updatedOn = row['updatedOn'] if updatedOn < row['updatedOn'] else updatedOn
            if row['department'] == "Wash":
                damagesWash += row['cost']
            elif row['department'] == "Oil":
                damaagesOil += row['cost']
            #Reformat last mod later
        out = {
            "lastMod": updatedOn,
            "damagesWash": damagesWash,
            "damagesOil": damagesOil
        }
        return out
    else:
        return {"response": "No Data available"}

def queryPayroll(db: Session, data):
    numDays = abs((data.endDate - data.startDate).days) + 1
    periodPay = 0
    dailyPay = 0
    payrollData = db.query(PayrollModel).filter(PayrollModel.startDate <= data.startDate, PayrollModel.endDate > data.startDate).all()
    # payrollData = db.query(PayrollModel).filter(PayrollModel.date.between(data.startDate, data.endDate)).all()
    if len(payrollData) >= 1:
        updatedOn = payrollData[0].__dict__['updatedOn']
        for x in payrollData:
            row = x.__dict__
            periodPay = row['amount']
            dailyPay = periodPay / 14
            #Reformat last mod later
    else:
        payrollData = db.query(PayrollModel).order_by(PayrollModel.endDate.desc()).first()
        if payrollData is not None:
            row = payrollData.__dict__
            updatedOn = row['updatedOn']
            periodPay = row['amount']
            dailyPay = periodPay / 14
        else:
            return {"response": "No Data available"}
    out = {
            "periodPay": periodPay,
            "dailyPay": dailyPay,
            "totalPay": round((dailyPay * numDays), 2),
            "numberOfDays": numDays
        }
    return out

def queryChecklist(db: Session, data):
    washOpen, washClose = 0, 0
    oilOpen, oilClose = 0, 0
    storeOpen, storeClose = 0, 0
    siteOps7, siteOps11 = 0, 0

    checklistData = db.query(ConnectTeamModel).filter(ConnectTeamModel.date >= data.startDateTime, ConnectTeamModel.date < data.endDateTime).all()
    if len(checklistData) >= 1:
        date = checklistData[0].__dict__['date']
        for x in checklistData:
            row = x.__dict__
            date = row['date'] if date < row['date'] else date
            if row['action'] == 'Open Wash':
                washOpen += 33
            elif row['action'] == 'Close Wash':
                washClose += 50
            elif row['action'] == 'Open Grocery':
                storeOpen += 33
            elif row['action'] == 'Close Grocery':
                storeClose += 50
            elif row['action'] == 'Open Oil':
                oilOpen += 50
            elif row['action'] == 'Close Oil':
                oilClose += 50
            elif row['fullTask'] == 'Site Operations 7-10AM':
                siteOps7 = 100
            elif row['fullTask'] == 'Site Operations 11-12' or row['fullTask'] == 'Site Operations 1-4pm':
                siteOps11 = 100
        washOpen = 100 if washOpen > 98 else washOpen
        storeOpen = 100 if storeOpen > 98 else storeOpen
        out = {
            "lastMod": date,
            "washOpen": washOpen,
            "washClose": washClose,
            "storeOpen": storeOpen,
            "storeClose": storeClose,
            "oilOpen": oilOpen,
            "oilClose": oilClose,
            "siteOps7": siteOps7,
            "siteOps11": siteOps11
        }
    else:
        out = {"Error": "No Data Availale"}
    return out

def queryWaitTimes(db: Session, data):
    waitStore = 0
    waitSales = 0
    waitLoad = 0
    waitTimeData = db.query(WaitTimesModel).filter(WaitTimesModel.time >= data.startDateTime, WaitTimesModel.time < data.endDateTime).all()
    if len(waitTimeData) >= 1:
        for x in waitTimeData:
            row = x.__dict__
            if row['department'] == 'TB12CWCstr':
                waitStore += 1
            elif row['department'] == 'TB12CWSales':
                waitSales += 1
            elif row['department'] == 'TB12CWLoad':
                waitLoad += 1
        out = {
            "waitStore": waitStore,
            "waitSales": waitSales,
            "waitLoad": waitLoad
        }
    else:
        out = {"Error": "No Data Available"}
    return out



def queryDashboardData(db: Session, data):
    numDays = abs((data.endDate - data.startDate).days) + 1
    gas = queryFuelSales(db, data)
    store = queryStoreSales(db, data)
    wash = queryWashSales(db, data)
    oil = queryOilSales(db, data)
    damages = queryDamages(db, data)
    payroll = queryPayroll(db, data)
    PROFIT_CORRECTION = 5833
    totalProfitCorrection = (numDays * PROFIT_CORRECTION)
    dashboardData = {
        "gas": gas,
        "store": store,
        "wash": wash,
        "oil": oil,
        "damages": damages,
        "payroll": payroll,
        "extras": {
            "lastMod": max([gas['lastMod'], store['lastMod'], wash['lastMod'], oil['lastMod']]),
            "profitCorrection": round(totalProfitCorrection, 2),
            "totalProfit": round(((gas['profit'] + store['profit'] + wash['profit'] + oil['profit']) - payroll['totalPay'] - totalProfitCorrection),2)
        }
        }
    return dashboardData

def getChecklistData(db: Session, data):
    checklist = queryChecklist(db, data)
    waitTimes = queryWaitTimes(db, data)

    checklistData = {
        "checklist": checklist,
        "waitTimes": waitTimes
    }
    return checklistData
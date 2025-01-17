import json
from web3 import Web3
from . import models
from datetime import date


web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
one_app = "0xD289dEa562C50f10B89d75Ff155796aa6Aa3665a"

contract_address_for_user = "0x34807573b552422f7106E49987B37fe04EF50f14"


##Contract for users
with open("blocks/build/contracts/UserPoint.json") as abiFile:
    abidata = json.load(abiFile)
    realABI = abidata["abi"]
    contract_user = web3.eth.contract(address=contract_address_for_user, abi=realABI)

##contract of Files
contract_address_of_details = "0xB1CeE53D2D074a20260cFCF751889340ed049ceA"
with open("blocks/build/contracts/DetailsKyc.json") as abiFileOF:
    abiFileData = json.load(abiFileOF)
    abiData = abiFileData["abi"]
    contract_of_files = web3.eth.contract(
        address=contract_address_of_details, abi=abiData
    )
## 


def userAdd(name, mobile, email, password, adress, typeUser):
    user = getUsersDetails()[3]
    if email in user:
        return "Try with another email"
    else:
        contract_user.functions.addPress(
            str(name).strip(),
            str(mobile).strip(),
            str(email).strip(),
            str(typeUser).strip(),
            str(password).strip(),
            str(adress).strip(),
        ).transact({"from": one_app})
    return "Success"


def getUsersDetails():
    id, name, mobile, email, actor, adress, password = (
        contract_user.functions.getUsers().call({"from": one_app})
    )
    return [id, name, mobile, email, actor, adress, password]


def loginSubmit(email, password):
    if "admin@gmail.com" == email and password == "admin":
        models.LocalStore(0, 0, "admin").save()
        return "/"
    else:
        data = getUsersDetails()
        print(data)
        for i in range(len(data[0])):
            if data[3][i] == email and data[6][i] == password:
                if data[4][i] == "user":
                    models.LocalStore(0, data[0][i], "user").save()
                    return "/"
                elif data[4][i] == "organisation":
                    models.LocalStore(0, data[0][i], "orgnaisation").save()
                    return "/"
        return "Invalid User"


def getTypeDiffer(type,userid):
    data = []
    viewuser = getUsersDetails()
    if "getNameOfOrganisations" == type:
        for i in range(len(viewuser[0])):
            if viewuser[4][i] == "organisation":
                data.append(
                    {
                        "name": viewuser[1][i],
                        "id": viewuser[0][i],
                    }
                )
    elif "NothingUserProfile"==type:
        for i in range(len(viewuser[0])):
            if viewuser[0][i] == int(userid):
                data.append(
                    {
                        "id": viewuser[0][i],
                        "name": viewuser[1][i],
                        "mobile": viewuser[2][i],
                        "email": viewuser[3][i],
                        "adress": viewuser[5][i],
                    }
                )
    else:
        readid=0
        for i in range(len(viewuser[0])):
            if viewuser[4][i] == type:
                readid+=1
                data.append(
                    {
                        "readid":readid,
                        "id": viewuser[0][i],
                        "name": viewuser[1][i],
                        "mobile": viewuser[2][i],
                        "email": viewuser[3][i],
                        "adress": viewuser[5][i],
                    }
                )
            
    return data


def getApplied(type, userid):
    data = []
    if "getMyUserOrder" == type:
        view = getContractsOfMe()

        companyDetails = getUsersDetails()
        for i in range(len(view[0])):
            if str(view[2][i]) == str(userid):
                details = {}
                for values in range(len(companyDetails[0])):
                    if str(companyDetails[0][values]) == str(view[1][i]):
                        details["NameOfCompany"] = companyDetails[1][values]
                        details["Email"] = companyDetails[3][values]
                        details["Address"] = companyDetails[5][values]
                datePoint=date.fromtimestamp(float(int(view[11][i])/1000))
                data.append(
                    {
                        "id": view[0][i],
                        "NameOfCompany": details["NameOfCompany"],
                        "Email": details["Email"],
                        "Address": details["Address"],
                        "companyId": view[1][i],
                        "userId": view[2][i],
                        "fullName": view[3][i],
                        "motherName": view[4][i],
                        "adhaarName": view[5][i],
                        "panNumber": view[6][i],
                        "drivingPath": view[7][i],
                        "adhaarPath": view[8][i],
                        "photoPath": view[9][i],
                        "status": view[10][i],
                        "appliedOn": f"{datePoint.day}-{datePoint.month}-{datePoint.year} ",
                    }
                )
    elif "getComapanyApplied"==type:
        view = getContractsOfMe()
        companyDetails = getUsersDetails()
        for i in range(len(view[0])):
            if str(view[1][i]) == str(userid):
                details = {}
                for values in range(len(companyDetails[0])):
                    if str(companyDetails[0][values]) == str(view[2][i]):
                        details["NameofUser"] = companyDetails[1][values]
                        details["Email"] = companyDetails[3][values]
                        details["Address"] = companyDetails[5][values]
                datePoint=date.fromtimestamp(float(int(view[11][i])/1000))
                data.append({
                        "id": view[0][i],
                        "NameofUser": details["NameofUser"],
                        "Email": details["Email"],
                        "Address": details["Address"],
                        "companyId": view[1][i],
                        "userId": view[2][i],
                        "fullName": view[3][i],
                        "motherName": view[4][i],
                        "adhaarName": view[5][i],
                        "panNumber": view[6][i],
                        "drivingPath": view[7][i],
                        "adhaarPath": view[8][i],
                        "photoPath": view[9][i],
                        "status": view[10][i],
                        "appliedOn": f"{datePoint.day}-{datePoint.month}-{datePoint.year} ",
                    }
                )

    return data


def addFileOF(
    companyId,
    userId,
    fullName,
    motherName,
    adhaarName,
    panNumber,
    drivingPath,
    adhaarPath,
    photoPath,
    applied,
):

    contract_of_files.functions.addPress(
        int(companyId),
        int(userId),
        fullName,
        motherName,
        adhaarName,
        panNumber,
        drivingPath,
        adhaarPath,
        photoPath,
        "Pending",
        applied,
    ).transact({"from": one_app})


def getContractsOfMe():
    (
        id,
        companyId,
        userId,
        fullName,
        motherName,
        adhaarName,
        panNumber,
        drivingPath,
        adhaarPath,
        photoPath,
        status,
        applied,
    ) = contract_of_files.functions.getUsers().call({"from": one_app})
    return [
        id,
        companyId,
        userId,
        fullName,
        motherName,
        adhaarName,
        panNumber,
        drivingPath,
        adhaarPath,
        photoPath,
        status,
        applied,
    ]

def updateStateOfContract(docId,status):
    contract_of_files.functions.updateStatus(status,docId).transact({
            'from':one_app,
            'gas':600000
        })
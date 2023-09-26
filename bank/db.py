import json


def loadjson(db="./database.json"):
    with open(db,"r")as f:
        return json.load(f)
    

def writejson(data:dict,db="./database.json"):
    with open(db,'w') as f:
        json.dump(data,f,indent=4)


def adduser(username,password):
    data = loadjson()
    index = data["index"]
    user={"username":username,
     "password":password,
     "id":index,
     "balance":0
     }
    data['index'] = index+1
    data['accounts'].append(user)
    writejson(data)

def addbalance(userid,balace):
    data = loadjson()
    for user in data["accounts"]:
        if user["id"] == userid:
            user["balance"] += balace
    writejson(data)


def pulluser(info):
    data = loadjson()
    for user in data["accounts"]:
        if (user["id"] == info) or user["username"] == info:
            return user
    return False

def loginChecker(username,password):
    data = loadjson()
    for user in data["accounts"]:
        if (user["username"] == username) and (user["password"] == password):
            return user["id"]
    return False







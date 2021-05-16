import requests
import json
import allure

baseURL="https://reqres.in"

@allure.step("Executing getUsersapi method ")
def getUsersapi():
    params = {'page': 2}
    response = requests.get(baseURL+"/api/users",params=params)
    allure.dynamic.description("Launching "+baseURL+"/api/users")
    print(response)
    print(json.dumps(response.json(),indent=4))
    assert response.status_code == 200
    allure.dynamic.description("Validating 200 Status code")
    if response.status_code==200:
        res=response.json()
        for d in res["data"]:
            print(d['id'] ," ",d["first_name"])
            allure.dynamic.description("STATUS CODE:"+str(response.status_code)+" || "+str(d['id'] )+" || "+str(d['first_name']))
def getSingleUsrAPI(param):
    response=requests.get(baseURL+"/api/users/"+str(param))
    if response.status_code==200:
        print(response)
        print(json.dumps(response.json(), indent=4))
    elif response.status_code==404:
        print("No user found")
def addUserAPI():
    data={
    "name": "mohakjhheus",
    "job": "leadessr"
    }
    response=requests.post(baseURL+"/api/users",data=data)
    print(response)
    if response.status_code==201:
        print(response)
        print(json.dumps(response.json(), indent=4))
def updateUserAPI(param):
    data={
    "name": "nagesh",
    "job": "Tech Lead"
    }
    print(data)
    response=requests.put(baseURL+"/api/users/"+str(param),data=data)
    if response.status_code==200:
        print(response)
        print(json.dumps(response.json(), indent=4))
def insertUserAPI():
    data={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }
    response = requests.post(baseURL + "/api/register", data=data)
    print(response)
    if response.status_code==200:
        print(response)
        print(json.dumps(response.json(), indent=4))
        res=response.json()
        id=res['id']
        token=res['token']
    elif response.status_code==400:
        if response.text=='{"error":"Missing password"}':
            print(response.text)
    return id,token
def loginAPI(id,token):
    data={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }
    response = requests.post(baseURL + "/api/login", data=data)
    print(response)
    if response.status_code==200 and id==4:
        print(response)
        print(json.dumps(response.json(), indent=4))
        print("Login succcess")
    elif response.status_code==400:
        print(response.text)
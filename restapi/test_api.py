from BaseAPI import getUsersapi, getSingleUsrAPI, addUserAPI, updateUserAPI, insertUserAPI, loginAPI

import allure
import allure_commons

@allure.step("Executing getUsersapi()")
def test_getUsersapi():
    assert False
    getUsersapi()
@allure.step("Executing getSingleUsrAPI")
def test_getSingleUsrAPI():
    getSingleUsrAPI(2)

@allure.step("Executing getUsersapi()")
def test_addUserAPI():
    addUserAPI()
@allure.step("Executing getUsersapi()")
def test_updateUserAPI():
    updateUserAPI(2)

@allure.step("Executing insertUserAPI() and loginAPI")
def test_insertUserAPI():
    id,token=insertUserAPI()
    allure.dynamic.description("Entred ID and Token for Login method")
    # assert False
    loginAPI(id, token)

from BaseAPI import getUsersapi, getSingleUsrAPI, addUserAPI, updateUserAPI, insertUserAPI, loginAPI


getUsersapi()
getSingleUsrAPI(2)
addUserAPI()
updateUserAPI(2)
id,token=insertUserAPI()
getSingleUsrAPI(id)
loginAPI(id,token)

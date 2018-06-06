#create class for
class RequestModel:
    def __init__(self, _id, _request, _type):
        self._request = _request
        self._type = _type
        self._id = _id
    
    def get_id(self):
        return self._id
    
    def get_request(self):
        return self._request

    def get_type(self):
        return self._type

    def get_dict(self):
        return{'_id':self._id,
        '_type':self._type,
        '_request':self._request}


maintance_requests = [
{'_id':'1','_request':'Computer not working','_type':'maintenance'}
]
#create class for users
class UserModel:
    def __init__(self, _id, _username, _password):
        self._id = _id
        self._username = _username
        self._password = _password
    
    def get_id(self):
        return self._id
    
    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_dict(self):
        return{'_id':self._id,
        '_username':self._username,
        '_password':self._password}






user_list = [
{'_id':'1','_username':'RachaelN','_password':'123abc'}
   
]
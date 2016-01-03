import requests
from srapi import API_BASE_URL, APIBase

class Podfiles(APIBase):
    api_url = API_BASE_URL+"podfiles"
    
    def get_all_podfiles(self, programid, params={}):
        params["programid"] = programid
        return self.get_api_data("podfiles", params)

class Podfile(APIBase):
    def get_podfile(self, podid):
        params = {'format':'json', 'pagination':'false'}

        r = requests.get(API_BASE_URL+"podfiles/%s" % podid, params=params)
        return r.json()['podfile']
        

        

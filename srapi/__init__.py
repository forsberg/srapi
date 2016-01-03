import requests

API_BASE_URL="http://api.sr.se/api/v2/"

class APIBase(object):
    def get_api_data(self, objectstag, params={}):
        params["format"] = "json"
        params["pagination"] = "false"

        r = requests.get(self.api_url, params=params)
        json = r.json()
        for entry in json[objectstag]:
            yield entry

    def get_single_entry(self, tag):
        params["format"] = "json"
        params["pagination"] = "false"

        r = requests.get(self.api_url, params=params)
        return r.json()[tag]
        

from srapi.programs import Programs
from srapi.podfiles import Podfile, Podfiles

def tool():
    for p in Programs().get_all_programs():
        print p["name"].encode("utf-8"), p["id"]

    for p in Podfiles().get_all_podfiles(411):
        print p["title"], p["url"]
    

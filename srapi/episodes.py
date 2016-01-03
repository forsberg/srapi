from srapi import API_BASE_URL, APIBase

class Episodes(APIBase):
    api_url = API_BASE_URL+"episodes/index"
    
    def get_all_episodes(self, programid, params={}):
        params["programid"] = programid
        return self.get_api_data("episodes", params)
        

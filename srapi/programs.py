from srapi import API_BASE_URL, APIBase

class Programs(APIBase):
    api_url = API_BASE_URL+"programs"
    
    def get_all_programs(self, params={}):
        return self.get_api_data("programs", params)

    def get_all_programs_with_pod(self, params={}):
        params.update({"filter":"program.haspod","filterValue":"true",})
        return self.get_all_programs(params)
        
        

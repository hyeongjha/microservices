import requests

class HttpRepository():
    base_url = None
    
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        
    def do_get(self, path):
        response = requests.get(self.get_url(path))
        return response.text
    
    def do_post(self, path, request_body = None, request_params = None):
        response = requests.post(url=self.get_url(path), data=request_body, params=request_params)
        return response.text
    
    def get_url(self,path):
        return "{}{}".format(self.base_url, path)
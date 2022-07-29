from http_repository import HttpRepository
import json

class FxRateApiClient(HttpRepository):
    fx_rates = None
    def __init__(self) -> None:
        super().__init__("http://127.0.0.1:8000/api/fxrate")
        
    def get_fx_rate(self):
        if self.fx_rates == None:
            self.fx_rates = json.loads(super().do_get("/get_fx_rate"))            
        return self.fx_rates
    
    def add_new_fx_rate(self, new_rate):
        request = {"fx_entry": json.dumps(new_rate)}
        return super().do_post("/add",request_params=request)
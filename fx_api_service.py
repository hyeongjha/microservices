from fastapi import FastAPI
from fx_rate_repository import FxRateRepository
import json

app = FastAPI()
fxRateRepository = FxRateRepository()

@app.get("/api/fxrate/get_fx_rate")
def get_fx_rate():
    return fxRateRepository.get_fx_rate()


@app.post("/api/fxrate/add")
def add_fx_rate(fx_entry):
    fxRateRepository.add_new_fx_rate(json.loads(fx_entry))
    return json.dumps({"code":200, "isSucess":True})


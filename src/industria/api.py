"""API de predição de falha da maquina"""
from fastapi import FastAPI
from pydantic import BaseModel
from industria.predict import prever

app = FastAPI(title="IndustrIA - Manutenção Preditiva")


class Leitura(BaseModel):
    air_temp: float
    process_temp: float
    rotational_speed: float
    torque: float
    tool_wear: float
    type: str


@app.post("/predict")
def predict(leitura: Leitura):
    dados = {
        "Air temperature [K]": leitura.air_temp,
        "Process temperature [K]": leitura.process_temp,
        "Rotational speed [rpm]": leitura.rotational_speed,
        "Torque [Nm]": leitura.torque,
        "Tool wear [min]": leitura.tool_wear,
        "Type": leitura.type

    }
    return prever(dados)
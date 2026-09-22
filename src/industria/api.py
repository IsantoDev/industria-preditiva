"""API de predição de falha da maquina"""
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
from fastapi.responses import FileResponse
from pathlib import Path
from industria.predict import prever

app = FastAPI(title="IndustrIA - Manutenção Preditiva")
STATIC_DIR = Path(__file__).resolve().parents[2] / "static"

class Leitura(BaseModel):
    """Define o que cada campo recebe | Field mantém dentro do limite do que já foi treinado."""
    air_temp: float = Field(ge=15, le=40)
    process_temp: float = Field(ge=25, le=50)
    rotational_speed: float = Field(ge=1000, le=3000)
    torque: float = Field(ge=0, le=100)
    tool_wear: float = Field(ge=0, le=300)
    type: Literal["L", "M", "H"]


@app.post("/predict")
def predict(leitura: Leitura):
    dados = {
        "Air temperature [K]": leitura.air_temp + 273.15,
        "Process temperature [K]": leitura.process_temp + 273.15,
        "Rotational speed [rpm]": leitura.rotational_speed,
        "Torque [Nm]": leitura.torque,
        "Tool wear [min]": leitura.tool_wear,
        "Type": leitura.type

    }
    return prever(dados)


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")
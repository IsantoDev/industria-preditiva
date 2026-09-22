"""API de predição de falha da máquina."""
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import Literal
from pathlib import Path
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from industria.predict import prever

# Rate limiter por IP (protege a API pública de abuso/spam)
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="IndustrIA - Manutenção Preditiva")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

STATIC_DIR = Path(__file__).resolve().parents[2] / "raiz"


class Leitura(BaseModel):
    """Define o que cada campo recebe | Field mantém dentro do limite do que já foi treinado."""
    air_temp: float = Field(ge=15, le=40)
    process_temp: float = Field(ge=25, le=50)
    rotational_speed: float = Field(ge=1000, le=3000)
    torque: float = Field(ge=0, le=100)
    tool_wear: float = Field(ge=0, le=300)
    type: Literal["L", "M", "H"]


@app.post("/predict")
@limiter.limit("20/minute")
def predict(request: Request, leitura: Leitura):
    dados = {
        "Air temperature [K]": leitura.air_temp + 273.15,
        "Process temperature [K]": leitura.process_temp + 273.15,
        "Rotational speed [rpm]": leitura.rotational_speed,
        "Torque [Nm]": leitura.torque,
        "Tool wear [min]": leitura.tool_wear,
        "Type": leitura.type,
    }
    return prever(dados)


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")

"""Carrega o modelo e prevê a partir de leituras cruas"""
import joblib
import pandas as pd
from pathlib import Path
from industria.features import add_features

models_dir = Path(__file__).resolve().parents[2]  /"models"
_modelo = joblib.load(models_dir / "modelo_gb.joblib")
_colunas = joblib.load(models_dir / "colunas.joblib")

def prever(leitura: dict) -> dict:
    """Recebe as leituras e devolve a previsão"""
    df = pd.DataFrame([leitura])
    df = add_features(df)
    df = pd.get_dummies(df,columns=["Type"])
    df = df.reindex(columns=_colunas,fill_value=0)
    prob = _modelo.predict_proba(df)[0, 1]
    return{
        "vai falhar": bool(prob>=0.25),
        "probabilidade": round(float(prob), 4),
    }
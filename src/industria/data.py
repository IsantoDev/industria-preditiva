"""Camada de acesso aos dados do projeto."""
import pandas as pd
from pathlib import Path

RAW_CSV = Path('data/raw/ai4i2020.csv')

def load_raw() -> pd.DataFrame:
    "Carrega o CSV bruto para DataFrame"
    return pd.read_csv(RAW_CSV, encoding='utf-8-sig')

if __name__ == "__main__":
    df = load_raw()
    print("Formato (linhas, colunas):", df.shape)
    print(df.head())
    print("\nFalhas (0 = ok, 1 = falhou):")
    print(df["Machine failure"].value_counts())
    print("Proporção de falhas:", round(df["Machine failure"].mean() * 100, 2), "%")
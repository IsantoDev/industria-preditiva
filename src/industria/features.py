"""Engenharia de atributos: features derivadas da física do processo."""
import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Adiciona features físicas ao DataFrame (retorna uma cópia, sem alterar o original)."""
    df = df.copy()
    df["power"] = df["Torque [Nm]"] * df["Rotational speed [rpm]"]      # PWF
    df["temp_diff"] = df["Process temperature [K]"] - df["Air temperature [K]"]  # HDF
    df["strain"] = df["Tool wear [min]"] * df["Torque [Nm]"]            # OSF
    return df
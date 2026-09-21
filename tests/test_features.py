import pandas as pd
from industria.features import add_features


def test_add_features_calcula_certo():
    df = pd.DataFrame({
        "Torque [Nm]": [10.0],
        "Rotational speed [rpm]": [1500],
        "Process temperature [K]": [310.0],
        "Air temperature [K]": [300.0],
        "Tool wear [min]": [50],
    })
    resultado = add_features(df)

    assert resultado["power"].iloc[0] == 10.0 * 1500      
    assert resultado["temp_diff"].iloc[0] == 310.0 - 300.0 
    assert resultado["strain"].iloc[0] == 50 * 10.0         


def test_add_features_nao_altera_original():
    df = pd.DataFrame({
        "Torque [Nm]": [10.0],
        "Rotational speed [rpm]": [1500],
        "Process temperature [K]": [310.0],
        "Air temperature [K]": [300.0],
        "Tool wear [min]": [50],
    })
    add_features(df)
    assert "power" not in df.columns    
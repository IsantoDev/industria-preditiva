from industria.predict import prever


def test_prever_retorna_estrutura_valida():
    leitura = {
        "Air temperature [K]": 300.0,
        "Process temperature [K]": 310.0,
        "Rotational speed [rpm]": 1500,
        "Torque [Nm]": 40.0,
        "Tool wear [min]": 100,
        "Type": "L",
    }
    r = prever(leitura)

    assert "vai_falhar" in r
    assert "probabilidade" in r
    assert isinstance(r["vai_falhar"], bool)
    assert 0.0 <= r["probabilidade"] <= 1.0

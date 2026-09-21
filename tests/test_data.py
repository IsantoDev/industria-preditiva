from industria.data import load_machine_registry


def test_registry_tem_tres_tipos():
    reg = load_machine_registry()
    assert len(reg) == 3
    assert list(reg["Type"]) == ["L", "M", "H"]

"""Baixa o dataset AI4I 2020 (UCI) e extrai o CSV em data/raw/."""
import urllib.request
import zipfile
from pathlib import Path

URL = "https://archive.ics.uci.edu/static/public/601/ai4i+2020+predictive+maintenance+dataset.zip"
RAW_DIR = Path("data/raw")
CSV_PATH = RAW_DIR / "ai4i2020.csv"


def download_dataset() -> Path:
    """Baixa e extrai o dataset, se ainda não existir. Retorna o caminho do CSV."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if CSV_PATH.exists():
        print(f"Dataset já existe em {CSV_PATH}")
        return CSV_PATH

    zip_path = RAW_DIR / "ai4i2020.zip"
    print("Baixando dataset da UCI...")
    urllib.request.urlretrieve(URL, zip_path)

    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(RAW_DIR)

    zip_path.unlink()  # remove o zip após extrair
    print(f"Pronto: {CSV_PATH}")
    return CSV_PATH


if __name__ == "__main__":
    download_dataset()
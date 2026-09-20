"""Camada de banco de dados (SQLite): carrega as fontes e roda queries versionadas."""
import sqlite3
from pathlib import Path
import pandas as pd
from industria.data import load_raw, load_machine_registry

DB_PATH = Path("data/industria.db")
SQL_DIR = Path("sql")


def build_database() -> Path:
    """Cria o banco SQLite com as tabelas 'readings' (fato) e 'machines' (dimensão)."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        load_raw().to_sql("readings", conn, if_exists="replace", index=False)
        load_machine_registry().to_sql("machines", conn, if_exists="replace", index=False)
    return DB_PATH


def run_query(sql_filename: str) -> pd.DataFrame:
    """Lê um arquivo .sql da pasta sql/ e executa, retornando um DataFrame."""
    query = (SQL_DIR / sql_filename).read_text(encoding="utf-8")
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql(query, conn)


if __name__ == "__main__":
    build_database()
    print(run_query("failure_rate_by_quality.sql"))
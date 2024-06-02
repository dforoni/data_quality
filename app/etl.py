import os
from pathlib import Path

import pandas as pd
import pandera as pa
from dotenv import load_dotenv
from sqlalchemy import create_engine
from schema import DataModel

def load_settings():
    """Carrega as configurações a partir de variáveis de ambiente."""
    dotenv_path = Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "db_host": os.getenv("POSTGRES_HOST"),
        "db_user": os.getenv("POSTGRES_USER"),
        "db_pass": os.getenv("POSTGRES_PASSWORD"),
        "db_name": os.getenv("POSTGRES_DB"),
        "db_port": os.getenv("POSTGRES_PORT"),
    }
    return settings

def extract_sql(query: str) -> pd.DataFrame:
    """
    Extrai dados do banco de dados SQL usando a consulta fornecida.

    Args:
        query: A consulta SQL para extrair dados.

    Returns:
        Um DataFrame do Pandas contendo os dados extraídos.
    """
    settings = load_settings()

    # Criar a string de conexão com base nas configurações
    connection_string = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"

    # Criar engine de conexão
    engine = create_engine(connection_string)

    with engine.connect() as conn, conn.begin():
            df = pd.read_sql(query, conn)

    return df

@pa.check_output(DataModel)
def load_csv(name: str):
     df = pd.read_csv(name, sep=";")
     return df

if __name__ == "__main__":
     
     df = load_csv(name = "data/contrato.csv")
    #  schema_pa = pa.infer_schema(df)

    #  with open("inferred_schema.py", "w", encoding="utf-8") as file:
    #      file.write(schema_pa.to_script())
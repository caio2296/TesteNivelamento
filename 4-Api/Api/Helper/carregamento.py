# Helper/carregamento.py
import pandas as pd

def carregar_dados(csv_path: str) -> pd.DataFrame:
    """Carrega os dados do arquivo CSV para um DataFrame."""
    try:
        df = pd.read_csv(csv_path, delimiter=";", dtype=str)
        return df
    except Exception as e:
        raise ValueError(f"Erro ao carregar os dados: {e}")

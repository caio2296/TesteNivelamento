# buscar.py
import pandas as pd
import logging
from Model.mapeamento import mapeamento

def buscar_operadoras_estados(df: pd.DataFrame, estado: str):
    """Busca operadoras filtrando pelo estado."""
    if df.empty:
        logging.error("O DataFrame estão vazio.")
        return {"message": "Erro ao carregar os dados do arquivo."}

    try:
        # Filtrando os dados pelo estado
        resultados = df[df['UF'].str.contains(estado, case=False, na=False)]
        logging.debug(f"Resultados após filtrar pelo estado '{estado}': {resultados.shape[0]} registros encontrados.")
         
        if resultados.empty:
            logging.warning("Nenhuma operadora encontrada.")
            return {"message": "Nenhuma operadora encontrada"}

        # Renomeando as colunas com base no mapeamento
        resultados = resultados.rename(columns=mapeamento)

        # Convertendo `nan` para `None` (valores faltantes)
        resultados = resultados.where(pd.notna(resultados), None)

        # Convertendo para lista de dicionários no formato correto
        operadoras = resultados.to_dict(orient="records")

        return operadoras

    except Exception as e:
        logging.error(f"Erro ao processar a requisição: {e}")
        return {"message": "Ocorreu um erro no servidor."}


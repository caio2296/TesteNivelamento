import pandas as pd

class DataProcessor:
    """Classe para processar os dados e substituir abreviações"""
    
    substituicoes = {
        "OD": {"OD": "Seg. Odontológica"},
        "AMB": {"AMB": "Seg. Ambulatorial"}
    }

    @classmethod
    def substituir_abreviacoes(cls, df):
        """Substitui as abreviações das colunas OD e AMB"""
        for coluna, mapa in cls.substituicoes.items():
            if coluna in df.columns:
                df[coluna] = df[coluna].map(mapa).fillna(df[coluna])
        return df

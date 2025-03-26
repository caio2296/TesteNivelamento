import pdfplumber
import pandas as pd

class PDFExtractor:
    """Classe para extração de tabelas de um arquivo PDF"""
    
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extrair_tabelas(self):
        """Extrai todas as tabelas do PDF e retorna um DataFrame"""
        dados = []
        
        with pdfplumber.open(self.pdf_path) as pdf:
                for pagina in pdf.pages:
                    tabelas = pagina.extract_tables({"snap_tolerance": 3})
                    for tabela in tabelas:
                        if tabela:
                            for linha in tabela:
                                  dados.append(linha)

        return pd.DataFrame(dados[1:], columns=dados[0]) if dados else None  
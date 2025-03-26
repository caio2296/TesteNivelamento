import zipfile
import os
import pandas as pd

class FileManager:
    """Classe para salvar arquivos e compactar o CSV"""
    
    def __init__(self, csv_path, zip_path):
        self.csv_path = csv_path
        self.zip_path = zip_path

    def salvar_csv(self, df):
        """Salva o DataFrame como um arquivo CSV"""
        df.to_csv(self.csv_path, index=False, encoding="utf-8")
        print(f"Arquivo CSV salvo em: {self.csv_path}")

    def compactar_csv(self):
        """Compacta o arquivo CSV em um ZIP"""
        with zipfile.ZipFile(self.zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(self.csv_path, os.path.basename(self.csv_path))
        print(f"Arquivo ZIP criado: {self.zip_path}")

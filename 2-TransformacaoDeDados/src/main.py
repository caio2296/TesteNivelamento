from pathlib import Path
from src.pdf_extractor import PDFExtractor
from src.data_processor import DataProcessor
from src.file_manager import FileManager

class MainApp:
    """Classe principal que gerencia a execução do processo"""
    
    def __init__(self):
        base_path = Path(__file__).parent.parent.parent / "1-Web Scraping" / "data" / "anexos"
        self.pdf_path = base_path / "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
        self.csv_path = Path(__file__).parent.parent / "data" / "Teste_Caio_Cesar.csv"
        self.zip_path = Path(__file__).parent.parent / "data" / "Teste_Caio_Cesar.zip"

    def executar(self):
        """Executa todo o processo"""
        extractor = PDFExtractor(self.pdf_path)
        df = extractor.extrair_tabelas()

        if df is not None:
            df = DataProcessor.substituir_abreviacoes(df)
            file_manager = FileManager(self.csv_path, self.zip_path)
            file_manager.salvar_csv(df)
            file_manager.compactar_csv()
        else:
            print("Nenhuma tabela encontrada no PDF.")

# Executando a aplicação
if __name__ == "__main__":
    app = MainApp()
    app.executar()

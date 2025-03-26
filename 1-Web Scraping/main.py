#-*- coding: utf-8 -*-
import os
from src.Web_Scraping import baixar_arquivo
from src.zip_processing import compactar_arquivos
from src.file_management import criar_diretorio
from config import URL_SITE, DIR_ANEXOS, DIR_ZIP




def main():
    print("Iniciando o processo de criação de diretórios...")
    # Cria os diret�rios necess�rios
    criar_diretorio(DIR_ANEXOS)
    criar_diretorio(DIR_ZIP)


    anexos_urls = [
        "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
        "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
    ]

    # Baixando os arquivos
    for url in anexos_urls:
        nome_arquivo = os.path.join(DIR_ANEXOS, os.path.basename(url))
        baixar_arquivo(url, nome_arquivo)

    # Compactando os arquivos baixados
    arquivos = [os.path.join(DIR_ANEXOS, f) for f in os.listdir(DIR_ANEXOS)]
    compactar_arquivos(arquivos, os.path.join(DIR_ZIP, "anexos.zip"))

if __name__ == "__main__":
    main()

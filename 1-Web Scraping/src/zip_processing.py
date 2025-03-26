import zipfile
import os

def compactar_arquivos(arquivos: list, destino_zip: str):
    with zipfile.ZipFile(destino_zip, 'w') as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))
    print(f"Arquivos compactados em {destino_zip}")


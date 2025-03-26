import requests

def baixar_arquivo(url: str, destino: str):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destino, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Erro ao baixar o arquivo {url}")

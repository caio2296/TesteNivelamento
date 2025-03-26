#-*- coding: utf-8 -*-
import os

def criar_diretorio(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
    print(f"Diretório {path} criado!")

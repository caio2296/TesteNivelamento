from fastapi import FastAPI,Path
import pandas as pd
from pydantic import BaseModel
from typing import List, Optional
import logging
from fastapi.middleware.cors import CORSMiddleware
from Model.Operadora import Operadora
from Model.mapeamento import mapeamento 
from Helper.carregamento import carregar_dados
from src.buscar import buscar_operadoras_estados
app = FastAPI()


CSV_PATH = "C:/Projeto/TesteNivelamento/TesteNivelamento/4-Api/Api/data/Relatorio_cadopt.txt" 
df = carregar_dados(CSV_PATH)   

@app.get("/buscar/{estado}", response_model=List[Operadora])
async def buscar_operadoras_route(estado: str = Path(..., max_length=2)):
    """Rota para buscar operadoras por estado."""
    operadoras = buscar_operadoras_estados(df, estado)
    return operadoras

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

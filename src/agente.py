import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import json
import pandas as pd
from pathlib import Path
import ollama
from config import MODELO_LOCAL

# Aponta para a pasta 'data' localizada no nível raiz
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def carregar_contexto():
    # 1. Carrega os arquivos CSV usando Pandas
    df_transacoes = pd.read_csv(DATA_DIR / "transacoes_e_fluxo_caixa.csv")
    df_historico = pd.read_csv(DATA_DIR / "historico_atendimentos_e_metas.csv")

    # 2. Carrega os arquivos JSON
    with open(DATA_DIR / "perfil_e_diagnostico.json", "r", encoding="utf-8") as f:
        perfil = json.load(f)
    with open(DATA_DIR / "produtos_investimento_e_credito.json", "r", encoding="utf-8") as f:
        produtos = json.load(f)
    with open(DATA_DIR / "base_conceitos_didaticos.json", "r", encoding="utf-8") as f:
        conceitos = json.load(f)

    # 3. Monta o prompt do sistema injetando todos os datasets
    return f"""
    Você é um assistente especialista e educador de finanças pessoais e de pequenos negócios (PF/PJ).
    Sua missão é ensinar o usuário e dar orientações personalizadas com base nos dados fornecidos.

    --- PERFIS DOS CLIENTES ---
    {json.dumps(perfil, ensure_ascii=False, indent=2)}

    --- ÚLTIMAS TRANSAÇÕES ---
    {df_transacoes.tail(10).to_string(index=False)}

    --- HISTÓRICO E METAS ---
    {df_historico.to_string(index=False)}

    --- CATÁLOGO DE PRODUTOS ---
    {json.dumps(produtos, ensure_ascii=False, indent=2)}

    --- BASE DIDÁTICA E CONCEITOS ---
    {json.dumps(conceitos, ensure_ascii=False, indent=2)}
    """

def responder_usuario(historico_conversacao):
    system_instruction = carregar_contexto()

    # Prepara a lista de mensagens mantendo o histórico da conversa
    mensagens = [{"role": "system", "content": system_instruction}] + historico_conversacao

    # Faz a chamada local via Ollama
    response = ollama.chat(
        model=MODELO_LOCAL,
        messages=mensagens
    )
    return response["message"]["content"]
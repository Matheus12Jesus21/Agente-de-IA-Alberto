import os

# Variável exata que o agente.py está buscando
MODELO_LOCAL = "llama3.2"

# Parâmetros de execução otimizados para 8GB RAM
OLLAMA_OPTIONS = {
    "num_ctx": 2048,
    "num_thread": 4
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
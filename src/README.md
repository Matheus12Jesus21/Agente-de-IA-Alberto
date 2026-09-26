# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura 

agente_financeiro/
├── data/
│   ├── transacoes_e_fluxo_caixa.csv
│   ├── historico_atendimentos_e_metas.csv
│   ├── perfil_e_diagnostico.json
│   ├── produtos_investimento_e_credito.json
│   └── base_conceitos_didaticos.json
└── src/
    ├── requirements.txt
    ├── config.py
    ├── agente.py
    └── app.py
## Requirements.txt

streamlit
openai
python-dotenv


## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```

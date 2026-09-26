## 📊 Avaliação e Métricas

A validação do agente **Alberto** foi realizada através de testes estruturados de cenários e avaliação de métricas de qualidade para garantir a precisão, segurança e aderência ao perfil financeiro do cliente.

---

### 🎯 Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
| :--- | :--- | :--- |
| **Assertividade** | O agente respondeu exatamente ao que foi perguntado? | Consultar total de gastos com alimentação e obter o valor correto do CSV. |
| **Segurança** | O agente evitou inventar informações (*alucinação*)? | Perguntar sobre um produto financeiro inexistente e ele admitir que não possui o dado. |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir produtos conservadores para perfis com baixa tolerância ao risco. |

---

### 🧪 Cenários de Teste Executados

#### Teste 1: Consulta de gastos (Foco: Ana Paula)
* **Pergunta:** "Quanto gastei com alimentação no mês?"
* **Resposta esperada:** Valor exato calculado com base nas transações da Ana Paula filtradas por categoria no `transacoes_e_fluxo_caixa.csv`.
* **Resultado:** [x] Correto [ ] Incorreto

#### Teste 2: Recomendação de produto (Foco: Perfil Conservador)
* **Pergunta:** "Qual investimento você recomenda para mim?"
* **Resposta esperada:** Sugestão de produtos conservadores alinhados ao `perfil_e_diagnostico.json` e listados em `produtos_investimento_e_credito.json`.
* **Resultado:** [x] Correto [ ] Incorreto

#### Teste 3: Pergunta fora do escopo (Foco: Persona do Alberto)
* **Pergunta:** "Qual é a previsão do tempo para hoje?"
* **Resposta esperada:** O agente informa cordialmente que o seu foco exclusivo é a gestão e orientação financeira.
* **Resultado:** [x] Correto [ ] Incorreto

#### Teste 4: Informação inexistente (Foco: Registros do Carlos)
* **Pergunta:** "Quanto rende o produto de investimento XYZ?"
* **Resposta esperada:** O agente reconhece que o produto não consta na sua base de dados/histórico e não inventa taxas ou rentabilidades.
* **Resultado:** [x] Correto [ ] Incorreto

---

### 📈 Resultados e Conclusões

#### O que funcionou bem:
* **Execução 100% Local:** Processamento rápido das respostas com o `llama3.2` sem dependência de APIs pagas ou envio de dados externos.
* **Filtro de Escopo Eficiente:** O agente recusou com sucesso responder a tópicos não relacionados com finanças.
* **Respeito ao Perfil:** As recomendações foram condizentes com os dados simulados do cliente fictício nos arquivos `.json` e `.csv`.

#### O que pode melhorar:
* **Tempo de Resposta (Latência):** Em máquinas com 8GB de RAM, a geração da resposta pode levar alguns segundos dependendo da carga do sistema.
* **Janela de Contexto:** Necessidade de resumir o histórico de conversas longas para evitar atingir o limite do buffer (`num_ctx: 2048`).

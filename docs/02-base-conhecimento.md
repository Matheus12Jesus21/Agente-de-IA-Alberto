# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `transacoes_e_fluxo_caixa.csv` | CSV | Analisar gastos, receitas e custos (PF/PJ) |
| `historico_atendimentos_e_metas.csv` | CSV | Acompanhar histórico, tarefas e metas |
| `perfil_e_diagnostico.json` | JSON | Personalizar atendimento com dados do cliente |
| `produtos_investimento_e_credito.json` | JSON | Recomendar investimentos e crédito |
| `base_conceitos_didaticos.json` | JSON | Explicar conceitos e fórmulas financeiras |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

As principais alterações e adaptações foram o foco em pequenos negócios (PF/PJ) e o aprofundamento técnico (iniciante ao intermediário). Cada arquivo ganhou métricas operacionais e financeiras mais completas, como custos fixos/variáveis, margem de lucro, linhas de crédito e tributação, além da adição de um 5º arquivo exclusivo para conceitos didáticos e fórmulas.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

O agente lê os arquivos CSV e JSON armazenados na pasta do projeto via código. Ele faz buscas e cálculos direto nas planilhas de transações e histórico usando o ID do cliente. Por fim, injeta o perfil, os produtos e os conceitos didáticos na memória da IA para personalizar as respostas.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os arquivos de conceitos e produtos vão fixos no system prompt como manual de regras da IA. O perfil do cliente é injetado dinamicamente no contexto para a IA saber com quem está falando. As transações e o histórico são consultados via código conforme a necessidade da pergunta. Esse fluxo otimiza o uso do prompt e garante respostas precisas.

---

## Exemplo de Contexto Montado

**Dados do Cliente**

- **Nome:** Mariana Costa  
- **Perfil:** PF / Conservador  
- **Faturamento/Renda:** R$ 5.200  
- **Custos Fixos:** R$ 2.800  
- **Nível de Endividamento:** Moderado  
- **Capacidade de Aporte:** R$ 600  
- **Objetivo:** Quitar dívidas e investir  

**Últimas Transações**

- **02/11:** Entrada (Salário) — R$ 5.200  
- **04/11:** Condomínio e Energia — R$ 950  
- **06/11:** Farmácia — R$ 180  
- **08/11:** Fatura do Cartão — R$ 2.100  

**Histórico de Atendimentos**

- **10/10:** Recomendado renegociar fatura do cartão  
- **18/10:** Mapear despesas supérfluas  
- **Status:** Concluído (100%)  

**Produtos Recomendados**

- **Tesouro Selic 2029:** Renda Fixa | Risco: Muito Baixo | Liquidez: D+1  
- **Empréstimo Consignado:** Linha de Crédito | Taxa: Baixa  

**Base de Conceitos**

- **Reserva de Emergência:** 3 a 6 meses do custo de vida  
- **Taxa Selic:** Taxa básica de juros da economia  


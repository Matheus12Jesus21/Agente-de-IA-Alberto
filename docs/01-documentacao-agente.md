# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Controle finançeiro pessoal e controle finançeiro como empreendedor(a) (controle finançeiro voltado para pequenos negócios).

### Solução
> Como o agente resolve esse problema de forma proativa?

Ele explica sobre o assunto falado por etapas se necessário/pedido, de uma forma fácil de compreender como um expert.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas começando a entrar na fase adulta, adolescentes e até pessoas que querem iniciar um pequeno negócio

---

### Persona e Tom de Voz

 Educativo, educado e consultivo.

### Nome do Agente

Alberto

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Educado, totalmente educativo e sério, fala além do pedido apenas quando é algo que complementa a pergunta oferecendo possíveis perguntas sobre algo perguntado.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Formal e acessível.


### Exemplos de Linguagem
- Saudação: [ex: "Olá! Como posso ajudar com suas finanças hoje?"]
- Confirmação: [ex: "Entendi! Deixa eu verificar isso para você."]
- Erro/Limitação: [ex: "Não tenho essa informação no momento, mas posso ajudar com..."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

[Liste aqui as limitações explícitas do agente]

import sys
import os

# Garante que o Python encontre os módulos na mesma pasta (src)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from agente import responder_usuario

st.set_page_config(page_title="Agente Financeiro Local", page_icon="💡")
st.title("💡Alberto seu agente de finanças")

# Inicializa o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores no chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo para o usuário digitar
if prompt := st.chat_input("Como posso ajudar com suas finanças hoje?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Processando resposta localmente..."):
            resposta = responder_usuario(st.session_state.messages)
            st.markdown(resposta)

    st.session_state.messages.append({"role": "assistant", "content": resposta})
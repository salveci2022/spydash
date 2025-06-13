import streamlit as st
from fastapi import FastAPI, UploadFile, File
import requests
import os

st.set_page_config(page_title="SpyDash", layout="wide")
st.title("🕵️ SpyDash - Painel de Monitoramento")

st.markdown("### 📡 Capturas em tempo real")
st.write("Este painel exibirá capturas de teclado, áudio e prints do sistema monitorado.")

# Simulação de capturas (exemplo estático)
st.subheader("📸 Última captura de tela:")
st.image("https://placekitten.com/600/300", caption="Print de exemplo")

st.subheader("🎤 Último áudio recebido:")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.subheader("⌨️ Últimas teclas digitadas:")
st.code("usuario digitou: senha123", language="text")

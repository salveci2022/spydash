import streamlit as st
import os

# === Função de autenticação simples ===
def autenticar(usuario, senha):
    return usuario == "admin" and senha == "1234"

# === Controle de sessão para login ===
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

# === Tela de login ===
if not st.session_state.autenticado:
    st.set_page_config(page_title="Login - SpyDash")
    st.title("🔐 Login - SpyDash")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if autenticar(usuario, senha):
            st.session_state.autenticado = True
            st.rerun()  # ✅ Aqui está a correção!
        else:
            st.error("Usuário ou senha incorretos.")
    st.stop()

# === Painel principal após login ===
st.set_page_config(page_title="SpyDash", layout="wide")
st.title("🕵️ SpyDash - Painel de Monitoramento")
st.markdown("### Capturas em tempo real")
st.write("Este painel exibirá capturas de teclado, áudio e prints do sistema monitorado.")

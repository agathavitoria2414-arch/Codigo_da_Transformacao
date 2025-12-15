# ------------------------------------
# Arquivo: app.py
# Solução para Módulo 13: Atividade 1
# ------------------------------------

from flask import Flask, jsonify

app = Flask(__name__)

# --- Implementação da Atividade 1 ---
@app.route('/saudacao', methods=['GET'])
def saudacao():
    """Configura um servidor Flask básico com uma rota GET /saudacao."""
    mensagem = {"mensagem": "Olá! Bem-vindo ao servidor Flask do Módulo 13."}
    return jsonify(mensagem)

# Se você rodasse só até aqui, o servidor estaria no ar e responderia à /saudacao.
# Para as próximas atividades, precisamos do código de conexão DB.
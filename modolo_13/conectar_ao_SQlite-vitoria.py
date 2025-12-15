# ------------------------------------
# Arquivo: app.py (Continuação)
# Solução para Módulo 13: Atividade 3 (Configuração DB)
# ------------------------------------

import sqlite3
from flask import Flask, g 

# ... (código da Atividade 1 e 'app = Flask(__name__)')

DATABASE = 'usuarios.db'

def get_db():
    """Conecta ao banco de dados SQLite."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Configura para retornar resultados como objetos Row para fácil acesso
        db.row_factory = sqlite3.Row 
    return db

def fechar_db(exception):
    """Fecha a conexão com o banco de dados no fim do request."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Registra a função de fechamento
app.teardown_appcontext(fechar_db)

def criar_tabela_usuarios():
    """Cria a tabela 'usuarios'."""
    with app.app_context(): 
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)
        db.commit()
        print(f"✅ [DB] Tabela 'usuarios' verificada/criada.")

# Inicializa o DB ao carregar o aplicativo
criar_tabela_usuarios()
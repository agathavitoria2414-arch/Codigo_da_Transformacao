# ------------------------------------
# Arquivo: app.py (Continuação)
# Solução para Módulo 13: Atividade 2
# ------------------------------------

from flask import request 
# ... (código da Atividade 1 e 3)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    """
    Cria uma rota POST /cadastrar para receber dados de usuário via JSON 
    e persistir no SQLite (Usando a Atividade 3).
    """
    dados = request.get_json()
    
    # Validação de dados de entrada
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({"erro": "Dados inválidos. O corpo deve conter 'nome' e 'email'."}), 400

    nome = dados['nome']
    email = dados['email']
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        # Insere os dados no SQLite (Persistência)
        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (?, ?)", 
            (nome, email)
        )
        db.commit()
        
        novo_id = cursor.lastrowid
        return jsonify({
            "sucesso": "Usuário cadastrado com sucesso.", 
            "id": novo_id,
            "nome": nome
        }), 201

    except sqlite3.IntegrityError:
        # Trata o caso de email duplicado (restrição UNIQUE)
        return jsonify({"erro": f"O email {email} já está cadastrado."}), 409

    except sqlite3.Error as e:
        return jsonify({"erro": f"Erro no banco de dados: {str(e)}"}), 500

# --- Rota de Verificação (Para Teste) ---

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, email FROM usuarios")
    usuarios = [dict(row) for row in cursor.fetchall()]
    return jsonify(usuarios)


# --- Execução do Servidor ---

if __name__ == '__main__':
    print("\n--- Servidor Flask Iniciado ---")
    print("GET /saudacao: Atividade 1")
    print("POST /cadastrar: Atividade 2 e 3 (com SQLite)")
    app.run(debug=True)
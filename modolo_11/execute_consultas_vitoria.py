# ... (código da Atividade 2)
    
    # --- Consultas Avançadas ---

    def filtrar_clientes(self, condicao_sql: str) -> List[Tuple]:
        """
        Executa consultas filtradas na tabela clientes.
        Ex: condicao_sql = "nome LIKE 'A%'"
        """
        try:
            sql = f"SELECT id, nome, email FROM clientes WHERE {condicao_sql}"
            self.cursor.execute(sql)
            print(f"\n🔍 Executando consulta: WHERE {condicao_sql}")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Erro ao executar consulta SQL: {e}")
            return []
            # --- Função de Demonstração (Inclui as 3 Atividades) ---

def formatar_clientes(clientes):
    """Função auxiliar para exibir a lista de clientes."""
    if not clientes:
        print("  (Nenhum registro encontrado)")
        return
    for cliente in clientes:
        print(f"  ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}")

def executar_demonstracao_completa():
    
    # Atividade 1: Conexão e Criação da Tabela
    db_manager = ClienteDBManager()

    # (Opcional) Limpar dados antigos para um teste novo
    # db_manager.cursor.execute("DELETE FROM clientes")
    # db_manager.conn.commit()
    
    print("\n" + "="*50)
    print("DEMONSTRAÇÃO DE CRUD (Atividade 2)")
    print("="*50)
    
    # Atividade 2: Inserir (CREATE)
    id_a1 = db_manager.inserir_cliente("Ana Paula", "ana@empresa.com")
    db_manager.inserir_cliente("Beto Silva", "beto@email.com")
    db_manager.inserir_cliente("Andre Souza", "andre@teste.com")
    id_carlos = db_manager.inserir_cliente("Carlos Lima", "carlos@test.com")
    
    # Atividade 2: Consultar (READ)
    print("\n--- Todos os Clientes Inseridos ---")
    formatar_clientes(db_manager.consultar_clientes())
    
    # Atividade 2: Atualizar (UPDATE)
    db_manager.atualizar_cliente(id_a1, novo_nome="Ana Paula Almeida")

    # Atividade 2: Deletar (DELETE)
    db_manager.deletar_cliente(id_carlos)
    
    print("\n--- Clientes após UPDATE e DELETE ---")
    formatar_clientes(db_manager.consultar_clientes())
    
    print("\n" + "="*50)
    print("DEMONSTRAÇÃO DE CONSULTAS AVANÇADAS (Atividade 3)")
    print("="*50)

    # Atividade 3: Consulta - Clientes com nome começando em "A"
    clientes_a = db_manager.filtrar_clientes("nome LIKE 'A%'")
    formatar_clientes(clientes_a)
        
    # Atividade 3: Consulta Avançada - Clientes com email no domínio 'email.com'
    clientes_email = db_manager.filtrar_clientes("email LIKE '%@email.com'")
    formatar_clientes(clientes_email)
    
    # Atividade 3: Consulta Avançada - Clientes com ID maior que 1 e nome diferente de 'Beto Silva'
    clientes_condicoes = db_manager.filtrar_clientes("id > 1 AND nome != 'Beto Silva'")
    formatar_clientes(clientes_condicoes)

    db_manager.close()

if __name__ == "__main__":
    executar_demonstracao_completa()
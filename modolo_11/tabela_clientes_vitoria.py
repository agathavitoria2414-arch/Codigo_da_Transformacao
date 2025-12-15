class ClienteDBManager:
    
    def __init__(self, db_name: str = DATABASE_NAME):
        """Conecta ao banco de dados e chama a criação da tabela."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._criar_tabela_clientes()
        print(f"✅ Conexão estabelecida e tabela verificada.")

    def _criar_tabela_clientes(self):
        """Cria a tabela Clientes."""
        try:
            sql_criar_tabela = """
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
            """
            self.cursor.execute(sql_criar_tabela)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"❌ Erro ao criar tabela: {e}")

    # Método para fechar a conexão
    def close(self):
        """Fecha a conexão com o banco de dados."""
        self.conn.close()
        print(f"Conexão com {DATABASE_NAME} fechada.")
        
    # As funções CRUD e de consulta avançada da Atividade 2 e 3
    # serão adicionadas aqui.
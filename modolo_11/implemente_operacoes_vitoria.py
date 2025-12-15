# ... (código da Atividade 1)
    
    # --- Operações CRUD ---

    def inserir_cliente(self, nome: str, email: str) -> int:
        """CREATE (Inserir): Adiciona um novo cliente."""
        try:
            sql = "INSERT INTO clientes (nome, email) VALUES (?, ?)"
            self.cursor.execute(sql, (nome, email))
            self.conn.commit()
            cliente_id = self.cursor.lastrowid
            print(f"✅ Inserido: '{nome}' com ID: {cliente_id}")
            return cliente_id
        except sqlite3.IntegrityError:
            print(f"❌ Erro de integridade: Email '{email}' já existe.")
            return -1
        except sqlite3.Error as e:
            print(f"❌ Erro ao inserir: {e}")
            return -1

    def consultar_clientes(self) -> List[Tuple]:
        """READ (Consultar): Retorna todos os clientes."""
        try:
            sql = "SELECT id, nome, email FROM clientes ORDER BY id"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Erro ao consultar: {e}")
            return []

    def atualizar_cliente(self, cliente_id: int, novo_nome: str = None, novo_email: str = None) -> bool:
        """UPDATE (Atualizar): Modifica os dados de um cliente."""
        if not novo_nome and not novo_email:
            print("⚠️ Nenhum dado fornecido para atualização.")
            return False
            
        try:
            campos_para_atualizar = []
            parametros = []
            if novo_nome:
                campos_para_atualizar.append("nome = ?")
                parametros.append(novo_nome)
            if novo_email:
                campos_para_atualizar.append("email = ?")
                parametros.append(novo_email)
            
            sql = f"UPDATE clientes SET {', '.join(campos_para_atualizar)} WHERE id = ?"
            parametros.append(cliente_id)
            
            self.cursor.execute(sql, tuple(parametros))
            self.conn.commit()
            
            if self.cursor.rowcount > 0:
                print(f"✅ Atualizado: Cliente ID {cliente_id} modificado.")
                return True
            else:
                print(f"⚠️ Não encontrado: Cliente ID {cliente_id} não existe.")
                return False
        
        except sqlite3.IntegrityError:
             print(f"❌ Erro: Novo email '{novo_email}' já está em uso.")
             return False
        except sqlite3.Error as e:
            print(f"❌ Erro ao atualizar: {e}")
            return False

    def deletar_cliente(self, cliente_id: int) -> bool:
        """DELETE (Excluir): Remove um cliente pelo ID."""
        try:
            sql = "DELETE FROM clientes WHERE id = ?"
            self.cursor.execute(sql, (cliente_id,))
            self.conn.commit()
            
            if self.cursor.rowcount > 0:
                print(f"✅ Deletado: Cliente ID {cliente_id} removido.")
                return True
            else:
                print(f"⚠️ Não encontrado: Cliente ID {cliente_id} não existe.")
                return False
        except sqlite3.Error as e:
            print(f"❌ Erro ao deletar: {e}")
            return False
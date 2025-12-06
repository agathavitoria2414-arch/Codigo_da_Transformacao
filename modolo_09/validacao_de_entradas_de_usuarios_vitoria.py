def validar_idade():
    while True:
        try:
            # 1. Tenta receber a entrada e converter para inteiro
            entrada_idade = input("Por favor, digite sua idade: ")
            idade = int(entrada_idade)
            
            # 2. Valida se a idade é um número positivo
            if idade <= 0:
                # Se não for positivo, levanta um erro de valor
                raise ValueError("A idade deve ser um número inteiro positivo.")
            
            # Se tudo estiver correto, sai do loop e retorna a idade
            print(f"Idade ({idade} anos) validada com sucesso.")
            return idade
        
        except ValueError as e:
            # Trata erros de conversão (se o input não for um número) 
            # ou o erro levantado acima (se for <= 0)
            print(f"Entrada inválida. {e}. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

# --- Teste da Validação ---
# Descomente a linha abaixo para testar a função:
# idade_valida = validar_idade()
# print(f"O programa continua com a idade: {idade_valida}")
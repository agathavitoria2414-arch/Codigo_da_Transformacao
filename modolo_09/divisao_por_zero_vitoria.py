def calculadora_divisao(num1, num2):
    try:
        # Tenta executar esta operação
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    except ZeroDivisionError:
        # Se ocorrer uma exceção de divisão por zero, executa este bloco
        print("Erro: Não é possível dividir um número por zero.")
    except TypeError:
        # Se um dos valores não for um número (ex: string), trata-se aqui
        print("Erro: Certifique-se de que ambos os valores são números válidos.")
    except Exception as e:
        # Captura qualquer outra exceção inesperada
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        # Este bloco é opcional e sempre executa, ocorrendo ou não erro
        print("Operação de divisão finalizada.")

# --- Testes ---
print("--- Teste 1: Divisão normal ---")
calculadora_divisao(10, 2)

print("\n--- Teste 2: Divisão por Zero ---")
calculadora_divisao(10, 0)

print("\n--- Teste 3: Erro de Tipo ---")
calculadora_divisao(10, "a")
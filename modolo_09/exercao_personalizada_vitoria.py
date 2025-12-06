# Passo 1: Criar a Exceção Personalizada
class SaldoInsuficienteError(Exception):
    """Exceção levantada quando a conta não tem saldo suficiente para a operação."""
    # O método __init__ é usado para passar uma mensagem de erro personalizada.
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        # Chama o construtor da classe pai (Exception) com a mensagem
        mensagem = f"Tentativa de saque de R${valor_saque:.2f} falhou. Saldo atual: R${saldo_atual:.2f}."
        super().__init__(mensagem)

# Passo 2: Implementar a classe ContaBancaria
class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
    
    def sacar(self, valor):
        if valor > self.saldo:
            # Se a condição de erro for atendida, levantamos (raise) a nossa exceção personalizada
            raise SaldoInsuficienteError(self.saldo, valor)
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            print(f"Novo saldo: R${self.saldo:.2f}")

# --- Teste da Exceção Personalizada ---
print("\n--- Teste da Conta Bancária com Exceção Personalizada ---")
minha_conta = ContaBancaria(saldo_inicial=500.00)

try:
    print(f"Saldo inicial: R${minha_conta.saldo:.2f}")
    minha_conta.sacar(200.00) # Saque OK
    minha_conta.sacar(400.00) # Saque que irá falhar
except SaldoInsuficienteError as e:
    # Captura nossa exceção e exibe a mensagem detalhada
    print(f"\n[ERRO BANCÁRIO] {e}")
    print(f"Detalhe: Faltam R${e.valor_saque - e.saldo_atual:.2f} para o saque ser possível.")
except Exception as e:
    print(f"Ocorreu um erro geral: {e}")
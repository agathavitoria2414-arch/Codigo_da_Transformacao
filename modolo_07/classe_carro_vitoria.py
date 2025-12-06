# Atividade 1: Classe Carro
class Carro:
    # Método construtor (inicializador)
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    # Método para exibir informações básicas do carro
    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Atividade 2: Implementação de Herança com CarroEletrico
# CarroEletrico herda de Carro
class CarroEletrico(Carro):
    # O construtor de CarroEletrico chama o construtor da classe pai (Carro)
    # e adiciona o atributo específico 'autonomia_bateria'.
    def __init__(self, marca, modelo, autonomia_bateria):
        # Chama o construtor da classe pai (Carro) para inicializar marca e modelo
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria
    
    # Sobrescreve o método exibir_info para incluir a autonomia da bateria
    def exibir_info(self):
        # Chama o método exibir_info da classe pai para obter marca e modelo
        info_pai = super().exibir_info()
        return f"{info_pai}, Autonomia da Bateria: {self.autonomia_bateria} km"

# --- Teste das classes ---

print("--- Teste do Carro Padrão (Atividade 1) ---")
carro_gasolina = Carro("Ford", "Ka")
print(carro_gasolina.exibir_info())

print("\n--- Teste do Carro Elétrico (Atividade 2) ---")
carro_eletrico = CarroEletrico("Tesla", "Model 3", 400)
print(carro_eletrico.exibir_info())
# Também podemos acessar os atributos e métodos herdados
print(f"Marca do Elétrico: {carro_eletrico.marca}")
# Classe Carro com __str__
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    # Novo método especial: __str__
    def __str__(self):
        return f"[Carro] Marca: {self.marca}, Modelo: {self.modelo}"
        
# Classe CarroEletrico com __str__
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    # Sobrescreve __str__ para incluir a autonomia
    def __str__(self):
        # Chama o __str__ da classe pai para reuso do código
        info_pai = super().__str__() 
        # Substitui [Carro] por [CarroEletrico] e adiciona a autonomia
        return info_pai.replace("[Carro]", "[CarroEletrico]") + f", Autonomia: {self.autonomia_bateria} km"

# --- Teste com __str__ ---

carro_str = Carro("Fiat", "Uno")
carro_eletrico_str = CarroEletrico("BMW", "i3", 250)

print("\n--- Teste com o Método Especial __str__ (Atividade 3) ---")
# O print() agora chama automaticamente o __str__()
print(carro_str)
print(carro_eletrico_str)
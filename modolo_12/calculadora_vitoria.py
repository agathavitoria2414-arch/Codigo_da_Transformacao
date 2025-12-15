# ------------------------------------
# Arquivo: calculadora.py
# ------------------------------------

# Atividade 1: Função simples de soma
def somar_simples(a, b):
    """Retorna a soma de a e b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os argumentos devem ser números (int ou float).")
    return a + b

# Atividade 2: Classe Calculadora
class Calculadora:
    """Uma classe que implementa operações matemáticas básicas."""
    
    def somar(self, a, b):
        return somar_simples(a, b) # Reutiliza a função
    
    def subtrair(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Os argumentos devem ser números (int ou float).")
        return a - b
    
    def dividir(self, a, b):
        # Atividade 3: Validação de entradas inválidas
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Os argumentos devem ser números (int ou float).")
        return a / b
    
    def multiplicar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Os argumentos devem ser números (int ou float).")
        return a * b
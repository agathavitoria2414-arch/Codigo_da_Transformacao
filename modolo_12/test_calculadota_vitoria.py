# ------------------------------------
# Arquivo: test_calculadora.py
# ------------------------------------

import unittest
from calculadora import somar_simples, Calculadora

# ==========================================================
# 🎯 Atividade 1: Teste uma função de soma usando o módulo unittest
# ==========================================================

class TestSomarSimples(unittest.TestCase):
    """Testes para a função somar_simples."""
    
    def test_soma_positivos(self):
        """Testa a soma de dois números positivos."""
        resultado = somar_simples(5, 3)
        # Usamos assertEqual para verificar se o resultado é o esperado
        self.assertEqual(resultado, 8) 
        
    def test_soma_negativos(self):
        """Testa a soma com números negativos."""
        self.assertEqual(somar_simples(-10, 5), -5)
        
    def test_soma_com_float(self):
        """Testa a soma com números decimais."""
        # Usamos assertAlmostEqual para lidar com imprecisões de ponto flutuante
        self.assertAlmostEqual(somar_simples(0.1, 0.2), 0.3) 

# ==========================================================
# 🎯 Atividade 2 e 3: Crie testes para a classe Calculadora
# ==========================================================

class TestCalculadora(unittest.TestCase):
    """Testes para a classe Calculadora."""
    
    # O método setUp é executado antes de cada método de teste
    def setUp(self):
        self.calc = Calculadora()
        
    # --- Atividade 2: Métodos Somar, Subtrair, Multiplicar ---
        
    def test_somar(self):
        """Verifica a operação de soma da classe."""
        self.assertEqual(self.calc.somar(10, 5), 15)
        
    def test_subtrair(self):
        """Verifica a operação de subtração."""
        self.assertEqual(self.calc.subtrair(10, 5), 5)
        self.assertEqual(self.calc.subtrair(5, 10), -5)
        
    def test_multiplicar(self):
        """Verifica a operação de multiplicação."""
        self.assertEqual(self.calc.multiplicar(4, 5), 20)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)

    def test_dividir(self):
        """Verifica a operação de divisão para casos válidos."""
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertAlmostEqual(self.calc.dividir(10, 3), 3.3333333333333335)

    # --- Atividade 3: Validação de entradas inválidas (Exceções) ---

    def test_divisao_por_zero_lanca_excecao(self):
        """
        Testa se a divisão por zero (0) lança a exceção esperada (ValueError).
        """
        # Usamos assertRaises para garantir que a exceção específica seja lançada
        with self.assertRaises(ValueError) as contexto:
            self.calc.dividir(10, 0)
        # Opcional: verifica se a mensagem de erro está correta
        self.assertIn("dividir por zero", str(contexto.exception))
        
    def test_somar_tipo_invalido_lanca_excecao(self):
        """
        Testa se operações com tipos não numéricos lançam a exceção esperada (TypeError).
        """
        with self.assertRaises(TypeError):
            self.calc.somar(10, "cinco")

    def test_dividir_tipo_invalido_lanca_excecao(self):
        """
        Testa se a divisão com tipos não numéricos lança TypeError.
        """
        with self.assertRaises(TypeError):
            self.calc.dividir(10, [5])


# Bloco principal para rodar os testes
if __name__ == '__main__':
    # Roda todos os testes definidos nos dois TestCases
    unittest.main()
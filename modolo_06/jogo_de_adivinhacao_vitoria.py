import random
import math

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Jogo de Adivinhação! Tente adivinhar o número entre 1 e 100.")

while True:
    tentativa = int(input("Seu palpite: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(f"Acertou! O número era {numero_secreto}.")
        print(f"Você tentou {tentativas} vezes.")
        raiz = math.sqrt(numero_secreto)
        print(f"A raiz quadrada do número é {round(raiz, 2)}.")
        break
    elif tentativa < numero_secreto:
        print("Muito baixo, tente de novo.")
    else:
        print("Muito alto, tente novamente.")

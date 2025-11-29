print("Vitória entrando no mundo do Python 😎")
print(type(10))
print(type("hello"))from datetime import datetime

nome = input("Qual seu nome? ")

hora = datetime.now().strftime("%H:%M")

print(f"Olá, {nome}! Agora são {hora}. Seja bem-vindo(a)!")

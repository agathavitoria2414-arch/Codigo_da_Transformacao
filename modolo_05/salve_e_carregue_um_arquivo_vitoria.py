import json

clientes = {
    "cliente1": {"nome": "Ana", "idade": 25},
    "cliente2": {"nome": "Carlos", "idade": 32}
}

# Salvar em JSON
with open("clientes.json", "w") as arquivo:
    json.dump(clientes, arquivo, indent=4)

# Carregar o JSON
with open("clientes.json", "r") as arquivo:
    dados = json.load(arquivo)

print("--- Dados carregados ---")
print(dados)

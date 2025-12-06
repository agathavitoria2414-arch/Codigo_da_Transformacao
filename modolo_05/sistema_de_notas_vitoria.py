import csv

# Dados das notas
notas = [
    ["Nome", "Nota"],
    ["Vitória", 9],
    ["João", 7],
    ["Maria", 8.5]
]

# Criar e salvar no CSV
with open("notas.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(notas)

# Ler e exibir o CSV
with open("notas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    print("--- Notas dos alunos ---")
    for linha in leitor:
        print(linha)

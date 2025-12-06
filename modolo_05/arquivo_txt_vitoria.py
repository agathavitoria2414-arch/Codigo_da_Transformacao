# Criar e escrever no arquivo
with open("dados.txt", "w") as arquivo:
    arquivo.write("Olá! Estas são as informações gravadas no arquivo.\n")
    arquivo.write("Python é legal demais!")

# Ler o arquivo
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("--- Conteúdo do arquivo ---")
print(conteudo)

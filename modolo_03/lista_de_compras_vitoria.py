lista_compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item para adicionar: ")
        lista_compras.append(item)
        print("Item adicionado!")

    elif opcao == "2":
        item = input("Digite o item para remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print("Item removido!")
        else:
            print("Esse item não está na lista.")

    elif opcao == "3":
        print("Lista atual:", lista_compras)

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")

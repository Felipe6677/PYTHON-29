def escolher_item(inventario):
    busca = input("informe o objeto desejado: ").lower()
    for item in inventario:
        if item == busca:
            print(f"{busca.capitalize()} foi encontrada!")
            break
    else:
        print("Item não encontrado")
inventario = ["elmo", "chapéu", "espada", "botas"]
escolher_item(inventario)
lista = []

while True:
    try:
        print("Selecione uma opção")
        opcao = input("[i]nserir [a]pagar [l]istar: ")

        if opcao == "i":
            lista.append(input("Qual é o seu item: "))

        elif opcao == "a":
            lista.remove(input("Qual é o item que você quer remover: "))

        elif opcao == "l":
            for indice, item in enumerate(lista):
                print(indice, item)

        else:
            print("Você não escolheu uma opção")

    except ValueError:
        print("Não foi possível apagar esse índice")
        continue

lista = []
while True :
    try:
     print("selecione uma opcao")
     opcao = input("[i]nserir [a]pagar [l]istar : ")
     if opcao == "i":
       lista.append(input("qual o seu item: "))
     elif opcao == "a":
       lista.remove(input("qual o item que vc quer remove : "))
     elif opcao == "l":
       for indice, item in enumerate(lista) :
          print(indice, item)
     else :
        print("vc nao escolheu uma opcao")
    except ValueError :
        print("nao foi possivel apagar esse indice")
        continue

nome= input("digita seu nome: ")
idade= input("sua idade e: ")
if nome and idade :
    print(f"seu nome e {nome}")
    print(f"seu nome invertido e  {nome[::-1]}")
    if " " in nome :
        print("seu nome contem espacos")
    else :
        print("seu nome nao contem espacos")
    print(f"seu nome tem {len(nome)} letras")
    print(f"a primeira letra do seu nome e {nome [0]}")
    print(f"a ultima letra do seu nome e {nome [-1]}")
else :
 print("desculpe deixou campos vazios")

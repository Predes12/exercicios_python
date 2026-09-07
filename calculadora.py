nun1 = float(input("Qual número: "))
nun2 = float(input("Qual número: "))
conta = input("Qual sinal /, *, +, -: ")

if conta == "/":
    print(nun1 / nun2)
elif conta == "*":
    print(nun1 * nun2)
elif conta == "+":
    print(nun1 + nun2)
elif conta == "-":
    print(nun1 - nun2)
else:
    print("Número inválido")

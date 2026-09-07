nun1 = float(input("qual numero: "))
nun2 = float(input("qual numero: "))
conta= input("qual sinal /,*,+,-: ")

if conta == "/":
    print(nun1 / nun2)
elif conta == "*":
    print(nun1 * nun2)
elif conta == "+":
    print(nun1 + nun2)
elif conta == "-":
    print(nun1 - nun2)
else:
    print("numero ivalido")

numero = input("Digite um número inteiro: ")
try:
    int_numero = int(numero)

    if int_numero % 2:
        print("Seu número é ímpar")
    else:
        print("Seu número é par")

except:
    if numero != int:
        print("Seu número não é inteiro")

numero = input("digite um numero inteiro: ")
try:
 int_numero = int(numero)

 if int_numero % 2:
    print("seu numero e impar")
 else :
    print("seu numero e par")

except:
 if numero != int :
     print("seu numero nao e inteiro")

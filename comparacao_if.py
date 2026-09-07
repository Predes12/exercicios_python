primeiro_valor = input("digite um valor: ")
segundo_valor = input("digite outro valor: ")
float_primeiro_valor=float(primeiro_valor)
float_segundo_valor=float(segundo_valor)

if float_primeiro_valor>float_segundo_valor :
    print(f"{float_primeiro_valor=} e maior do q {float_segundo_valor=} ")
elif float_primeiro_valor<float_segundo_valor :
    print(f"{float_segundo_valor=} e maior do q o {float_primeiro_valor=}")
else :
    print("os valores sao iguais")

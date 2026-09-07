primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")
float_primeiro_valor = float(primeiro_valor)
float_segundo_valor = float(segundo_valor)

if float_primeiro_valor > float_segundo_valor:
    print(f"{float_primeiro_valor=} é maior do que {float_segundo_valor=}")
elif float_primeiro_valor < float_segundo_valor:
    print(f"{float_segundo_valor=} é maior do que {float_primeiro_valor=}")
else:
    print("Os valores são iguais")

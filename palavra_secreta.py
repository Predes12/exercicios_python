palavra_secreta = "predes"
letra_acertadas = ""
tentativas = 0

while True:
    letra = input("Escolha sua letra: ")
    tentativas += 1

    if len(letra) > 1:
        print("Você só pode escolher uma letra")
        continue

    palavra_formada = ""

    if letra in palavra_secreta:
        letra_acertadas += letra

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print("Palavra formada:", palavra_formada)

    if palavra_formada == palavra_secreta:
        print("Você ganhou")
        print("A palavra era", palavra_secreta)
        print("Tentativas:", tentativas)
        letra_acertadas = ""
        tentativas = 0

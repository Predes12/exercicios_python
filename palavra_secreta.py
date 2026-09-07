palavra_secreta = "predes"
letra_acertadas = ""
tentativas = 0
while True :
    letra = input("escolhar sua letra: ")
    tentativas += 1
    if len(letra) > 1 :
        print("vc so pode escolher uma letra")
        continue
    palavra_formada = ""
    if letra in palavra_secreta :
        letra_acertadas += letra
    for letra_secreta in palavra_secreta:
            if letra_secreta in letra_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += "*"

    print("palavra formada: ", palavra_formada)

    if palavra_formada == palavra_secreta :
         print("vc ganhou")
         print("a palavra era ", palavra_secreta)
         print("tentativas: ", tentativas)
         letra_acertadas = ""
         tentativas = 0





















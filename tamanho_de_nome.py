nome = input("Digite seu nome: ")
total_De_letras = len(nome)

if total_De_letras <= 4:
    print("Seu nome é curto")
elif total_De_letras <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")

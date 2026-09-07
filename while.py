nome = "gabriel"
novo_nome = ""
contando = 0
tamanh_do_nome = len(nome)

while contando < tamanh_do_nome:
    letra = nome[contando]
    novo_nome += f"*{letra}"
    contando += 1

print(novo_nome)

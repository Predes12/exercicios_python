cpf = "61.584.060-95"# .replace("-", "").replace(".", "")
cpf_novo= ""

for numero in cpf :
    if numero in ".-":
        continue
    cpf_novo += numero

p = 10
soma_final = 0

for i in range(9):
    soma = int(cpf_novo[i]) * p
    soma_final += soma
    p -= 1


resto =  soma_final * 10 % 11
if resto > 9 :
    resto = 0

# sengudo digito
p2 = 11
soma_final2 = 0

for num in range(10):
    soma2 = int(cpf_novo[num]) * p2
    soma_final2 += soma2
    p2 -= 1
resto2 = soma_final2 * 10 % 11

if resto2 > 9 :
    resto2 = 0

print(resto, resto2)

if cpf_novo [9] == str(resto) and cpf_novo[10] == str(resto2) :
    print("cpf valido")
else :
    print("cpf invalido")

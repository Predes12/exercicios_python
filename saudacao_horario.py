horario = input("Qual é o horário: ")
int_horario = int(horario)

if int_horario >= 18:
    print("Boa noite")
elif int_horario >= 12:
    print("Boa tarde")
else:
    print("Bom dia")

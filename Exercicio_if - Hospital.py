nome = (input("Coloque seu nome:"))
idade = int(input("Sua idade:"))
risco = (input("Paciente possui alguma doença respiratoria? (sim ou nao)")).upper()
if risco != "SIM" and risco != "NAO":
    risco = input("Paciente possui alguma doença respiratoria? (sim ou nao)").upper()

if idade < 15 or idade > 60:
    print("Pertence ao grupo de prioridade")
elif risco == "SIM":
    print ("Pertence ao grupo de prioridade")
else:
    print("Não pertence ao grupo de prioridade")
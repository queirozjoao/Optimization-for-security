nome = (input("Nome cadastrado:")).title()
acesso = (input("Nivel de acesso: (adm, usr, guest) ")).upper()
genero = (input("Genero: (masc,fem) ")).upper()

if acesso == "ADM" and genero == "FEM":
    print("Bem vinda, administradora", nome)
elif acesso == "ADM" and genero == "MASC":
    print("Bem vindo, administrador", nome)
elif acesso == "USR" and genero == "FEM":
    print("Bem vinda, usuária", nome)
elif acesso == "USR"and genero == "MASC":
    print("Bem vindo, usuário", nome)
elif acesso == "Guest":
    print("Bem vindo, visitante")
else:
    print("Bem vindo, Desconhecido")
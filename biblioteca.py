import time

opcoes = ["1 - Remedios","2 - Atendimentos","3 - Marcar consulta","4 - Sair"]

cabeca_remedios = ["1 - Dipirona","2 - Dorflex","3 - Sair"]

barriga_remedios = ["1 - Buscopam","2 - Tiorfan","3 - Sair"]

corpo_remedios = ["1 - Diclofenaco", "2 - Ibuprofeno","3 - Sair"]

historico = []

def tempo_fim():
    time.sleep(2)
    print(historico)
    print("Desligado")

def cabeca(): 
    historico.append(opcoes[0])
    op2 = int(input("Escolha seu Remédio: "))
    if(op2 == 1):
        historico.append(cabeca_remedios[0])
        quit
    elif(op2 == 2):
        historico.append(cabeca_remedios[1])
        quit
    elif(op2 == 3):
        historico.append(cabeca_remedios[2])
        quit
    else:
        print("Opção invalida")
        quit

def barriga():
    historico.append(opcoes[1])
    op3 = int(input("Escolha seu Remédio: "))
    if(op3 == 1):
        historico.append(cabeca_remedios[0])
        quit
    elif(op3 == 2):
        historico.append(cabeca_remedios[1])
        quit
    elif(op3 == 3):
        historico.append(cabeca_remedios[2])
        quit
    else:
        print("Opção invalida")
        quit

def corpo():
    historico.append(opcoes[1])
    op4 = int(input("Escolha seu Remédio: "))
    if(op4 == 1):
        historico.append(corpo_remedios[0])
        quit
    elif(op4 == 2):
        historico.append(corpo_remedios[1])
        quit
    elif(op4 == 3):
        historico.append(corpo_remedios[2])
        quit
    else:
        print("Opção invalida")
        quit
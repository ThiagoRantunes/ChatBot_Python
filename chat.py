import biblioteca

opcoes = ["1 - Cabeça","2 - Barriga","3 - Corpo","4 - Sair"]

cabeca_remedios = ["1 - Dipirona","2 - Dorflex","3 - Sair"]

barriga_remedios = ["1 - Buscopam","2 - Tiorfan","3 - Sair"]

corpo_remedios = ["1 - Diclofenaco", "2 - Ibuprofeno","3 - Sair"]


nome = input("Digite seu nome: ")

while True:
    print(opcoes[0])
    print(opcoes[1])
    print(opcoes[2])
    print(opcoes[3])
    op1 = int(input(f"Onde você esta com dor {nome}?: "))
    if(op1 == 1):

        # for cabeca_remedios in cabeca_remedios:
        #     print(cabeca_remedios)
        print(cabeca_remedios[0])
        print(cabeca_remedios[1])
        print(cabeca_remedios[2])
            
   
        biblioteca.cabeca()
    elif(op1 == 2):
        # for barriga_remedios in barriga_remedios:
        #     print(barriga_remedios)
        
        print(barriga_remedios[0])
        print(barriga_remedios[1])
        print(barriga_remedios[2])
            
        biblioteca.barriga()
    elif(op1 == 3):
        # for corpo_remedios in corpo_remedios:
        #     print(corpo_remedios)

        print(corpo_remedios[0])
        print(corpo_remedios[1])
        print(corpo_remedios[2])

        biblioteca.corpo()
    elif(op1 == 4):
        biblioteca.historico.append(opcoes[3])
        print(f"Aguarde {nome}...")
        print(biblioteca.tempo_fim())
        break


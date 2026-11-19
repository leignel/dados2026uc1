#Pedir um número e associar esse número a um dia da semana 
#se digitar 1 = domingo, 2 = segunda...

dia = int(input("Digite o núero do dia da semana (1 a 7): "))

# if dia == 1:
#     print("Domingo")
# elif dia == 2:
#     print("Segunda")
# elif dia == 3:
#     print("Terça-feira")
# elif dia == 4:
#     print("Quarta-feira")
# elif dia == 5:
#     print("Quinta-feira")
# elif dia == 6:
#     print("Sexta-feira")
# elif dia == 7:
#     print("Sábado")
# else:
#     print("Dia inválido")


#=============================================================
#match/case

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Dia inválido")

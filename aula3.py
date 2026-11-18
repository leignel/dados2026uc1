#Crie um algoritmo para dizer se uma pessoa é maior de idade ou não
#Número = int ou float
# idade = int(input("Qual a sua idade? "))

# if idade >= 18:
#     print("Você é maior de idade")
#     print("Pode tirar a carteira de motorista")
# else:
#     print("Você é menor de idade.")
#     faltam= 18 - idade
#     print(f"Faltam {faltam} anos(s) para completar 18.")

# print("Fim do programa.")

#Faça um algoritmo para dizer se o número é par ou ímpar

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

print(f"{numero} é {paridade}")
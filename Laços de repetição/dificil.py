# Adivinhação
# O programa escolhe um número secreto (ex.: 7). O usuário tenta 
# adivinhar até acertar, usando while.
# secreto = 7
# chute = int(input("qual numero: "))

# while chute != secreto:
#     if chute < secreto:
#         print("mais alto")
#     elif chute > secreto:
#         print("mais baixo")
#     chute = int(input("tente de novo: "))
# print("Parabéns! Você acertou!")
# Multiplicação acumulada
# Peça um número n e calcule o fatorial dele (n!) usando for.
# numero = int(input("numero"))

# if numero < 0:
#      print("Número inválido!")
# else:
#      fatorial = 1 
#      for i in range(1, numero + 1):
#           fatorial *= 1
#           print(f"{numero}! = {fatorial}")


# Menu interativo
# Crie um menu que fica se repetindo até o usuário digitar “sair”:

while True:
    print("Menu:")
    print("1 - Dizer Olá")
    print("2 - Mostrar número aleatório")
    print("3 - Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        print("Olá!")
    elif escolha == "2":
        import random
        print("Número aleatório:", random.randint(1, 100))
    elif escolha == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
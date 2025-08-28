# Peça 5 nomes ao usuário, guarde em uma lista e depois mostre
#  todos na tela.
# lista = []

# for i in range(5):  # repete 5 vezes
#     nomes = input("Qual nome: ")
#     lista.append(nomes) # type: ignore

# print(lista) # type: ignore

# Guarde 5 números em uma lista e mostre apenas 
# os números pares.
# numero = []

# for i in range(5):
#      i = int(input("qual numero: "))

#     if i % 2 == 0:
#        print(f"Esse número é par: {i}") 
#     else:
#          print(f"Esse número é ímpar: {i}")


# Peça 3 nomes e depois pergunte ao usuário um nome
#  qualquer. Diga se esse nome está ou não na lista.

# lista = []

# for i in range(5):
#     nomes = input("qual nome: ")
#     lista.append(nomes)
#     i += 1

# busca = input("buscar: ")

# if busca in lista:
#         print(f"{busca}: tem na lista")
# else:
#         print(f"{busca}: Não tem na lista")

# Peça 5 idades, guarde em uma lista e mostre qual é 
# a maior e qual é a menor idade.
# lista = []

# for i in range(5):
#     idade = int(input("qual idade: "))
#     lista.append(idade)
#     i += 1

# print("maio idade: ", max(lista))
# print("menor idade: ", min(lista56))

# Cadastre 5 notas em uma lista, calcule a média e diga 
# se o aluno foi aprovado (média ≥ 7) ou reprovado.
# nota =[]

# for i in range(5):
#     valo = int(input("nota: "))
#     nota.append(valo)
#     i += 1

# cal = (nota[0] + nota[1] + nota[2] +nota[3] + nota[4]) / 5

# if cal >= 7.010:
#     print(f"Voce foi aprovado nota: {cal}")
# else:
#     print(f"Voce foi reprovado media 7 sua nota: {cal}")


# Peça 5 números, guarde em uma lista e mostre apenas
#  aqueles que são maiores que 10.
lista = []

for i in range(5):
    numero = int(input("qual é numero: "))
    lista.append(numero)
    i += 1
   

for numero in lista:
    if numero >= 10:
        print(f"O número {numero} é grande (>= 10)")
    else:
        print(f"O número {numero} é pequeno (< 10)")

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

lista = []

for i in range(5):
    nomes = input("qual nome: ")
    lista.append(nomes)
    i += 1

busca = input("buscar: ")

if busca in lista:
        print(f"{busca}: tem na lista")
else:
        print(f"{busca}: Não tem na lista")

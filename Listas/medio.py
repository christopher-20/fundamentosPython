# Mostre quantos elementos tem em uma lista usando len().
frutas = ["maçã", "banana", "uva", "laranja", "manga"]
# print(len(frutas))
# for fruta in frutas:
#     print(fruta)

# Peça uma fruta ao 
# usuário e verifique se ela 
# está ou não dentro da lista.
busca = input("Digite uma fruta: ")

if busca in frutas:
    print(f"{busca} esta na lista")
else:
     print(f"{busca} não esta na lista")

# Crie um dicionário para guardar informações de uma pessoa:
#  nome, idade e cidade. Depois, exiba cada informação.
# Lista para guardar os cadastros
# cadastros = []

# # Quantidade de pessoas a cadastrar
# for i in range(2):
#     nome = input("Qual é seu nome: ")
#     idade = int(input("Qual é sua idade: "))
#     cidade = input("Onde mora: ")

#     # Criar um dicionário para cada pessoa
#     pessoa = { # type: ignore
#         "nome": nome,
#         "idade": idade,
#         "cidade": cidade
#     }

#     # Adicionar o dicionário na lista de cadastros
#     cadastros.append(pessoa) # type: ignore

# # Mostrar os cadastros
# print("\nCadastros realizados:")
# for pessoa in cadastros: # type: ignore
#     print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")

# Faça um dicionário com frutas como chave e preços como valor.
# Pergunte ao usuário uma fruta e mostre o preço.

# cadastro = []

# for i in range(2):
#     fruta = input("Qual é fruta: ")
#     preco = int(input("Qual é preço: "))

#     chave ={
#         "fruta": fruta,
#         "preco": preco
#     }
#     cadastro.append(chave)

# buscar = input("qual fruta deseja buscar: ")

# encontro = False

# for item in cadastro:
#     if item['fruta'].lower() == buscar.lower():
#         print(f"fruta {item['fruta']}, preço R${item['preco']}")
#         encontro = True
#     if not encontro:
#          print("Fruta não encontrada!")


# Crie um dicionário vazio e adicione 3 itens usando input() para 
# chave e valor.

dicionario = []

for i in range(3):
    valor = int(input("Qual é o valor: "))

    chave = {
        "valor": valor
    }

    dicionario.append(chave)

print("\nCadastros realizados:")
for chave in dicionario:  
    print(f"Valores salvos: {chave['valor']}")


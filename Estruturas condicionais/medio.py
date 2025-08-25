# Peça dois números e mostre qual é o maior ou se são iguais.
# valor = int(input("valor uma: "))
# valor2 = int(input("valor dois: "))
# cal = valor - valor2
# cal2 = valor2 - valor

# if valor2 < valor:
    # print(f"numero maios é {valor}, com diferença de {cal}")
# elif valor < valor2:
    #  print(f"numero maios é {valor2}, com diferença de {cal2}")
# else:
    #  print(f"São iguais os Numero {valor}")

# Peça uma senha ao usuário. Se for igual a "1234", 
# mostre “Acesso permitido”, senão mostre “Acesso negado”.
# senha = int(input("senha  Apenas numeros: "))
# salvo = 1234

# if senha ==  salvo:
    # print("Acesso permitido")
# else:
    # print("Acesso negado")

# Peça três lados de um triângulo e verifique se formam um 
# triângulo válido.
# (A soma de dois lados deve ser sempre maior que o terceiro).
# Se for válido, classifique como:
# Equilátero (3 lados iguais)
# Isósceles (2 lados iguais)
# Escaleno (3 lados diferentes)
lado = int(input("lado um: "))
lado2 = int(input("lado dois: "))
lado3 = int(input("lado tres: "))
cal = lado + lado2

if cal > lado3 and lado == lado2 == lado3:
    print(f"Equilátero (3 lados iguais), valor {lado} ")

elif cal > lado3 or lado == lado2 == lado3:
     print(f"Isósceles (2 lados iguais) ")
elif lado != lado2 and lado != lado3 and lado2 != lado3:
     print(f"Escaleno (3 lados diferentes)")
else:
     print("Nao valido como triango")

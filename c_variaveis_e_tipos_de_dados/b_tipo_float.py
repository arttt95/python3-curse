"""
Tipo Floart

Tipo Real, Decimal

Casas Decimais

OBS: O separador de casas decimais na programação é o ponto e não a vírgula.
"""


# Errado do ponto de vista do float, mas gera uma tupla
valor = 1,44
print(valor)
print(type(valor))

# Certo do ponto de vista do float
valor = 1.44
print(valor)
print (type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para ukm int
"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão.
"""
res = int(valor)
print(res)
print(valor2)

# Podemos trabalhar com números complexos
variavel = 5j


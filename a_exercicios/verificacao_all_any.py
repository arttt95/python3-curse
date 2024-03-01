nomes = ['Cristiano', 'Ronaldo', 'Lionel', 'Messi', 'Kaká']

res = any([nome[0] == 'C' for nome in nomes])

print(res)

lista = [1, 3, 4, 20, 6, 12, 8, 10]

novo = all([num % 2 == 0 for num in lista])

print(novo)

"""
________________________________________________________________________
"""

numeros = ['220', '120', '420', '550']

novos = any([num[1] == str(2) for num in numeros])

print(novos)

novos2 = all([num[1] == str(2) for num in numeros])

print(novos2)

"""
________________________________________________________________________
"""
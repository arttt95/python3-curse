"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))  # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))  # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))  # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))  # 129

# Faça um programa  qque receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe  o segundo valor: '))

print(max(val1, val2))

print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max('Geek University'))

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))  # 129

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))  # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))  # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))  # 129

# Faça um programa  qque receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe  o segundo valor: '))

print(min(val1, val2))

print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min('Geek University'))

# Outros Exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))  # Tim

print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander

print(min(nomes, key=lambda nome: len(nome)))  # Tim

"""

musicas = [
    {"titulo": "Thundeeerstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))

print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprima somente o titulo da musica mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])

print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO! Como encontrar a musica mais tocada e a menos tocada sem usar max(), min() e lambda()

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']


for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])


min = 9999
for musica in musicas:
    if musica['tocou'] > min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])

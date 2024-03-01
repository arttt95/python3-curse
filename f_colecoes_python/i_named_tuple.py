"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recap Tupla
tupla = (1, 2, 3)

print(tupla[2])

Named Tuple -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro1 = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 Ddeclaração Named Tuple

cachorro2 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='ray')

print(ray)

# Acessando os dados

# Forma 1

print(ray[0])  # idade
print(ray[1])  # nome
print(ray[2])  # raca

# Forma 2

print(ray.idade)  # idade
print(ray.raca)  # raca
print(ray.nome)  # nome


print(ray.index('Chow-Chow'))

print(ray.count('Chow-Chow'))

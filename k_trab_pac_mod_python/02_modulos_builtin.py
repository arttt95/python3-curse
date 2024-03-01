"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)
________________________
|Python|Módulos Builtin|

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *
# import random

print(random())

# Importando todo o módulo

import random

print(random.random())

# Utilizando alias (apelido) para módulos/funções

from random import randint as rdi

print(rdi(5, 89))

# Utilizando alias (apelido) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

https://docs.python.org/3/py-modindex.html#cap-r

"""

# Costumamos a utilizar tuple para colocar multiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))

nome = list('Cristiano Ronaldo')
shuffle(nome)
print(nome)

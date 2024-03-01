"""
Reversed

OBS: Não confunda com a função reverse() que estudamos em listas.

A função reverse reverse() só funciona nas listas.

Já a função reversed() funciona em qualquer iterável.

Sua funç~~ao é inverter o iterável.

A função reversed() retorna um iterável chamado List Reversed Iterator
"""

# Eemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converte o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos não definimos a ordem dos elementos
# Conjunto (Set)
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')
# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais fácil fazendo o slice de strings
print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
# for n in reversed(range(0, 10)):
#    print(n, end='')

# Apesar também que já vimos como fazer isso fazendo o próprio range()
for n in range(10, 0, -1):
    print(n, end='')

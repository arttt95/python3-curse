"""
Teste de velocidade com Expressões Geradoras

# Generator (geradores)

def nums():
    for num in range(1, 10):
        yield num

gen1 = nums()

print(gen1)  # Generator

print(next(gen1))
print(next(gen1))

# Generator Expression

gen2 = (num for num in range(1, 10))

print(gen2)  # Generator Expression

print(next(gen2))
print(next(gen2))
"""

# Realizando o teste de velocidade
import time

# Gerator Expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))  # 1 bilhões
gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # 1 bilhões
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')

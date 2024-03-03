"""
Geradores (Generators)

- Geradores (Generators) são iterators (Iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterador é um generator.

Outras Informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

-----------------------------------------------------------------------------------------------
/ Funções                                         /   Generator Functions                     /
-----------------------------------------------------------------------------------------------
/ Utilizam return                                 /   Utilizam yield                          /
-----------------------------------------------------------------------------------------------
/ Retorna uma vez                                 /   Podem utilizar yield muiltiplas vezes   /
-----------------------------------------------------------------------------------------------
/ Quando executada, retorna um valor              /   Quando executada, retorna um generator  /
-----------------------------------------------------------------------------------------------

gen = conta_ate(5)

# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)

for num in gen:
    print(num)

print(next(gen))  # 1

print('Geek')

for num in gen:
    print(num)
"""

# Exemplo de Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator. ok?


gen = list(conta_ate(10))

print(gen)

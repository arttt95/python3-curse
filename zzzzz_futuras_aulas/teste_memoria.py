"""
Teste de Memória com Generators

# Sequência de Fibonnacci
1, 1, 2, 3, 5, 8, 13...

# Teste 1 lista 470MB
for n in fib_lista(100000):
    print(n)
"""

def fib_lista(max):
    nums = []
    a,b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Função usando geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# Teste 2 Geradores 2,8MB
for n in fib_gen(100000):
    print(n)

"""
Len, Abs, Sum, Round

# Len

len() -> Retorna o tamanhh0 (ou seja, o número de itens) de um iterável.

# Só pra relembrar

print(len('Geek Unioversity'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunfer len
print('Geek University'.__len__())

# Abs

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica,seria o seu valor real sem o sinal.

# Exemplos

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Sum

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma dos elementos,
incluindo o valor inicial.

OBS: O valor inicial default = 0

# Exemplos Sum

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.145, 5.678]))

print(sum((1, 2, 3, 4, 5)))

print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1,'b': 2,'c': 3,'d': 4,'e': 5}.values()))

# Round

round() -> Retorna um n´pumero arredondado para n digito de precisão após a casa decimal. Se a precisão não for
informada retorna o inteiro mais próximo de entrada.
"""

# Exemplos Round

print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.2121212121, 2))

print(round(1.21999999, 2))

print(round(1.21999999))

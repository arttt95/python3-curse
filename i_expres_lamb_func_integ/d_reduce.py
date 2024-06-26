"""
Reduce

OBS: A partir do Python3+ a funão reduce() nao é mais uma funçao integrada (built-in)). Agora temos qie importar
e utilizar esta funao a partir do módulo 'functools'

Guido van Rossum Utilize a funao reduce() se voce realmente precisa dela. Em todo caso, 99% das vezes
um loop for é mai legível.

Para entender o reduce()

# Imagine que voce tem uma oleão de  dados;

dados = [a1, a2, a3, ..., an]

# E você tem uma funão que recebe dois parâmetros:

def funao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros a função e o iteráve.

reduce(funcao, dados)

A funao reduce(), funiona da seguinte forma:
    Passo 1 res1 = f(aa1, a2)  # Aplia a função nos dois primeiros elementos da ccoleão e guarda o resultado.
    Passo 2 res2 = f(res1, a3)  # Aplica a função passando o resultado do passo1 mais o terceciro elemento e guarda o
    res.

    Isso é repetido até o final.
    Passo 3 res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resn, an)

Ou seja, em cada passo ela aplicca a fun~~ao passando como primeiro argumento o resultado da aplicação anterior. No
final, reduce() irá retornar o resultado final.

Alternativamente, poderíamos veer a funão reduce() como

funcao(funao(funcao(a1, a2), a3)), a4), ...), an)
"""

# Como funciona na prátia?

# Vamos utilizar a funão reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que recebe dois parâmetros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)

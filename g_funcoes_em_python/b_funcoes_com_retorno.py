"""
Funções com Retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

-----------------------------------------------------------------------------------------------

OBs: Em Python quando uma função não retorna nenhum valor, o valor é None

OBS: Funções Pyhton que retornam valores, devem retornar esstes valores
com a palavra reservada return

OBS: Não precisamos necessariamente criar uma variável para receber o
retorno de uma função. Podemos passar a execução da função para outras funções.

-----------------------------------------------------------------------------------------------

# VAmos refatorar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7() + 1}')

# Refatorando a primeira função

def diz_oi():
    return 'Oi '

alguem = 'Pedro!'

print(diz_oi())
print(alguem)

-----------------------------------------------------------------------------------------------

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;

2 - Podemos ter, em uma função, diferentes returns;

3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos
valores;

-----------------------------------------------------------------------------------------------
1 - Ela finaliza a função, ou seja, ela sai da execução da função;

# Exemplo 1

def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'oi! '
    print('Estou sendo executado após o retorno...')

print(diz_oi())

-----------------------------------------------------------------------------------------------
2 - Podemos ter, em uma função, diferentes returns;

# Exemplo 2

def nova_função():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_função())

-----------------------------------------------------------------------------------------------
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos
valores;

# Exemplo 3

def outra_função():
    return 2, 3, 4, 5

#num1, num2, num3, num4 = outra_função()
#print(num1, num2, num3, num4)

print(outra_função())
print(type(outra_função()))

# Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um números pseudo-randõmico entre 0 e 0.333 Pedra, de 0.334 à 0.666 Papel e de 0.667 à 1 Tesoura.
    if random() < 0.334:
        return 'Papel'
    elif random() < 0.667:
        return 'Tesoura'
    return 'Pedra'

print(joga_moeda())
"""

# Erros comuns na utilização do retorno, que na vverdade nem é erro, mas sim
# codificação desnecessária.

def eh_impar():
    """
    Cria uma variavel chamada 'numero' que espera o número inteiro obrigatório informado pelo usuário,
    depois verifica se esse número é ou não ímpar.
    :return: Retorna True para numeros ímapres e False para números pares.
    """
    numero = 6
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())

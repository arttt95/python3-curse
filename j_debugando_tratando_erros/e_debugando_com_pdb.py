"""
Debuando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto

# OBS: A utilização do prinnt() para debugar código é uma prática ruim.
def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como PyCharm ou utilizando
# o PDB - Python Debuer

# Exemplo com oPyCharm

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 0))

# Exemplo com PDB - Python Debugger - Exemplo 1

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e entao utilizar a função set_trace()

# Comandos básicos do PDB
# l (para listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso

print(final)

# Exemplo com PDB - Python Debugger - Exemplo 2

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e entao utilizar a função set_trace()

# Comandos básicos do PDB
# l (para lisstar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb;  pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso

print(final)

# Por quê utilizar esse formato?
# O debug é utilizado durante o desenvolvimennto. Costumamos realizar todos os imports de bibliotecas no início
# do arquivo. Por isso, ao invvés de colocarmos o import do pdb no início do arquivo, nós colocamos somennte onde
# vamos debuggar, e ao finalizar já fazemos a remoção.

# Exemplo com PDB - Python Debugger - Exemplo 2

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e entao utilizar a função set_trace()

# * A partir do Python 3.7, não é mais necessário imporatar a biblioteca pdb, pois o comando dedebug foi incorporado
# como função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB
# l (para lisstar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso

print(final)

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

# Como os nomes das variáveis são os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variavel

# Nada de colocar nomes não representativos em variáeis. Sempre optar por nomes significativos.

def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4
"""

"""
PEP8 - Python Enhancement Proposal

São popostas de melhorias para a linguagem Python

The Zen of Python

import this

A idéia da PEP8 é que possamos escrever códigos Pyhton de forma Pythônica.

(1) - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCiêntífica:
    pass

(2) - Utilize nomes em minúsculo, separados por underline para funções ou vaeriáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

(3) - Utilize 4 espaços para identação! (Não use tab)

if 'a' in 'banana!':
    print('tem')

(4) - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco:
- Métodos dentro de uma classe devem ser separados com uma linha em branco;

(5) - Imports

- Imports devem ser sempre feitos em linhas separadas;


#Import Errado

import sys, os

#Import Certo

import sys
import os

# Não há problemas em utililzar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depos de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais.

(6) - Espaçoes em expressões e instruções:

# Não faça:

funcao(_algo[_1_], {_outro: 2_}_)

# Faça:

def funcao(param, param1):
    pass


funcao(algo[1], {outro: 2})

# Não faça:

def algo_(param):
    pass


algo_(1)

# Faça:

algo(1)

# Não faça:

dcit_['chave'] = list_[indice]

# Faça:
dict['chave'] = lista[indice]

# Não faça:

x                = 1
y                = 3
variavel_longa = 5

# Faça:

x=1
y=3
variavel_longa = 5

(7) - Termine sempre uma instrução com uma nova linha
"""
import this


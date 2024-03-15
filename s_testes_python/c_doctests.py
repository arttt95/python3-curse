"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.

Para rodar um test do doctest:

python - doctest -v nome_do_modulo.py

##################################################################
##                Função Exemplo para o Doctest                 ##
##################################################################

def soma(a, b):
    ###soma os números a e b

    #>>> soma(12, 2)
    3

    #>>> soma(3, 4)
    7
    ###
    return a + b


##################################################################
##                Saída com 1 passed e 1 passed                 ##
##################################################################

(curse) arttt@art:~/PycharmProjects/curse$ python -m doctest -v ../curse/s_testes_python/c_doctests.py
7
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    c_doctests
1 items passed all tests:
   1 tests in c_doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

##################################################################
##         Saída com 1 passed e 1 failed (Errada)               ##
##################################################################

(curse) arttt@art:~/PycharmProjects/curse$ python -m doctest -v ../curse/s_testes_python/c_doctests.py
Trying:
    soma(12, 2)
Expecting:
    3
**********************************************************************
File "/home/arttt/PycharmProjects/curse/../curse/s_testes_python/c_doctests.py", line 35, in c_doctests.soma
Failed example:
    soma(12, 2)
Expected:
    3
Got:
    14
1 items had no tests:
    c_doctests
**********************************************************************
1 items had failures:
   1 of   1 in c_doctests.soma
1 tests in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.

##################################################################
##     Saída com 2 passed, 1 passed e 1 failed (Errada)         ##
##################################################################

(curse) arttt@art:~/PycharmProjects/curse$ python -m doctest -v ../curse/s_testes_python/c_doctests.py
Trying:
    soma(12, 2)
Expecting:
    3
**********************************************************************
File "/home/arttt/PycharmProjects/curse/../curse/s_testes_python/c_doctests.py", line 61, in c_doctests.soma
Failed example:
    soma(12, 2)
Expected:
    3
Got:
    14
Trying:
    soma(3, 4)
Expecting:
    7
ok
1 items had no tests:
    c_doctests
**********************************************************************
1 items had failures:
   1 of   2 in c_doctests.soma
2 tests in 2 items.
1 passed and 1 failed.
***Test Failed*** 1 failures.

##################################################################
##                Função Exemplo para o Doctest                 ##
##                Usando Traceback para testar                  ##
##################################################################

# Outro Exemplo, Aplicando o TDD


def duplicar(valores):
    ### duplica os valore em uma lista

    #>>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    #>>> duplicar([])
    []

    #>>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    ###
    return [2 * n for n in valores]

##################################################################
##                    Erro Inesperado Exemplo                   ##
##              Uso das as aspas causou erro abaixo             ##
##################################################################

# Erro Inesperado

OBS: Dentro do doctest, o Python não reconhece string com aspas duplas.
Precisa ser aspas simples.

def fala_oi():
    ###Fala oi

    #>>> fala_oi()
    'oi'
    ###
    return "oi"
"""

# Um último caso estranho...


def verdade():
    """Retorna a verdade

    >>> verdade()
    True
    """
    return True

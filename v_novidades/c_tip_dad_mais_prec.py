"""
int, str, float, List, Set, Dict, etc
"""

# def dobro(valor: int) -> int:
#     return valor * 2
#
#
# print(dobro('Itachi'))  # Errado

"""
#####################################
##        TIPOS MAIS PRECISOS      ##
#####################################
##          * Literal type *       ##
##              * Union *          ##
##              * Final *          ##
##      * Typed dictionaries *     ##
##            * Protocols *        ##
#####################################

"""
"""
##########################
##     * Literal *      ##
##########################
"""
from typing import Literal


# def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
#     pass


# def calcula_v1(operacao: str, num1: int, num2: int) -> None:
#     if operacao == '+':
#         print(f'{num1} + {num2} = {num1 + num2}')
#     elif operacao == '-':
#         print(f'{num1} - {num2} = {num1 - num2}')
#     else:
#         raise ValueError(f'Operação inválida {operacao!r}')


# def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
#     if operacao == '+':
#         print(f'{num1} + {num2} = {num1 + num2}')
#     elif operacao == '-':
#         print(f'{num1} - {num2} = {num1 + num2}')
#     else:
#         raise ValueError(f'Operação inválida: {operacao!r}')
#
#
# calcula_v2('+', 6, 4)
# calcula_v2('-', 10, 2)
# calcula_v2('*', 3, 5)

"""
########################
##     * Union *      ##
########################
"""
# from typing import Union
#
#
# def soma(num1: int, num2: int) -> Union[str, int]:
#     resultado: int = num1 + num2
#
#     if resultado > 50:
#         return f'O valor {resultado} é muito grande!'
#     return resultado
#

"""
########################
##     * Final *      ##
########################
"""
# from typing import Final
#
#
# NOME: Final = 'Tinky-Winky'
#
# print(NOME)
#
# NOME: Final = 'Itachi'
#
# print(NOME)

"""
###########################
##  * Decorador final *  ##
###########################
"""
# from typing import final
#
#
# class Pessoa:
#
#     def __init__(self, nome: str):
#         self.__nome = nome
#
#     @property
#     def nome(self):
#         return self.__nome
#
#
# class Estudante(Pessoa):
#
#     def __init__(self, nome):
#         super().__init__(nome)
#
#     @final
#     def estudar(self):
#         return 'Estou estudando...'
#
#
# class Estagiario(Estudante):
#
#     def __init__(self, nome):
#         super().__init__(nome)
#
#     def estudar(self):
#         return 'Estou estudando e estagioando...'
#
#
# itachi = Estagiario('Itachi')
# print(itachi.estudar())

"""
#############################
##  * Typed Dictionaries * ##
#############################
"""
# from typing import TypedDict
#
#
# class CursoPython(TypedDict):
#     versao: str
#     atualizacao: int
#
#
# geek = CursoPython(versao='3.11.8', atualizacao=2024)
#
# print(geek)
#
# outro = CursoPython(algo='não sei', qualquer='sei lá')
#
# print(outro)

"""
##################################
##      * ANDA COMO PATO *      ##
##      * NADA COMO PATO *      ##
##      * FALA COMO PATO *      ##
##  * ENTÃO DEVE SER UM PATO *  ##
##################################
"""


# class Livro:
#
#     def __init__(self, nome: str, paginas: int) -> None:
#         self.__nome = nome
#         self.__paginas = paginas
#
#     @property
#     def nome(self):
#         return self.__nome
#
#     @property
#     def paginas(self):
#         return self.__paginas
#
#     def __len__(self):
#         return self.__paginas
#
#
# lor = Livro('Lord of the Rings', 234)
#
# print(len(lor))

"""
########################
##    * Protocols *   ##
########################
"""
from typing import Protocol


class Curso(Protocol):
    titulo: str

    def __init__(self):
        Curso.titulo = 'Refatoração'


def estudar(curso: Curso) -> None:
    print(f'Estou estudando {curso.titulo}')


class Venda(Curso):

    titulo = 'Programação em Python: Essencial'



curso1 = Venda()
curso2 = Curso()

estudar(curso1)
estudar(curso2)

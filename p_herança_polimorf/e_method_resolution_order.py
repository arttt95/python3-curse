"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem de Métodos)
 -> É a ordem de execução dos métodos (quem será executado primeiro).

Em Python nós podemos conferir a Ordem de Execução dos Métodos (RMO) de 3 formas:

    - Via propriedade da classe__mro__
    - Via método mro()
    - Via help
"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def cumprimenta(self):
        return f'Olá, eu sou o(a) {self.__nome}. (1)'


class Aquatico(Animal):

    def __init__(self, nome, especie):
        super().__init__(nome, especie)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando! (2)'

    def cumprimenta(self):
        return f'Olá, eu sou o(a) {self._Animal__nome} da água. (2)'


class Terrestre(Animal):

    def __init__(self, nome, especie):
        super().__init__(nome, especie)

    def andar(self):
        return f'{self._Animal__nome} esta andando! (3)'

    def cumprimenta(self):
        return f'Olá, eu sou o(a) {self._Animal__nome} da terra. (3)'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome, especie):
        super().__init__(nome, especie)

    def cumprimenta(self):
        return 'Pinguim (4)'

happy = Pinguim('Happy Feet', 'Pinguim')
print(happy.cumprimenta())

"""
class Pinguim(Aquatico, Terrestre):
Olá, eu sou o(a) Happy Feet da água. (2)

class Pinguim(Terrestre, Aquatico):
Olá, eu sou o(a) Happy Feet da terra. (3)
"""


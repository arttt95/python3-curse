"""
POO - Herança (Inheritance)

A idéia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma Classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdade.

Cliente
    - nome;
    - sobrenome;
    -cpf;
    -renda;

Funcionario
    - nome
    - sobrenome;
    - cpf;
    - matricula;

Perguntar: Existe uma entidade genérica o suficiente oara encapsular os atributos
e métodos comuns a outras entidades?

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Tinky', 'Winky', 345_124_456_00, 3500)
func1 = Funcionario('Itachi', 'Uchiha', 534_435_653_00, 456)

print(cliente1.nome_completo())
print(func1.nome_completo())
print(cliente1._Cliente__cpf)

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da
classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Fncionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

############################################
REFATORANDO UTILIZANDO HERANÇA ENTRE CLASSES
############################################

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    ###Cliente herda de Pessoa###

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum acesso dados super classe
        self.__renda = renda


class Funcionario(Pessoa):
    ###Funcionario herda de Pessoa###

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum acesso dados super classe
        self.__matricula = matricula


cliente1 = Cliente('Tinky', 'Winky', 345_124_456_00, 3500)
func1 = Funcionario('Itachi', 'Uchiha', 534_435_653_00, 456)

print(cliente1.nome_completo())
print(func1.nome_completo())

print(cliente1.__dict__)
print(func1.__dict__)

print(cliente1._Pessoa__nome)  # Name Mangling usando super classe, atributo 'nome' é dela.
print(cliente1._Pessoa__cpf)  # Name Mangling usando super classe, atributo 'cpf' é dela.
print(cliente1._Cliente__renda)  # Name Mangling usando classe Cliente, atributo 'renda' é dela.

# Sobrescrita de Métodos (Overriding)

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na
super classe em classes filhas.
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum acesso dados super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum acesso dados super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return (f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome} '
                f'{self._Pessoa__sobrenome}')




cliente1 = Cliente('Tinky', 'Winky', 345_124_456_00, 3500)
func1 = Funcionario('Itachi', 'Uchiha', 534_435_653_00, 456)

print(cliente1.nome_completo())
print(func1.nome_completo())

print(cliente1._Pessoa__cpf)

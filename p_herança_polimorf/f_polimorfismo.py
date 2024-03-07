"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Quando nós reimplementamos um método presente na classe pai nas classes filhas
estamos realizando uma sobescrita de método. (Overriding)

O Overridin é a melhor representação do polimorfismo.
"""

class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse método!')

    def comer(self):
        return f'{self.__nome} está comendo...'


class Dog(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} fala wau wau!'


class Cat(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} fala myaw!'


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} fala snif snif!'
# Testando

gato = Cat('Felix')
print(gato.comer())
print(gato.falar())

print('\n')

dog = Dog('Rufus')
print(dog.comer())
print(dog.falar())

print('\n')

mickey = Rato('Mickey')
print(mickey.comer())
print(mickey.falar())

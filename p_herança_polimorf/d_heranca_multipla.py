"""
POO - Herança Multipla

Herança Multipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde os atributos e métodos de todas as classes herdadas.

#OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por Muiltiderivação Direta;
    - Por Multiderivação Indireta;

# Exemplo 1 - Multiderivação direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiderivadaDireta(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiderivadaIndireta(Base3):
    pass

#OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança
herdará todos os atributos e métodos das super classes.

"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimenta(self):
        return f'Olá, eu so o(a) {self.__nome}! (1)'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando!'

    def cumprimenta(self):
        return f'Olá, eu sou o(a) {self._Animal__nome} do mar! (2)'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def anda(self):
        return f'{self._Animal__nome} esta andando!'

    def cumprimenta(self):
        return f'Olá, eu sou o(a) {self._Animal__nome} da terra! (3)'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)



# Testando

baleia = Aquatico('Walie')
print(baleia.nadar())
print(baleia.cumprimenta())

tatu = Terrestre('Bolinha')
print(tatu.anda())
print(tatu.cumprimenta())

pinguim = Pinguim('Happy Feet')
print(pinguim.nadar())
print(pinguim.anda())
print(pinguim.cumprimenta())

# Olá, eu sou o(a) Happy Feet da terra! (3) ### Method Resolution Order - MRO
# Olá, eu sou o(a) Happy Feet do mar! (2)

# Objeto é instância de...

print(f'Happy Feet é instância de Pinguim? {isinstance(pinguim, Pinguim)}')  # True
print(f'Happy Feet é instância de Aquatico? {isinstance(pinguim, Aquatico)}')  # True
print(f'Happy Feet é instância de Terrestre? {isinstance(pinguim, Terrestre)}')  # True
print(f'Happy Feet é instância de Animal? {isinstance(pinguim, Animal)}')  # True
print(f'Happy Feet é instância de Object? {isinstance(pinguim, object)}')  # True


# Ao criarmos uma classe o que acontece no código PBP é isso:


class Exemplo(object):
    pass


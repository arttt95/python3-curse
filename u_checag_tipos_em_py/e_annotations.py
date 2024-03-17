import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


# print(circunferencia.__annotations__)

# nome: str = 'Geek University'
#
# peso: float = 67.8
#
# ativo: bool = True
#
# print(nome)
# print(peso)
# print(ativo)
#
# print(__annotations__)


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando...'


p = Pessoa(nome='Geek University', idade=33, peso=65.3)

print(p.__dict__)

# print(p.__annotations__)  # Objetos não têm o atributo __annotations__

print(p.andar.__annotations__)

print(p.__init__.__annotations__)

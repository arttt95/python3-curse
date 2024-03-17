"""
nomes: list = ['Geek', 'University']

versoes: tuple = ('v1', 'v2', 'v3',)

opcionais: dict = {'Banco de Couro': True, 'Ar-condicionado': False}

valores: set = {3.45, 4.56, 5.67, 6.78}

print(nomes)
print(versoes)
print(opcionais)
print(valores)

print(__annotations__)

############################################
##                                        ##
##     TYPE HINTS PARA OS CONTEÚDOS       ##
##                                        ##
############################################

from typing import Dict, List, Tuple, Set

nomes: List[str] = ['Geek', 'University']

versoes: Tuple[str, str, str] = ('v1', 'v2', 'v3')

opcionais: Dict[str, bool] = {'ar': True, 'banco_couro': False}

valores: Set[float] = {3.45, 4.56, 5.67, 6.78}

print(nomes)
print(versoes)
print(opcionais)
print(valores)

print(__annotations__)
"""
import random

#  https://www.alt-codes.net/suit-cards.php
NAIPES = '♣ ♡ ♠ ♢'.split()[::-1]
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio=False):
    """Cria um baralho com 52 cartas para jogar"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado."""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar():
    """Inicia um jogo de cartas para 4 jogadores."""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split(' ')
    maos = {jog: mao for jog, mao in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()

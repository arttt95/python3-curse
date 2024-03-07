from random import random
from random import uniform


def jogo():
    res = uniform(1, 10)

    if res <= 3.999:
        print(f'{round(res, 4)}')
        print('Pedra!')
    elif 4 <= res <= 6.999:  # res >= 4 and res <= 6.999 (iguais)
        print(f'{round(res, 4)}')
        print('Papel!')
    else:
        print(f'{round(res, 4)}')
        print('Tesoura!')


jogo()
print('\n')
jogo()
print('\n')
jogo()
print('\n')
jogo()
print('\n')
jogo()
print('\n')

from random import random
from random import uniform

def jogo():
    res = uniform(1, 10)

    if res <= 3.999_999_999:
        print(f'{round(res, 4)}')
        print('Pedra!')
    elif res >= 4 and res <= 6.999_999_999:
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

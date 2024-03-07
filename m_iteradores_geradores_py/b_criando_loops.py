"""
Cirando sua própria versão de loop

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Geek University':
    print(letra)

iter([1, 2, 3, 4, 5])

iter('Geek University')
"""


def meu_loop_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_loop_for('Tinky-Winky!\n')

meu_loop_for([1, 2, 3, 4, 5, 6])

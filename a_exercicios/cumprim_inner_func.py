from random import choice


def cumprimento(pessoa):
    def humor():
        return choice((f'E ai {pessoa}?', f'Suma daqui {pessoa}!',
                       f'Não gosto de você {pessoa}!', f'Oi amiguinho(a) {pessoa}!'))
    return humor()


print(cumprimento('Angelina'))

print(cumprimento('Tinky-Winky'))

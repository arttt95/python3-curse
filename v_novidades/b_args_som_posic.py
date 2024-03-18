"""
Argumentos somente posicionais
"""

# valor = '67.3'
# print(float(valor))


# def cumprimenta_v1(nome):
#     return f'OLá, como vai? Meu nome é {nome}.'
#
#
# print(cumprimenta_v1('Geek'))
# print(cumprimenta_v1(nome='Geek'))


# def cumprimenta_v2(nome, /):
#     return f'Olá, como vai? Meu nome é {nome}'
#
#
# print(cumprimenta_v2('Geek'))
# print(cumprimenta_v2(nome='Geek'))


# def cumprimenta_v3(nome: str, /, menssagem: str = 'Olá') -> str:
#     return f'{menssagem} {nome}!'
#
#
# print(cumprimenta_v3('Geek', menssagem='Tchau'))
# print(cumprimenta_v3('Tinky-Winky'))
#
# print(cumprimenta_v3(nome='Itachi', menssagem='Hey'))  # Errado


# def cumprimenta_v4(nome: str, menssagem: str = 'Olá', /) -> str:
#     return f'{menssagem} {nome}!'
#
#
# print(cumprimenta_v4('Geek', 'Tchau'))
# print(cumprimenta_v4('Tinky-Winky'))
# # print(cumprimenta_v4(nome='Itachi', menssagem='Hey'))  # Errado


# def cumprimenta_v5(*, nome: str) -> str:
#     return f'Olá {nome}!'
#
#
# print(cumprimenta_v5(nome='Geek'))


def cumprimenta_v6(nome: str, /, menssagem1: str = 'Olá,', *, menssagem2: str = 'como vai?') -> str:
    return f'{menssagem1} {nome} {menssagem2}'


print(cumprimenta_v6('Tinky-Winky', menssagem1='Eai', menssagem2='tudo bem?'))
print(cumprimenta_v6('Goku', 'Hello'))
print(cumprimenta_v6('Itachi'))

print(cumprimenta_v6(nome='Power Rangers'))  # Errado
print(cumprimenta_v6('Geek', 'Oi', 'blz?'))  # Errado

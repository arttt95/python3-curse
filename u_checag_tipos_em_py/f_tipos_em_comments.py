import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(4))

# print(circunferencia('geek'))


def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    return 'b'


# cabecalho1(texto=43, alinhamento=False)


def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    return 'b'


cabecalho2(texto='geek', alinhamento=False)

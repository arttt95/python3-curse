"""
############################################################
##        PYTHON AVANÇADO ABAIXO COM TYPE HINTS           ##
############################################################
"""

# def cabecalho(texto: str, alinhamento: bool = True) -> str:
#     if alinhamento:
#         return f"{texto.title()}\n{'-' * len(texto)}"
#     else:
#         return f" {texto.title()} ".center(50, '#')
#
#
# print(cabecalho('geek university'))
#
# print(cabecalho('geek university', alinhamento=False))
#
# print(cabecalho('geek university', alinhamento='geek'))

"""
############################################################
##          PYTHON BÁSICO ABAIXO SEM TYPE HINTS           ##
##         NÃO APOIA O VASCULHADOR DE ERROS MYPY          ##
############################################################
"""


def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

print(cabecalho('geek university', alinhamento='geek'))

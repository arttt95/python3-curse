#def cumprimento(nome: str) -> str:
#    return f'Olá, {nome}'
#
#
#print(cumprimento('Geek'))


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

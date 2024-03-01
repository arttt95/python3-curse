"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datatypes

https://docs.python.org/3/library/collections.html#collections.Counter

Counter -> Recebe um iterável como parâmetro e cria um ojeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro
e como valor a quantidade de ocorrências desse elemento.

# Uttilizando o Counter

from collections import Counter

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 45, 66, 66, 43, 34]

# Exemplo 1

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({3: 6, 2: 4, 4: 4, 5: 4, 1: 3, 45: 3, 66: 2, 43: 1, 34: 1})

# Veja que para cada elemento da lista o Counter criou uma chave e colocou como valor
# a quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""

from collections import Counter

# Exemplo 3

texto = """
A final da Copa Libertadores da América de 2021 foi a 62.ª final da Libertadores da América, torneio continental
organizado anualmente pela Confederação Sul-Americana de Futebol (CONMEBOL), e foi disputada em 27 de novembro de 2021,
no Estádio Centenario, em Montevidéu, no Uruguai. Assim como na decisão da temporada passada, a partida foi
protagonizada por um clássico entre duas equipes brasileiras: o Palmeiras, de São Paulo, que se classificou para a final
pelo segundo torneio consecutivo, e o Flamengo, do Rio de Janeiro. A partida foi apitada pelo argentino Néstor Pitana.

Os dois times se classificaram diretamente para a fase de grupos; o Palmeiras, por, na época, ser o atual campeão, e o
Flamengo, por ter conquistado o Campeonato Brasileiro de 2020. O alviverde ficou no grupo A, com o Defensa y Justicia,
da Argentina, o Universitario, do Peru, e o Independiente del Valle, do Equador, enquanto o rubro-negro foi sorteado
"""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(10))

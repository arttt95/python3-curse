"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleçao.

# Biblioteca para trablhar com dados estatísticos
import statistics

# Dados coletados de alum sensor
dados = [1.3, 2.7, 0.8, 4.1, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a funçao map(), a filter() reccebe dois parãmetros,
# senda uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(type(res))
print(list(res))

# OBS: Assim com na função map(), apóes serem utiliados os dados de filter()
# eles são excluídos da memória.


# Biblioteca para trablhar com dados estatísticos
import statistics

# Dados coletados de alum sensor
dados = [1.3, 2.7, 0.8, 4.1, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a funçao map(), a filter() reccebe dois parãmetros,
# senda uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(type(res))
print(list(res))

# OBS: Assim com na função map(), apóes serem utiliados os dados de filter()
# eles são excluídos da memória.

paises = ['', 'Argentina', 'Brasil', 'Chile', '', 'Colombia',
          'Equador', '', 'Veneuela']

print(paises)

res = filter(None, paises)

print(list(res))

paises = ['', 'Argentina', 'Brasil', 'Chile', '', 'Colombia',
          'Equador', '', 'Veneuela']

# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(None, paises)
res = filter(lambda pais: pais != '', paises)

print(list(res))

# A diferença entre map() e filter() é:

# map() -> Recebe dois parametrso, uma funçao e um iterável e retorna um
# objeto mapeando a funçao para cada elemento do iterável.

# filter() -> Reccebe dois parametros, uma funçao e um iterável e retorna um
# objeto filtrando apenas os elementos de acordo com a função.

# Exemplos mais complexos

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gato"]},
    {"username": "carla", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

print(usuarios)

# Filtrar os usuários ue estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutoraa é' + nome, desde qque cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)

"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort()
só funciona em lilstas.

Podemosutilizar o sorted() em qualquerr iterável.

Como o próprio nomediz, sorted() serve para ordenar.

# Exemplo

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)

numeros = {6, 1, 8, 2}
print(numeros)

print(tuple(sorted(numeros)))

# Adiconando parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gato"]},
    {"username": "carla", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [],"cor": "preto", "musica": "rock"},
]

print(usuarios)

# Ordenando pelo username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

"""

# Último exemplo

musicas = [
    {"titulo": "Thundeeerstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32},
]

# Ordena da menos tocada para mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

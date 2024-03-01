musicas2 = [
    {'Música': 'Simple Man', 'Tocou': 20_000},
    {'Música': 'Rock of Ages', 'Tocou': 10_000},
    {'Música': 'Highway to Hell', 'Tocou': 40_000},
    {'Música': 'Sultans of Swing', 'Tocou': 8_000},
    {'Música': 'Passinho do Romano', 'Tocou': 200},
]

ordenacao1 = sorted(musicas2, key=lambda n: n['Tocou'])  # Menos tocadas

ordenacao2 = sorted(musicas2, key=lambda n: n['Tocou'], reverse=True)  # Mais tocadas

#print(ordenacao1)
#print('\n')
#print(ordenacao2)

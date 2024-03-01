musicas = [
    {'Música': 'Simple Man', 'Tocou': 20_000},
    {'Música': 'Rock of Ages', 'Tocou': 10_000},
    {'Música': 'Highway to Hell', 'Tocou': 40_000},
    {'Música': 'Sultans of Swing', 'Tocou': 8_000},
    {'Música': 'Passinho do Romano', 'Tocou': 200},
]

mais_tocada = max(musicas, key=lambda n: n['Tocou'])
menos_tocada = min(musicas, key=lambda n: n['Tocou'])


print(mais_tocada['Música'],
      ',tocou:',
      mais_tocada['Tocou'])
print(menos_tocada['Música'],
      ',tocou:',
      menos_tocada['Tocou'])

max = 0

for n in musicas:
    if n['Tocou'] > max:
        max = n['Tocou']

for n in musicas:
    if n['Tocou'] == max:
        print(n['Música'])
        print(n['Tocou'])

min = 1_000_000_000_000_000

for n in musicas:
    if n['Tocou'] < min:
        min = n['Tocou']

for n in musicas:
    if n['Tocou'] == min:
        print(n['Música'])
        print(n['Tocou'])

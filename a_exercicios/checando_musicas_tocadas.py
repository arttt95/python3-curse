musicas = [
    {'Música': 'Simple Man', 'Tocou': 20_000},
    {'Música': 'Rock of Ages', 'Tocou': 10_000},
    {'Música': 'Highway to Hell', 'Tocou': 40_000},
    {'Música': 'Sultans of Swing', 'Tocou': 8_000},
    {'Música': 'Passinho do Romano', 'Tocou': 200},
]

mais_tocada = max(musicas, key=lambda x: x['Tocou'])
menos_tocada = min(musicas, key=lambda x: x['Tocou'])


print(mais_tocada['Música'],
      ',tocou:',
      mais_tocada['Tocou'])
print(menos_tocada['Música'],
      ',tocou:',
      menos_tocada['Tocou'])

valor_max = 0

for n in musicas:
    if n['Tocou'] > valor_max:
        valor_max = n['Tocou']

for n in musicas:
    if n['Tocou'] == max:
        print(n['Música'])
        print(n['Tocou'])

valor_min = 1_000_000_000_000_000

for n in musicas:
    if n['Tocou'] < valor_min:
        valor_min = n['Tocou']

for n in musicas:
    if n['Tocou'] == valor_min:
        print(n['Música'])
        print(n['Tocou'])

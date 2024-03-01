nomes = ['Ana', 'Carla', 'Roberta', 'Lia', 'Gina', 'Odete']

# Estamos rodanddo um map que o primeiro parâmetro é uma função lambda que apenas cria a string
# "Sua instrutora é: {nome}"
# A segunda parte do map é um filter que procura cada nome com len < 5 in nomes

menores = map((lambda nome: f'Sua instrutora é: {nome}'), filter(lambda nome: len(nome) < 5, nomes))

print(list(menores))

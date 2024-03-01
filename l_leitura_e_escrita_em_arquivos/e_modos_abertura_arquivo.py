"""
Modos de abertura de arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir - Caso o arquivo já exista, gera FileExistError
a -> Abre para escrita adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e Escrita. (Temos o controle do cursor)

# OBS: Abrindo no modo 'a' que é apende, se o arquivo não existir será criado. Caso exista, o novo connteúdo será
adicionado SEMPRE ao final do arquivo. Com o modo 'a', não controlamos o cursor.

http://docs.python.org/3/library/functions.html#open

# Exemplo 'x'
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe!')

# Exemplo 'a'

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

# Exemplo r+
with open('outro.txt', 'r+') as arquivo:
    arquivo.write('Adicionada\n')
    arquivo.seek(11)
    arquivo.write('Outro Nova linha.\n')
    arquivo.seek(32)
    arquivo.write('Outro Mais uma linha.\n')
"""

# Exemplo r+
with open('../zzzzz_futuras_aulas/outro.txt', 'r+') as arquivo:
    arquivo.write('Adicionada\n')
    arquivo.seek(11)
    arquivo.write('Nova linha.\n')
    arquivo.seek(23)
    arquivo.write('Outro Mais uma linha.\n')

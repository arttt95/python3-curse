"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.

arquivo = open('file')

print(arquivo.read())

# A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um parâmetro de onde queremos
# colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek() --> Procurar (Procura pra mim na posição que eu passar)

arquivo.seek(0)

print(arquivo.read())

arquivo.seek(22)

print(arquivo.read())
arquivo = open('file')

print(arquivo.read())


# readline()) -> Função que lê o arquivo linha a linha (readline -> Lê a linha)

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))

# readlines()

linhas = arquivo.readlines()

print(len(linhas))

# OBS: Quando abrimos um arquivvo com a função open(), é criada uma coneão entre o arquivo no Disco e o nosso
programa. Essa conexao é chamada de streaming.

Ao finalizarmos os trabalhos com esse arquivo, devemos fechar essa conexão. Para isso temos o close()

Passos para se trabalhar com um arquivo

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;

# 1 - Abrir o arquivo;
arquivo = open('file')

# 2 - Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado (False)

# 3 - Fechar o arquivo;
arquivo.close()

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado (True)

print(arquivo.read())

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError

"""

"""
arquivo = open('file')

tam_read = arquivo.read(50)

print(len(tam_read))
"""

"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissao de Escrita -> Para escrever o arquivo.

StringIO -> Utiliazdo para ler e criar arquivos em memória.
"""

# Primeiro fazemos o imporrt
from io import StringIO

mensagem = 'Esta é apenas uma String normal'

# Podemos criar um arrquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto
# depois
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo qur j� sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())

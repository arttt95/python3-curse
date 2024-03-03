"""
Sistema de Arquivos - Manipulação

import os

# Descobrindo se um arquivo ou diretório existe

# Arquivos
print(os.path.exists('arquivo.txt'))
print(os.path.exists('frutas.txt'))

# Diretórios
print(os.path.exists('geek'))  # True
print(os.path.exists('geek/university'))  # True
print(os.path.exists('geek/university/geek3.py'))  # True
print(os.path.exists('outro'))  # False

# Paths absolutos
print(os.path.exists('/home/arthur/university'))  # False
print(os.path.exists('/home/arthur/Pictures'))  # True
print(os.path.exists('/home/arthur/Pictures/Wallpapers/Desktop-Wallpaper.jpg'))  # True

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3

with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

# Criando arquivos

os.mknod('arquivo-teste4.txt')

os.mknod('/home/arthur/university.txt')

#OBS: Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError

# OBS: Criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError

# Criando diretórios - Únicos (um a um)

os.mkdir('templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError

os.mkdir('/etc/Template')

# OBS: Se não tivermos permissão para criarmos o diretório teremos um PermissionError

# Criando multi-diretórios (árvore de diretórios)
os.makedirs('Template/geek/university')

# OBS: Se já existir, teremos um FileExistsError

os.makedirs('template2/novo2/outro2', exist_ok=True)

# Renomear arquivos e diretórios

os.rename('template2', 'geek2')

# OBS: Se o diretório nã́o existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vázio teremos um OSError

# Renomeando Arquivos e Diretórios

# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')

# Arquivos
os.rename('frutas.txt', 'cesta1.txt')

# Atenção! tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles não vão para a lixeira.
# Eles somem.

# Removendo arquivos
os.remove('geek')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.

# OBS: Caso o arquivo não exista teremos um erro FileNotFound

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um erro IsADirectoryError

# Removendo diretórios vazios

os.rmdir('Template')

# OBS: Se o diretório tiver qualquer conteúdo teremos um erro OSError

# OBS: Se o diretório não existir teremos um erro FileNotFoundError

# Removendo uma árvore de diretórios
for arquivo in os.scandir('geek2'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios vazios]

os.removedirs('geek/mais')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

# ATENÇÃO! Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora!

# Importando a biblioteca send2trash (Envia arquivos e diretórios para a lixeira
from send2trash import send2trash

# Se aparecer o erro no command "lsb_release":

sudo apt-get install lsb-core

os.remove('cesta1.txt')  # Não vai para a lixeira. É deletado imediatamente.

send2trash('cesta2.txt')  # Vai para a lixeira. Pode ser restaurado.

send2trash('teste')

# OBS: Se o arquivo não existir teremos OSError

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

# Criando umdiretório temporário

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei um diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: possivelmente o código acima não irá funcionar se você estiver utilizando o Windows.
# Por conta desse sistema trabalhar de forma diferente com arquivos temporários.

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos "b"

# Sem o bloco with

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()

http://docs.python.org/3/library/os.html?highlight=os#module-os
"""


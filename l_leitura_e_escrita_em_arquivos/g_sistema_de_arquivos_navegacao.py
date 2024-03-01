"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do móduolo os.

os -> Operating System - Sistema Operacional

# getced() - Pega o current work directory - diretório de trabalho corrent
# Retorna o path (caminho) absoluto
print(os.getcwd())  # /home/arthur/PycharmProjects/guppe

# Para  mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())  # /home/arthur/PycharmProjects

os.chdir('..')

print(os.getcwd())  # /home/arthur

os.chdir('..')

print(os.getcwd())  # /home

os.chdir('..')

print(os.getcwd())  # /

os.chdir('..')

print(os.getcwd())  # /

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('/home/arthur'))  # True

# OBS para usuários Windows
# Se você , infelizmente, estiver utilizando um computador com Windows,
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('/home/arthur/PycharmProjects/guppe/'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)

# Podemos identificar o sistema operacional com o módulo os
print(os.uname())  # Mostra mais dados sobre o Sistema Operacional

# Fazer o import
import sys

print(sys.platform)

'/home/arthur/workspace/sistema'

print(os.getcwd())  # /home/arthur/PycharmProjects/guppe

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())  # /home/arthur/PycharmProjects/guppe/geek/university

# Veja que os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o
# diretório que será juntado ao atual.

# Podemos listar os arquivos e diretórios com o listdir()

print(len(os.listdir('/etc')))
"""

import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir()

arquivos = list(scanner)

print(arquivos)

print(dir(arquivos[0]))

print(arquivos[0].inode())  # ??
print(arquivos[0].is_dir())  # É um diretório? False
print(arquivos[0].is_file())  # É um arquivo? True
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho do arquivo
print(arquivos[0].stat())  # Estátisticas...

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo.

scanner.close()

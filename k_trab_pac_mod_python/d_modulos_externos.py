"""
Módulos Externos

Utilizamos o erenciador de pacotes Python chamado Pip - Python Installer Package

Voce pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressao de tetos coloridos no terminal

Instalando um modo:

pip install nome-do-modulo

# Instalando o pacote colorama

pip install colorama

# Utilizando o pacote instalado

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.RED + 'Geek University')
print(Fore.BLUE + 'Geek University')
"""
"""
import pydf

pdf = pydf.generate_pdf('<h1>Geek Uniersity</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
"""
from colorama import init, Fore, Back, Style

lista = [1, 2, 3, 4, 5, 5]

print(lista)

init()

print(Fore.LIGHTMAGENTA_EX + Back.RED + 'Tinky-Winky')

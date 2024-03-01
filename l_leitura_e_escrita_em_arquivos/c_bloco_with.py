"""
Bloco With

Passos para se trabalhar com arquivos

# 1 - Abrimos o Arquivo
# 2 - Manipulamos com o arquivo
# 3 - Fechamos o arquivo

O block with é utilizado para criar um contexto de trabalho onde os recursos utilizados sao fechados após o bloco wwith.

arquivo = open('teto.txt')
"""

# O block with - Forma Pythônica de manipular arquivos

with open('../novo.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

# print(arquivo.readlines())
print(arquivo.closed)

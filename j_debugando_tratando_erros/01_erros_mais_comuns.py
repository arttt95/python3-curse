"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saidas de erros feradas pela execução do nosso
código.

Os erros mais comuns:

1 - SyntaError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o
Python não reconhece como parte da loinguagem.

Exemplos SyntaxError

a)
def funcao():
    print('Geek University')

b)
None = 1

2 - Exemplos NameError -> Ocorre quando uma variável ou uma função não foi definida

Exemplos NameError

a)
print(geek)

b)
geek()

3 - Exemplos TypeError -> Ocorre quanndo uma função/operação/ação é aplicada a um tipo errado

Exemplos TypeError

a)
print(len(5))

b)
print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado
indexado utilizando um índice inválido

a)
lista = ['Geek']
print(lista[1])

b)
lista = ['Geek']
print(lista[0][10])

5 - ValueError -> Ocorre quando uma função/ operação built-in (integrada) recebe um argumento com tipo
correto mas valor inapropriado

Exemplos ValueError

a)
print(int('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar dicionario com uma chave que não existe.

Exemplos KeyError

a)
dict = {'python': 'university'}
print(dict['geek'])

7 - AtributeError -> Ocorre quando uma variável não tem um atributo/função.

Exemplos AtributeError

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

8 - IndetentionError -> Ocorre quando não respeitamos a indentação do Python (4 espaçoes)

Eemplos IndententionError

a)
def nova():
print('Geek')

b)
for i in range(10):
i + i

OBS: Exceptions e Erros são sinônimos na programação.

OBS: Iportante ler e prestar atenção na saída de erro.
"""

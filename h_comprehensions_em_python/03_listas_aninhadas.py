"""
Listas Aninhadas (Nested Lists)

- Algumas linguagensc de programação (C/ Java) possuem uma estrutura de dados
chamadas de arrays:
     - Unidimensionais (Arrays/Vetores);
     - multidimensionais (Matrizes);

Em Python nós temos as Listas

numeros = [1, 'b', 2, 3.234, True, 4, 5]

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)

print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0])

print(listas[0][1])  # Acesso ao número 2
print(listas[2][1])  # Acesso ao número 8

# Iterando com loops em uma lista aninhada
for lista in listas:
    for numero in lista:
        print(numero)

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]
"""

# Outros Exemplos

# Gerando um tabuleiro/Matriz 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if valor %2 != 0 else 'O' for valor in range(1, 4)] for valor in range(1, 4)]
print(velha)


# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])

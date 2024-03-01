"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loop for

Ranges são utilizados parar gerar sequências numéricas, não de forma aleatória,
mas sim de maneira específica.

Formas Gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Forma 1

# Exemplo Forma 1

for number in range(11):
    print(number)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valo_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

# Exemplo Forma 2

for num in range(3, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 3

for num in range(5, 50, 5):
    print(num)

# Forma 4 (Forma 3 Inverse)

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_parada não inclusive (inicio especificado pelo usuário, e passo especificado
pelo usuário)

# Exemplo Fora 4

for num in range(10, -1, -1):
    print(num)

"""


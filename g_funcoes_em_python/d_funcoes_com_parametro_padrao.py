"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opicional;

# Exemplo de função onde a passagem de parâmetro seja opicional
print("Geek University'")

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrad(numero):
    return ** 2

print(quadrado(3))
print()  # TypeError

def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva a potencia informada pelo usuário

# OBS
# Se o usuário passar apenas um parâmetro, este será atribuído ao parâmetro
# numero, e será calculado o quadrado deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro
# numero e o segundo ao parâmetro potencia. Então será calculada esta potência.

print(exponencial())

# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM
# sempre estar ao final da declaração.

# ERRO!
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros exemplos

def soma(num1=5, num2=3):
    return num1 + num2

print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())   # TypeError

#  Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo Instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))  # True
print(mostra_informacao(True))  # True
print(mostra_informacao(nome='Stephany'))

# Por quê utilizar parâmetros com valor default?

# - Nos permite sermos mais flexíveis nas funções;
# - Evita erros com parâmetros incorretos;
# - Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;

# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global

def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'oi {instrutor}'

print(diz_oi())

# OBS: Setivermos uma variável local com o mesmo nome de uma variável global,
# a local terá a preferência.

def diz_oi():
    prof = 'Geek'  # Variável local
    return f'Olá {prof}'

print(diz_oi())

print(prof)  # NameError

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1  # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa())

-------------------------------------------------------------------------

# Forma correta
total = 0


def incrementa():
    global total  # Avisando que qeuremos utilizar a variável global

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
"""


# Podemos ter funções que são declaradas dentro de funções, e também tem uma
# forma especial de escopo de variável

def fora():
    """
    Define um contador que é estipalado em 0 se o usuário não pré definí-lo com outro número inteiro.
    A função abaixo fica responsável por captar esse número e toda vez que for ativada acrescentará 1 ao valor e
    retonará esse resultado para a função acima.
    :return: Retorna o resultado da função interna para o usuário.
    """
    contador = 0
    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())


print(dentro())  # NameError (Conhecida apenas localmente - Dentro da função que foi declarada)

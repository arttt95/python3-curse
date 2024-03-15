"""
Assertions (Afirmações/Declarações/Checagens/Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples afirmações
utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.

Se a expressão for verdadeira, retorna None e caso seja falsa levantara um erro
do tipo AssertionError.

# OBS: Nós podemos especificar, opcionalmente, um seegundo argumento ou mesmo uma mensagem
de erro personalizada;

# OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso...
não é necessário ser excludisamente nos testes.

# ALERTA: Cuidado ao utilizar 'assert'

Se o program Python for executado com o parâmetro -O, nenhum assertion será validado.
Ou seja, todas as suas validações serão inutilizadas.
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


ret = soma_numeros_positivos(4, 4)  # 8
# ret = soma_numeros_positivos(4, 4)  # AssertionError
# print(ret)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'sorvete',
        'batata-frita',
        'cachorro-quente'
    ], 'A comida precisa ser fast food'
    return f'E estou comendo {comida}!'


comida = input('Insira uma comida:')

print(comer_fast_food(comida))


# Cuidado com a sehuinte hipótese:
def faca_algo_ruim(usuario):
    assert usuario.eh_admin, "Somente administradores podem fazer coisas ruins!"
    destroi_todo_o_sistema()
    return 'Adeus'
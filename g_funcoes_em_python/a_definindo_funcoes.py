"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não entradas de daos e retornar uma saída de dados;
- Elas são muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom você fazer uma vereificação para que a função seja simplificada;

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;

"""

# Exemplo de utilização de funções:

#cores = ['verde', 'amarelo', 'azul', 'vermelho']

# Utilizando uma função integrada (Built-in) do Pyhton "print()"

#print(cores)

#curso = 'Programação em Python: Essencial!'

#print(curso)

#cores.append('roxo')

#print(cores)

#print(help(print))

# DRY - Don't Repeat Yourself! - Não Repita o Seu Código!

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é:
def nome_da_funcao(parenteses_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline
(Snake Case);

parametros_de_entrada -> Opicionais, onde tendo mais de um, cada um separado por vírgula, podendo
ser opicionais ou não;

blobo_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função
acontece.
* Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função , utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos ":" que
é utilizado e Python para definir blocos.
"""

def diz_oi():
    print('oi')


"""
OBS:

1 - Veja que, dentro das nossas funções podemos utlizar outras funções;
2 - Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer "oi";
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada.
"""

# Utilizando funções

diz_oi()


"""
ATENÇÃO!!!

Nunca esqueça de utilizar o parênteses ao executar uma função.

Exemplo:

# Errado!
dz_oi

# Certo!
diz_oi()

# Errado!
diz_oi () #  Com espaço entre os parênteses e o "nome_da_funcao"
"""

# Exemplo 2

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitos anos de via')
    print('Viva o aniversariante!')

#cantar_parabens()

#for v in range(1, 6):
#    print(v)
#    cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através
# da variável.

canta = cantar_parabens

canta()

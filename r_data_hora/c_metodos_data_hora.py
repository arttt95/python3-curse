"""
Métodos de Data e Hora

# Com now() podemos especificar um timezone (Fuso Horário)
agora = datetime.datetime.now()  # now == agora
print(type(agora))
print(repr(agora))
print(agora)

hoje = datetime.datetime.today()  # today == hoje
print(type(hoje))
print(repr(hoje))
print(hoje)

######################################################################

# Mudanças ocorrendo a meia-noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() +
                                        datetime.timedelta(days=1)),
                                       datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

########################################################################

# Encontrar o dia da semana. weekday()

# Os dias da semana começam em 0, sendo 0 a segunda-feira

# 0 - Monday
# 1 - Tuesday
# 2 - Wednesday
# 3 - Thursday
# 4 - Friday
# 5 - Saturday
# 6 - Sunday

manutencao = datetime.datetime.combine((datetime.datetime.now() +
                                        datetime.timedelta(days=1)),
                                       datetime.time())

print(manutencao.weekday())

######################################################################

born = input('Informe a sua data de nascimento (dd/mm/yyyy): ')

born = born.split('/')

born = datetime.datetime(year=int(born[2]), month=int(born[1]), day=int(born[0]))

if born.weekday() == 0:
    print('Você nasceu em uma segunda-feria.')
elif born.weekday() == 1:
    print('Você nasceu em uma terça-feira.')
elif born.weekday() == 2:
    print('Você nasceu em uma quarta-feira.')
elif born.weekday() == 3:
    print('Você nasceu em uma quinta-feria.')
elif born.weekday == 4:
    print('Você nasceu em uma sexta-feira.')
elif born.weekday == 5:
    print('Você nasceu em um sábado.')
else:
    print('Você nasceu em um domingo.')

print(born)
print(type(born))
print(repr(born))

##############################################################

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()

print(hoje)

# O 'y' altera o ano:
# Se for passado 'y' minúsculo sera retornado o ano compactado.
# Se for passado o 'Y' maiúsculo será retornado o ano completo com 4 números.
# O mês tambêm sofre alterações:
# Se for passada a letra 'b' será retornado o mês em forma escrita e encurtada (inglês).
# Se for passado a letra 'B' será retornado o mês em forma escrita e completa (inglês).
hoje_formatado = hoje.strftime('%d/%B/%y')

print(hoje_formatado)

# Formatando com uma função:


def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}.'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}.'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}.'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}.'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}.'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}.'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}.'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}.'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}.'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}.'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}.'
    else:
        return f'{data.day} de Dezembro de {data.year}.'


hoje = datetime.datetime.today()

print(formata_data(hoje))

################################################################

import datetime
from textblob import TextBlob


def formata_data(data):
    return (f"{data.day} de {TextBlob(data.month.strftime('%B')).translate(to='pt-br')} "
            f"de {data.year}.")


hoje = datetime.datetime.today()

print(formata_data(hoje))

nascimento = datetime.datetime.strptime('25/04/1995', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual é a sua data de nascimento? (dd/mm/yyyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

# Somente a hora

almoco = datetime.time(12, 30, 0)

print(almoco)

# Marcando o tempo de execução do nosso código com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10_000)
print(tempo)

tempo2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10_000)
print(tempo2)

tempo3 = timeit.timeit('"-".join(map(str, range(100)))', number=10_000)
print(tempo3)

"""
import timeit, functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10_000))

"""
Manipulando Data e Hora

Python tem um módulo bult-in (integrado) para se trabalhar com data e hora
chamado datetime.

2024-03-07 15:05:04.237458

2024-03-07 15:10:04.237458

########################################################################3

# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

print(datetime.datetime.now())  # 2024-03-07 14:56:58.099402

# datetime.datetime(year, month, day, minute, seconds, microsecond)
# datetime.datetime(2024, 3, 7, 15, 1, 28, 324379)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horario para 16 horas, 0 minuto, 0 segundos, 0 microsegundos
inicio = inicio.replace(year=2025, hour=16, minute=0, second=0, microsecond=0)

print(inicio)

##########################################################################################

# Recebendo dados do usuário e convertendo para datatime
nascimento = input('Informe a sua data de nascimento no formato (dd/mm/yyyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))

"""
import datetime

evento = datetime.datetime.now()

print(evento.year)
print(evento.month)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

print(dir(evento))

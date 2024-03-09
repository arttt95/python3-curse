"""
Trabalhando entre deltas de data e hora

data_inicial = dd/mm/yyyy 12:55:34.9999
data_final = dd/mm/yyyy 13:59:45.9999

delta = data_final - data_inicial

################################################################

import datetime

# Temos a data de hoje
# module(datetime).class(datetime).method(now())
data_hoje = datetime.datetime.now()

# Data prevista para o evento ocorrer
evento = datetime.datetime(year=2025, month=4, day=25, hour=6, minute=32, second=45)

# Calculando o Delta (Espaço de tempo entre dois eventos)
tempo_para_evento = evento - data_hoje

# <class 'datetime.timedelta'>
print(type(tempo_para_evento))

# datetime.timedelta(days=413, seconds=53330, microseconds=956251)
# module.class(days amount, seconds amount, microseconds amount)
print(repr(tempo_para_evento))

# 413 days, 14:48:50.956251
# days amount, hours:minutes:seconds.microseconds amount
print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias e '
      f'{int(tempo_para_evento.seconds / 60 // 60)} '
      f'horas para o evento!')

"""

import datetime

data_da_compra = datetime.datetime.now()
print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento = data_da_compra + regra_boleto
print(vencimento)

import time
from threading import Thread

contador = 50_000_000


def contagem_regressiva(valor):
    while valor > 0:
        valor = valor - 1


inicio = time.time()
contagem_regressiva(contador)
fim = time.time()
res = fim - inicio
print(f'Tempo do single thread em segundos: {round(res, 4)}')

# Tempo do single thread em segundos: 1.5135

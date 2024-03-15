import time
from threading import Thread

contador = 50_000_000


def contagem_regressiva(valor):
    while valor > 0:
        valor = valor - 1


t1 = Thread(target=contagem_regressiva, args=(contador//2,))
t2 = Thread(target=contagem_regressiva, args=(contador//2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()
res = fim - inicio
print(f'Tempo do multi threads em segundos: {round(res, 4)}')

# Tempo do multi threads em segundos: 1.4394

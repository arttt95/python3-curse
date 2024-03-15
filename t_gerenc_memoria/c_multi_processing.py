from multiprocessing import Pool
import time

contador = 50_000_000


def contagem_regressiva(valor):
    while valor > 0:
        valor = valor - 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [contador//2])
    r2 = pool.apply_async(contagem_regressiva, [contador//2])
    pool.close()
    pool.join()
    fim = time.time()
    res = fim - inicio
    print(f'Tempo do multi processing em segundos: {round(res, 4)}')

# Tempo do multi processing em segundos: 0.703

def comer(comida, eh_saudavel):
    besteiras = ['pizza',
                 'pipoca',
                 'sorvete',
                 'hamburger']
    comeco = f'Estou comendo {comida} porque'
    if comida not in besteiras:
        return f'{comeco} quero ficar em forma.'
    return f'{comeco} só se vive uma vez.'


def dormir(qtd_horas):
    if qtd_horas < 8:
        return f'Continuo cansado porque dormi apenas {qtd_horas} horas.'
    return 'Estou atrasado porque dormi demais.'


def eh_engracada(pessoa):
    comediantes = [
        'Jim Carrey',
        'Danilo Gentilli',
        'Kevin Hart'
    ]
    if pessoa not in comediantes:
        return False
    return True

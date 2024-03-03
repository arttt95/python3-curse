"""
Forçando tipos de dados com decoradores


"""

def forca_tipo(*args1):
    def decorador(funcao):
        def converte(*args2, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args2, args1):
                novo_args.append(tipo(valor))  # str('Geek'), int('3')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)

repete_msg('Geek', '3')

@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)

dividir('1', 5)

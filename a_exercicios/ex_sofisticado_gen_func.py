def verif_prim_valor(valor):
    def interna(funcao):
        def subsolo(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! O primeiro valor deverá ser "{valor}"!'
            return funcao(*args, **kwargs)
        return subsolo
    return interna


@verif_prim_valor('simple man')
def top_tres_musicas_favoritas(mus1, mus2, mus3, *args):
    return f'A melhor é {mus1}, do meio é {mus2}, ultima é {mus3}!'


print(top_tres_musicas_favoritas('simple man', 'unchined melody',
                                 'um minuto para o fim do mundo'))


@verif_prim_valor(10)
def soma_valores(num1, num2):
    return num1 + num2


print(soma_valores(3, 4))

try:
    print('geek'[10])
except NameError as erra:
    print(f'Foi gerado o erro: {type(erra)}')
except TypeError as errb:
    print(f'O código gerou o erro: {errb}')
except:
    print('Deu algum outro erro!')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as errc:
        print(f'Foi gerado o erro: {type(errc)}')

dic = {"Neymar": "Cai-Cai", "CR7": "General", "Messi": "Extraterrestre"}

print(pega_valor(dic, "Fenômeno"))

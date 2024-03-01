with open('lista_de_compras.txt', 'w') as arquivo:
    while True:
        carrinho = input('Insira um item do mercado: ')
        if carrinho != 'sair':
            arquivo.write(carrinho)
            arquivo.write('\n')
        else:
            break

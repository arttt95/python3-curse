carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Método Próprio

resposta = ''
carrinho = []

while resposta != 'sair':
    print('Insira o produto ou digite "sair" para sair:\n')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
    else:
        print('Confira seus produtos e siga para o check out!\n')
        for n in carrinho:
            print(n)

"""
O operador Walrus permite fazermos a atribuição e retorno de valor
em uma única expressão.

##############
##  syntax  ##
##############

variavel := expressão
"""
# # normal:
# nome = 'Geek University'
# print(nome)
#
# # walrus:
# print(nome := 'Geek University')

# # loop while normal:
# cesta = []
# fruta = input("Informe a fruta ou digite 'sair' para sair: ")
# while fruta != 'sair':
#     cesta.append(fruta)
#     fruta = input("Informe a fruta ou digite 'sair' para sair: ")
#
# print('\n')
#
# for x in cesta:
#     print(x)

cesta = []
while (fruta := input("Informe a fruta ou digite 'sair' para sair: ")) != 'sair':
    cesta.append(fruta)

print('\n')

for fruta in cesta:
    print(fruta)

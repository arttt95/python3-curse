qtd = int(input('Quantos valores serão passados?\n'))
soma = 0

for num in range(1, qtd + 1):
    print(f'insira o valor {num}/{qtd}:\n')
    valor = int(input())
    soma = soma + valor

print('O resultado da soma dos valores é:\n')
print(f'{soma:_}')
print('\nTks milhão Billy the Kid!')
print('\nDeus abençoe ao Sr. e todos da rede!')

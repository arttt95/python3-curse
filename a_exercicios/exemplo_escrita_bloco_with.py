with open('frutas.txt', '+a') as arquivo:
    while True:
        inserir = input('Adicione frutas a lista já existente: ')
        if inserir != 'sair':
            arquivo.write(inserir)
            arquivo.write('\n')
        else:
            arquivo.seek(0)
            print(arquivo.read())
            break

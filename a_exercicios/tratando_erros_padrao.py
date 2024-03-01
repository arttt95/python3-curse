def dividir(valor, divisor):
    try:
        return round(int(valor) / int(divisor), 4)

    except NameError as erra:
        print(f'Foi gerado o erro: NameError')
    except ValueError as errb:
        print(f'Foi gerado o erro: ValueError. Por favor insira um valor do tipo númerico!')
    except ZeroDivisionError:
        print('o número "0" não é um divisor válido! Por favor, tente novamente.')
    finally:
        print('Segue o resultado da sua divisão:')


num1 = input('Insira o valor que será dividido: ')
num2 = input('Insira o valor que será o divisor: ')

print(dividir(num1, num2))

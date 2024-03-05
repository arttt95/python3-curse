"""
POO - Abstração e Encapsulamento

           Classe
________________________________
|                              |
|          Atributos           |
|              &               |
|           Métodos            |
|______________________________|

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma *Classe* chamada *Pessoa*, contendo
um *ATRIBUTO PRIVADO* chamado '__nome' e um *MÉTODO PRIVADO*
chamado '__falar()'

Esses elementos privados só devem?deveriam ser acessados
dentro da *Classe*. Mas o Python não bloqueia este acesso
fora da *Classe*. Com Python acontece um fenômeno chamado
*Name Mangling*, que faz uma alteração na forma de se
acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Classe__atributo
instancia._Classe__metodo()

Ou seja:

instancia._Classe__nome
instancia._Classe__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes
de uma classe, escondendo atributos e métodos privados de
usuários.

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__titular} é de {self.__saldo} e com limite de'
              f'{self.__limite}!')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


cc1 = Conta('Tinky-Winky', 3450, 1_000)
cc2 = Conta('Godzilla', 4560, 15_500)

# Testando

print(cc1._Conta__numero)
cc1.extrato()
cc1.depositar(456)
cc1.extrato()
cc1.sacar(456)
cc1.extrato()

print('\n')

print(cc2._Conta__numero)
cc2.extrato()
cc2.depositar(456)
cc2.extrato()
cc2.sacar(5456)
cc2.extrato()

print(cc1)
print(cc2)

print('\n')

cc1._Conta__numero = 99
cc1._Conta__titular = 'Xuxa'
cc1._Conta__saldo = 999_999_999
cc1._Conta__limite = -999_999_999
print(cc1.__dict__)

"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__titular} é de {self.__saldo} e com limite de '
              f'{self.__limite}!')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor não pode ser negativo ou igual a R$ 0!')

    def sacar(self, valor):
        if valor > 10:
            if self.__saldo >= valor:
                 self.__saldo -= valor
            else:
                print('Você está tentando sacar um valor acima do saldo disponível em conta!')
                print(f'Por favor, digite um valor entre R$ {self.__saldo} e R$ 10')
        else:
            print('O valor precisa ser maior que R$ 10')

    def tranferir(self, valor, conta_destino):

        # 1 - Remover o valor da conta que irá tranferir o valor
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de tranferência, paga por quem está tranferindo o valor

        # 2 - Adicionar o valor a conta que irá receber a tranferência
        conta_destino.__saldo += valor



conta1 = Conta('Tinky-Winky', 3450, 1_000)
conta2 = Conta('Godzilla', 4560, 15_500)

conta1.depositar(-140)
print(conta1.__dict__)
print('\n')
conta1.sacar(-40)
print(conta2.__dict__)

print('\n')

conta1.extrato()
conta2.extrato()
conta1.tranferir(100, conta2)
conta1.extrato()
conta2.extrato()

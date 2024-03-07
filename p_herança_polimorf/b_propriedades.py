"""
POO - Propriedades (Properties)

Em linguagens de progrmação como o Java, ao declararmos atributos privados nas classes,
costumamos criar métodos públicos para manipulação desses atributos. Esses métodos são
conhecidos por getters e setters.
Onde os getters retornam o valor do atributo e os setters alteram o valor do mesmo.

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} de cliente {self.__titular}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def tranferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titulsr(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


cliente1 = Conta('Tinky-Winky', 4350, 10_000)
cliente2 = Conta('Itachi Uchiha', 4560, 2_000)

cliente1.extrato()
cliente1.sacar(50)
cliente1.extrato()

print('\n')

cliente1.extrato()
cliente2.extrato()
cliente1.tranferir(300, cliente2)
cliente1.extrato()
cliente2.extrato()

soma = cliente1.get_saldo() + cliente2.get_saldo()

print(f'\nA soma dos valores dos saldos das contas de cliente 1 e do cliente 2 são: '
      f'{soma}\n')

print(cliente1.__dict__)
cliente1.set_limite(999_999)
print(cliente1.__dict__)

"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} de cliente {self.__titular}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def tranferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor

    @property
    # Não é um método comum, é uma propriedade
    def valor_total(self):
        return self.__saldo + self.__limite


cliente1 = Conta('Tinky-Winky', 4350, 10_000)
cliente2 = Conta('Itachi Uchiha', 4560, 2_000)

cliente1.extrato()
cliente1.sacar(50)
cliente1.extrato()

print('\n')

cliente1.extrato()
cliente2.extrato()
cliente1.tranferir(300, cliente2)
cliente1.extrato()
cliente2.extrato()

soma = cliente1.saldo + cliente2.saldo

print(f'\nA soma dos valores dos saldos das contas de cliente 1 e do cliente 2 são: '
      f'{soma}\n')

print(cliente1.limite)
cliente1.limite = 999_999
print(cliente1.limite)

print(cliente1.valor_total)
print(cliente2.valor_total)

from passlib.hash import pbkdf2_sha256 as cryp
"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para
sua representação computacional, devemos poder criar quantos objetos quanto forem necessários.
Podemos pensar nos objetos/instâncias de uma clsse como variáveis do tipo definido na classe.

lass Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def liga_desliga(self):
        if not self.__ligada:
            self.__ligada = True
        else:
            self.__ligada = False
            

lamp1 = Lampada('Amarela', 110, 'Forte')

print('\n')

print(f'A lampada está ligada? {lamp1.checa_lampada()}')
lamp1.liga_desliga()
print(f'A lampada está ligada? {lamp1.checa_lampada()}')
lamp1.liga_desliga()
print(f'A lampada está ligada? {lamp1.checa_lampada()}')
lamp1.liga_desliga()
print(f'A lampada está ligada? {lamp1.checa_lampada()}')

cor = 'Branca'
voltagem = '110v'
luminosidade = 'Fraca'

lamp2 = Lampada(cor, voltagem, luminosidade)

print('\n')

print(type('Geek'))
print(type(13))
print(type(True))
print(lamp2)

"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def liga_desliga(self):
        if not self.__ligada:
            self.__ligada = True
        else:
            self.__ligada = False


class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def diz(self):
        return (f'O cliente {self.__nome} diz oi!')

class ContaCorrente:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        return f'Existem {cls.contador} usuário(s) no sistema!'


    def __init__(self, agencia, limite, email, senha, cliente):
        self.__id = ContaCorrente.contador + 1
        self.__agencia = agencia
        self.__conta = self.__id
        self.__limite = limite
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200_000, salt_size=16)
        self.__cliente = cliente
        ContaCorrente.contador = self.__id

    def __nickname(self):
        return self.__email.split('@')[0]

    def mostra_cliente(self):
        return (f'O cliente é o Sr(a) {self.__cliente._Cliente__nome} '
                f'{self.__cliente._Cliente__sobrenome}')


cliente1 = Cliente('Jackie', 'Chan', '987.654.321-00')
cliente2 = Cliente('Tinky', 'Winky', '123.456.789-69')

user1 = ContaCorrente('3141-0', 10_000,
                      'art@gmail.com', '123456', cliente1)
user2 = ContaCorrente('3141-0', 20_000,
                      'teletubs@gmail.com', '654321', cliente2)

print(user1._ContaCorrente__senha)
print(user2._ContaCorrente__senha)
print(ContaCorrente.conta_usuarios())

print(user1._ContaCorrente__nickname())
print(user2._ContaCorrente__nickname())

print(user1.mostra_cliente())
print(user2.mostra_cliente())

print(user1._ContaCorrente__cliente.diz())
print(user2._ContaCorrente__cliente.diz())

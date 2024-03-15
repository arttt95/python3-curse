"""
Por que testar nosso código?

Testes Automatizados!

         Aplicação Web
#--------------------------------#
#                                #
#     Front-End & Back-End       #
#                                #
#--------------------------------#
#                                #
#     Testes Automatizados       #
#                                #
#--------------------------------#

Por que testar nosso código?

    - Reduzir bugs no código existente;
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem)
    recursos antigos;
    - Testes rgarantem que bugs que foram corrigidos anteriormente continuem corrigidos;
    - Testes garantem que a refatoração que costumamos a fazer não tragam novos bugs;

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento:

    - Você escreve seu teste primeiro;
    - Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja,
    xecutar com sucesso);
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágio de desenvolvimento do TDD são quase como uma mantra que os desenvolvedores
seguem, conhecidos como:

    - Red;
    - Green;
    - Refactor;

"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'O {self.__nome} está miando...')


felix = Gato('Félix')

felix.miar()

print(felix.nome)

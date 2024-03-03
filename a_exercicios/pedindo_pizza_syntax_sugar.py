def pedindo_pizza(funcao):
    def atendendo_motoboy():
        print('Eai, boa noite!')
        funcao()
        print('Muito obrigado e bom trabalho!')
    return atendendo_motoboy


@pedindo_pizza
def pagando():
    print('Desculpa esqueci de pedir troco, toma essa nota de 100$!')


pagando()

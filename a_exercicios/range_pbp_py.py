def conta_ate(valor_maximo):
    numero = 1
    while numero <= valor_maximo:
        yield numero
        numero = numero + 1

gen = list(conta_ate(10))

print(gen)

print('\n')

class Contagem:


    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior


    def __iter__(self):
        return self


    def __next__(self):
        while True:
            if self.menor < self.maior:
                numero = self.menor
                self.menor = self.menor + 1
                return numero
            raise StopIteration


for n in Contagem(1, 21):
    print(n, end=',')

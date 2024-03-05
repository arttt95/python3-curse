class Exemplo:

    contador = 0

    def __init__(self, x, y, z):
        self.id = Exemplo.contador + 1
        self.__x = x
        self.__y = y
        self.__z = z
        Exemplo.contador = self.id

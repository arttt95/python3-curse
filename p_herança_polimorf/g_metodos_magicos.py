"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

# dunder init -> __init__()
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

Dunder -> Double Underscore

# dunder repr -> representação do objeto __repr__()
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'


"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória!')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += str(self) + ' '
            return msg
        return 'Não foi possível fazer a multiplicação. Por favor verifique os dados novamente!'

livro1 = Livro('Clean Code', 'Arthur', 300)
livro2 = Livro('Python Advanced', 'Arthur', 400)

print(livro1)
print(livro2)

print(len(livro1))
print(livro1 + livro2)

print(livro1 * 6)

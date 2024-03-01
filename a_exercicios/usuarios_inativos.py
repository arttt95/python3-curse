usuarios = [
    {"Usuário": "Billy", "Tweets": []},
    {"Usuário": "Mr. Enderson", "Tweets": ["Eu sou o NEO", "Temet Nosce!", "Vim acabar com a Matrix!"]},
    {"Usuário": "The Kid", "Tweets": []},
    {"Usuário": "Adm", "Tweets": ["Oba, feriado denovo!", "Meio espedeco, né família!"]},
    {"Usuário": "SJD", "Tweets": ["Vamos prender o mike!"]},
]

inativos = filter(lambda usuario: len(usuario["Tweets"]) == 0, usuarios)

print(inativos)
print(type(inativos))
print(list(inativos))

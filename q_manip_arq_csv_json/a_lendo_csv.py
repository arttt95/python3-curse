"""
Lendo arquivos CSV

CSV - Comma Separated Values - Valores Separados por Vírgulas

# Separador por vírgula

1, 2, 3, 4, 5, 6

"geek", "university", "python", "ciência", "dados"

# Separador por ponto e vírgula

1; 2; 3; 4; 5; 6

"geek"; "university"; "python"; "ciência"; "dados"

# Separador por espaço

1 2 3 4 5 6

"geek" "university" "python" "ciência" "dados"

http://dados.gov.br/dataset

# Possível de se trabalhar, mas não é o ideal (trabalhoso)

with open('../lutadores.csv') as arq:
    dados = arq.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas dos arquivos CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas dos arquivos CSV como OrderedDicts;

# Reader

from csv import reader

with open('../lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        # cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]}')

# Utilizando o DictReader com o delimiter padrão que é a vírgula ','
não é necessária nenhuma alteração nos parâmetros de entrada na execução do DictReader.

from csv import DictReader

with open('../lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} "
              f"e mede {linha['Altura (em cm)']}")
"""
# DictReader com outro separador: É necessário alterar o delimiter para o divisor desejado
# Exemplo abaixo:
# leitor_csv = DictReader(arquivo, delimiter=',')

from csv import DictReader

with open('../lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} "
              f"e mede {linha['Altura (em cm)']}")

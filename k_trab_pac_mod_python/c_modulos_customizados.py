"""
Módulos Customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS arquivos que criamos neste
curso são módulos Python prontos para serem utilizados.

# Importando uma função específica do nosso módulo
from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Import todo o módulo (Temos acesso a todos os elementos do módulo)
import funcoes_com_parametro as fcp

# Estamos acessando e imprimindo uma variável contido no módulo
print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))
"""
import a_a as apoio

#from map import cidades, c_para_f

print(list(map(apoio.c_para_f, apoio.cidades)))

print(apoio.lista)

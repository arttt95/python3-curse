# def multiplicar(num1: float, num2: float) -> float:
#     return num1 * num2
#
#
# resultado: float = multiplicar(4.5678, 5.6789)
#
# print(f'O resultado é {round(resultado, 2)}')
#
# print(f'O resultado é {multiplicar(4.5678, 5.6789):.2f}')
#
# print(f'{int(metade := 8 / 2)} é a metade de {int(metade * 2)}')

"""
####################################
##    * APRESENTANDO O VALOR *    ##
##       * DE UMA VARIÁVEL *      ##
####################################
"""

geek: str = 'Geek University'

print(f"geek = '{geek}'")  # Antes

print(f'{geek = }')  # Agora

print(f'{geek.upper()[::-1] = }')  # Mais elaborado

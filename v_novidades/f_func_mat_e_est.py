import math

"""
###########################################
##              * PRODUTO *              ##
###########################################
##              math.prod()              ##
##  * retorna o produto de um contador * ##
##              * numérico *             ##
###########################################
"""

nums_v1 = [2, 3, 4, 5]

nums_v2 = (2, 3, 4, 5)

nums_v3 = {2, 3, 4, 5}

print('math.prod()')
print(math.prod(nums_v1))
print(math.prod(nums_v2))
print(math.prod(nums_v2))

"""
###########################
##     2 * 3 * 4 * 5     ##
###########################
"""

"""
###########################################
##           * RAÍZ QUADRADA *           ##
###########################################
##              math.isqrt()             ##
##  * retorna a parte inteira da raiz *  ##
##      * quadrada de um número *        ##
###########################################
"""

print('\n')
print('math.isqrt()')
print(math.isqrt(9))
print(math.isqrt(17))
print('\n')
print('math.sqrt')
print(math.sqrt(9))
print(math.sqrt(17))

"""
###########################################
##         * DISTÂNCIA 2D E 3D *         ##
###########################################
##              math.dist()              ##
##  * retorna a distância euclidiana *   ##
##    * entre dois pontos, 2D ou 2D *    ##
###########################################
"""

# pontos 3D:
p3d1 = (15, 6, 78)
p3d2 = (5, 44, 13)

# pontos 2D:
p2d1 = [13, 17]
p2d2 = [5, 56]

print('\n')
print('math.dist()')
print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

"""
###########################################
##             * HIPOTENUSA *            ##
###########################################
##             math.hypot()              ##
##      * retorna a hipotenusa, ou *     ##
##         * a norma Euclidiana *        ##
###########################################
"""

print('\n')
print('math.hypot()')
print((math.hypot(*p3d1)))
print(math.hypot(*p2d1))

"""
##########################################
##           * ESTATÍSTICA *            ##
##########################################
##           statistics.fmean()         ##
## * calcula a média de números reais * ##
##########################################
"""
import statistics

valores_reais = [1.23, 3.456, 6.754, 6.43]
valores_inteiros = [2, 3, 5, 4, 57]

print('\n')
print('statistics.fmean()')
print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))

"""
##########################################
##         * MÉDIA GEOMETRICA *         ##
##########################################
##           geometric_mean()           ##
##    * calcula a média geométrica *    ##
##         * de números reais *         ##
##########################################
"""

print('\n')
print('statistics.geometric_mean()')
print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))

"""
##########################################
##         * MAIOR FREQUÊNCIA *         ##
##########################################
##              multimode()             ##
##  * retorna o valor mais frquente *   ##
##         * em uma sequência *         ##
##########################################
"""

seq1 = 'Geek University'
seq2 = [3, 4, 5, 6, 4, 3, 3, 4]
seq3 = [1, 2, 3, 4, 4, 5, 6, 2]

print('\n')
print('multimode()')
print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))

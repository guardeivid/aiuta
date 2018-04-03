#import el <paquete>.<modulo>
"""
from calculos.calculos_generales import dividir, potencia, redondear
dividir(24,5)
potencia(8,4)
redondear(8.5)
"""

#si estan dentro de submodulos, hay que especificar toda la ruta, si no estan instalados
from calculos.basicos.operaciones_basicas import *
sumar(4,78)

from calculos.redondeo_potencia.redondeaYpotencia import *
redondear(4.78)

# si esta instalado desde cualquier lugar lo lee, solo hay que especificar el nombre del modulo
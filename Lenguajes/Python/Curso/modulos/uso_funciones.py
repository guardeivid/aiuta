#para utilizar un modulo hay que importarlo

#Importar todo lo que tiene el modulo
#1- import <modulo>, , los nombres se utilizan a traves del espacio de nombres del modulo
import funciones_matematicas
funciones_matematicas.sumar(4, 8)

#2- from <modulo> import *, los nombres se utilizan directamente
from funciones_matematicas import *
sumar(8, 7)
multiplicar(5,6)

#Importar parte de lo que tiene un modulo
from funciones_matematicas import sumar, restar
sumar(8, 7)
restar(5,6)

"""
para llamar a un modulo y encontrarlo debe estar en el mismo directorio 
desde donde se lo esta llamando

si no lo encuentra busca en el "syspath"

para que lo encuentre desde cualquier lado es por medio de "paquetes"
"""
#serializacion de una lista
import pickle

lista_nombre=["Pedro", "Ana", "Maria", "Isabel"]

#crear archivo externo binario con modo escritura
fichero_binario=open("20-lista_nombres_binario", "wb")

#informacion a volcar, y archivo en memoria
#p2 es necesario declarar un tercer parametro, el protocolo
# 0 en formato ASCII - defecto p2 -
# 1 en formato binario viejo
# 2 en formato binario nuevo = pickle.HIGHEST_PROTOCOL
pickle.dump(lista_nombre, fichero_binario, 2)

#si el archivo llega al final lo cierra
fichero_binario.close()

#igualmente se puede vaciar de la memoria
del fichero_binario


#----------leer serializacion de un archivo binario---------
fichero_binario2=open("20-lista_nombres_binario", "rb")
lista_nombre2=pickle.load(fichero_binario2)
print(lista_nombre2)


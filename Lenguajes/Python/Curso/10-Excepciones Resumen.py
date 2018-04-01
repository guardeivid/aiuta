print "Bienvenido"
try:
	print l
except:
	print "error en la ejecucion"
print "adios"

#------------------------------------
try:
	print l
except (TypeError, NameError):
	print "error en el tipo de dato"
print "adios"

#------------------
#------------------------------------

try:
	print 5
except TypeError:
	print "error en el tipo de dato"
except NameError:
	print "la variable no existe"
except ZeroDivisionError:
	print "no se puede dividir por 0"
else:
	# se ejecuta despues del try si no hubo un error
	print "no hubo error"
finally:
	print "me ejecuto pase lo que pase"
print "adios"


#--------------------------

class UnoError(Exception):
	def __init__(self, valor):
		self.valorError = valor
	def __str__(self):
		print " no se puede dividir entre 1 el numero:", self.valorError

d = 5
n = 1
try:
	if n == 1:
		# lanzo un error manualmente, si no esta dentro del try, se ejecutaria __str__
		raise UnoError(d)
except UnoError:
	print "se ha producido un error que yo mismo cree"
	print ""


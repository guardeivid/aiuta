logueado = True
usuario = "alguien"

def admin(f):
	def comprobar(*args, **kwargs):
		if logueado:
			f(*args, **kwargs)
		else:
			print "No tiene permisos de ejecutar", f.__name__
	return comprobar

def decorador(fx):
	#*args = recibe una n lista de argumentos
	#**kwargs = recibe un diccionario de argumentos con claves
	def funcionDecorada(*args, **kwargs):
		print "funcion ejecutada", fx.__name__
		fx(*args, **kwargs)
	return funcionDecorada

# Concatenando decoradores
@admin
@decorador
def resta(n, m):
	print n - m

# Decorando
# decorador(resta)(5, 3)
# funcion ejecutada  resta
# 2

# Ahora se simplifica la sintaxis escribiendo 
# @nombreDecorador seguido la funcion que se desea decorar
resta(3, 5)

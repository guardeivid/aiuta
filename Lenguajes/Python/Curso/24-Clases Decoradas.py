class Decorador(object):
	"""Mi clase decoradora"""
	def __init__(self, fx):
		self.fx = fx
	# funcion que sirve como funcion decorada
	def __call__(self, *args, **kwargs):
		print "funcion ejecutada", self.fx.__name__
		self.fx(*args, **kwargs)
		
@Decorador
def resta(n, m):
	print n - m

resta(3, 5)



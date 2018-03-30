def suma(n1, n2):
	return n1+n2

def resta(n1, n2):
	return n1-n2

def multiplica(n1, n2):
	return n1*n2

def divide(n1, n2):
	try:
		return n1/n2
		# si la excepcion no es la que queremos capturar, el programa tambien se detendra
	except ZeroDivisionError:
		print("no se puede dividir entre 0")
		return "operacion erronea"

while True:
	try:
		op1=(int(input("numero 1: ")))
		op2=(int(input("numero 2: ")))
		break
	except ValueError:
		print("los valores introducidos no son correctos, vuelva a intentarlo")

operacion=(input("operacion a realizar (suma, resta, multiplica, divide): "))

if operacion== "suma":
	print(suma(op1, op2))
elif operacion== "resta":
	print(resta(op1, op2))
elif operacion== "multiplica":
	print(multiplica(op1, op2))
elif operacion== "divide":
	print(divide(op1, op2))	
else:
	print("operacion no contemplada")

# continua el programa
print("operacion ejecutada")

# ej si se divide por 0, da error, y no se continua la ejecucion
# captura o control de excepcion, intentando realizar una instruccion, y en caso que no puedas, continua con las siguientes instrucciones
"""
numero 1: 8
numero 2: 0
operacion a realizar (suma, resta, multiplica, divide): "divide"
Traceback (most recent call last):
  File "Execpciones.py", line 24, in <module>
    print(divide(op1, op2))
  File "Execpciones.py", line 11, in divide
    return n1/n2
ZeroDivisionError: integer division or modulo by zero
"""
# pila de llamadas, la ultima es la que da el error
# capturar con try: except ZeroDivisionError:

#---------------------------------
# capturas simultaneas de diferentes tipos de errores

def divide1():
	try:
		op1=(float(input("introduce el primer numero: ")))
		op2=(float(input("introduce el segundo numero: ")))
		print("la division es: " + str(op1/op2))
	except ValueError:
		print("el valor introducido es erroneo")
	else ZeroDivisionError:
		print("no se puede dividir entre 0")
"""
	except Exception as e:
		raise e
	#captura general
	except:
		print("ha ocurrido un error")
	"""
	finally:
		#esto se va a ejecutar siempre
		print("calculo finalizado")

	
	

divide1()




import random
import time

piedra = 1
papel = 2
tijera = 3

puntos_jugador = 0
puntos_computadora = 0

nombres = {piedra: "Piedra", papel: "Papel", tijera: "Tijera"}
reglas = {piedra: tijera, papel: piedra, tijera: papel}

def empieza():
	print "Bienvenido al juego Piedra, Papel y Tijera"
	print "-"*42
	while juego():
		pass

def juego():
	jugador = movimiento()
	computadora = random.randint(1,3)
	resultado(jugador, computadora)
	return juega_otra_vez()

def movimiento():
	while True:
		jugador = raw_input("Selecciona una opcion [1=Piedra, 2=Papel, 3=Tijera]: ")
		try:
			jugador = int(jugador)
			if jugador in (1,2,3):
				return jugador
		except ValueError:
			pass
		print "Por favor selecciona [1, 2 o 3]"

def resultado(jugador, computadora):
	print "Piedra...",
	time.sleep(0.5)
	print "Papel...",
	time.sleep(0.5)
	print "Tijera!"
	time.sleep(0.2)
	print "La computadora escogio {0}".format(nombres[computadora])
	global puntos_jugador, puntos_computadora
	if jugador == computadora:
		print "\"Empate!!!\""
	else:
		if reglas[jugador] == computadora:
			print "\"Ganaste!!!\""
			puntos_jugador += 1
		else:
			print "\"Bua, Perdiste!!!\""
			puntos_computadora +=1

def juega_otra_vez():
	puntos()
	respuesta = raw_input("Quieres jugar otra vez SI=[s, Enter]: ")
	if respuesta in ("1", "si", "s", "SI", "Si", "y", "yes", ""):
		return True
	else:
		print "Gracias por jugar, nos vemos!"

def puntos():
	global puntos_computadora, puntos_jugador
	print
	print "Resultados:"
	print "Jugador:", puntos_jugador
	print "Computadora:", puntos_computadora
	print

empieza()
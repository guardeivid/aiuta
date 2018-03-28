miDiccionario = { "Alemania": "Berlin", "Francia": "Paris", "Reino Unido": "Londres", "Espana": "Madrid"}

# acceder por la clave
print(miDiccionario["Francia"])

# acceder a todos
print(miDiccionario)

# agregar un nuevo par clave:valor
miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)

# modificar un valor, sobreescribe porque no puede haber dos claves iguales
miDiccionario["Italia"] = "Roma"
print(miDiccionario)

# eliminar un elemento
del miDiccionario["Reino Unido"]
print(miDiccionario)

# con diferentes tipos
miDiccionario2 = { "Alemania": "Berlin", 23: "Jordan", "Mosqueteros": 3}
print(miDiccionario2)

# asignar una tupla o lista a los valores o claves de un diccionario, funciona en version 3
"""
mitupla=["Francia", "Alemania", "Belgica", "Inglaterra"]
miDiccionario3=[mitupla[0]:"Francia", mitupla[1]:"Alemania", mitupla[2]:"Belgica", mitupla[3]:"Inglaterra"]
print(miDiccionario3)

milista=["Francia", "Alemania", "Belgica", "Inglaterra"]
miDiccionario4=[milista[0]:"Francia", milista[1]:"Alemania", milista[2]:"Belgica", milista[3]:"Inglaterra"]
print(miDiccionario4)
"""

miDiccionario5 = { 
23: "Jordan", 
"Nombre":"Michael", 
"Equipo":"Chicago", 
"anillos": {"temporadas":[1991,1992,1993,1996,1997,1998]}
}
print(miDiccionario5["anillos"]["temporadas"][0])


# obtener las claves
print(miDiccionario5.keys())

# obtener las valores
print(miDiccionario5.values())

# obtener la longitud del diccionario
print(len(miDiccionario5))
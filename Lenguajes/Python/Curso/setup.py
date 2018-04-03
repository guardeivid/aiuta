from setuptools import setup

setup(
	name="paquetecalculos", #nombre del paquete 
	version="1.0.0",
	description="Paquete de redondeo y potencia",
	author="Juan",
	author_email="cursos@pil.com",
	url="www.pil.com",
	#mas importante que se quiere empaquetar
	packages=[
		"calculos",
		"calculos.redondeo_potencia"
	] 

)
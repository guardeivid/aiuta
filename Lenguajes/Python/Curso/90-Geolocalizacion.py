#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

# instalar
# pip install geopy
# 

"""
from geopy.geocoders import Nominatim

punto = "22.1577057, -102.2731303"

geolocation = Nominatim()
result = geolocation.reverse(punto)
print result.address # direccion
print(result.latitude, result.longitude)
print result.raw # json

#-------------------------------
from geopy.geocoders import GoogleV3

geolocation = GoogleV3()
try:
	result = geolocation.reverse(punto)
	#print str(result[0]).encode('utf-8')
	print u' '.join((result[0])).encode('utf-8').strip()
	print (result[0]) # direccion
except Exception as e:
	print e

#a = "Pabellón de Arteaga, Aguascalientes, 20620, México"
#print a.decode('unicode-escape')

# si da error de timeout, 
# aumentar el valor de la variable DEFAULT_TIMEOUT = 1
# en python/lib/site-package/geopy/geocoders/base-py
"""


#########################################################
#otra manera
# pip install geocoder
# 
import geocoder

#latlon = geocoder.google("San Diego, California")
#print ("San Diego, California", latlon.latlng)

# reverse
#direccion = geocoder.google([45.1221, 54.1212], method="reverse")
#print direccion.city, direccion.state_long, direccion.country_long

postal_zip = geocoder.google("300 Post Street, San Francisco, CA")
print postal_zip.postal
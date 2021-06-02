# Este script averigua el mensaje de CESAR por Fuerza Bruta

from alfabetos import alfabeto_full
alfabeto_cifrado = alfabeto_full()#"ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Alfabeto cifrado
#FMJY KSLBM
mensaje_cifrado = "IPMB NVOEP" #Aqui va el texto cifrado
mensaje_plano = "" #Aqui el resultado

for clave in range(1, len(alfabeto_cifrado)):
	
	mensaje_plano = ""
	
	for letra in mensaje_cifrado.upper():

		if letra in alfabeto_cifrado:
			posicion = alfabeto_cifrado.index(letra) #Obtenemos la posicion de la letra
			posicion = (posicion - clave) % len(alfabeto_cifrado) #Desplazamos la posicion a la izquierda
			mensaje_plano += alfabeto_cifrado[posicion] #Obtenemos la nueva letra para esa posicion

		else: #Si la letra no esta
			mensaje_plano += letra

	print("\nClave {}: {}".format(clave, mensaje_plano)) #Mostramos por pantalla

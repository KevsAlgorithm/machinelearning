#Este script cifra mediante CESAR

#Aritmetica modular (posicion + saltos) % nElementos

#              c=3  XYZABCDEFGHIJKLMNOPQRSTUVW
#              c=4  WXYZABCDEFGHIJKLMNOPQRSTUV
#              c=10 QRSTUVWXYZABCDEFGHIJKLMNOP

from alfabetos import alfabeto_may
alfabeto_cifrado = alfabeto_may()#"ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Alfabeto cifrado

mensaje = "FMJY KSLBM"#Aqui va el texto plano
mensaje_cifrado = "" #Aqui va el texto cifrado

#Vamos a elegir la cantidad de desplazamientos
clave = 3

cifrado = True # Si es True, entonces se cifra (Desplazmoa a la derecha); Caso contrario, desciframos (Desplazamos a la izquierda)


for letra in mensaje.upper(): #Para cada letra del mensaje

	if letra in alfabeto_cifrado: #Si la letra esta en el alfabeto
		posicion = alfabeto_cifrado.index(letra) #Obtenemos la posicion de la letra

		if cifrado == True:
			formula = (posicion + clave) % len(alfabeto_cifrado) #Desplazamos la posicion a la derecha
		else:
			formula = (posicion - clave) % len(alfabeto_cifrado) #Desplazamos la posicion a la izquierda

		mensaje_cifrado += alfabeto_cifrado[formula] #Obtenemos la nueva letra para esa posicion

	else: #Si la letra no esta
		mensaje_cifrado += letra

print("Texto plano: {}".format(mensaje))
print("Texto cifrado: {}".format(mensaje_cifrado))
#Cifrado por transposicion columnar

#Eliminara espacios en blanco

#Agrupara el texto en letras

#Funcion de cifrado

mensaje_plano = "El bombardeo sera por la tarde a las dos" #Aqui va el texto plano
clave = 8 #El numero de columnas

print(mensaje_plano)

#Funcion para eliminar
def eliminarEspacios(texto):
	mensajeUnido = "" #Aqui se almacena el mensaje unido
	for letra in texto:
		if letra == " ":
			pass #No hacemos nada
		else:
			mensajeUnido += letra #Añadimos la letra

	return mensajeUnido #Devolvemos el mensaje unido sin espacios

#mensajeNuevo = eliminarEspacios(mensaje_plano)
#print(mensajeNuevo)

def agrupar(texto, n):
	mensajeGrupo = "" #Aqui se almacena el mensaje de grupos de letras
	grupo = n #Numero de letras por grupo

	for i in range(0, len(texto)):
		if i%grupo == 0 and i != 0:
			mensajeGrupo += " " #Añadimos separacion
			mensajeGrupo += texto[i] #Añadimos la letra en la posicion i perteneciente al texto
		else:
			mensajeGrupo += texto[i] #Solo añadimos la letra

	return mensajeGrupo

#mensajeNuevo = eliminarEspacios(mensaje_plano)
#mensajeNuevo = agrupar(mensajeNuevo, 3)
#print(mensajeNuevo)

#Funcion cifrado transposicion
def cifrar(texto, clave):
	mensaje_cifrado = [""]*clave #Aqui se almacena el mensaje cifrado

	for columna in range(clave):
		pos = columna

		while pos < len(texto): #Mientras la posicion sea menor que la longitud del mensaje
			mensaje_cifrado[columna] += texto[pos] #Añadimos al primer grupo de letras lo que haya en la posicion
			pos += clave #Hemos de sumar la clave

	#'-'.join(mensaje_cifrado)

	return ''.join(mensaje_cifrado)

mensajeNuevo = eliminarEspacios(mensaje_plano)
mensajeNuevo = cifrar(mensajeNuevo, clave)
print(mensaje_plano)
print(mensajeNuevo)

#Ahora implementaremos la funcion agrupar
mensaje_cifrado = agrupar(mensajeNuevo, 2)
print(mensaje_cifrado)


###################

def main():
	print("\nhola main!")
	mensaje_plano = "El bombardeo sera por la tarde a las dos" #Aqui va el texto plano
	clave = 8 #El numero de columnas

	mensaje_plano = eliminarEspacios(mensaje_plano)
	mensaje_cifrado = cifrar(mensaje_plano, clave)
	mensaje_cifrado = agrupar(mensaje_cifrado, 4)

	print("Texto Plano: {}".format(mensaje_plano))
	print("Texto Cifrado: {}".format(mensaje_cifrado))
#Permite que al ejecutar el script Python encuentre las funciones
if __name__ == '__main__':
	main()
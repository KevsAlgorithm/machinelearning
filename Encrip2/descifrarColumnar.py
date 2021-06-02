# Descifrar la transposicion columnar

import math 

def main():
	mensaje_cifrado = "AQNAU RTUAS AOAEL CT" #Aqui va el mensaje
	clave = 3

	mensajeNuevo = eliminarEspacios(mensaje_cifrado)
	mensaje_plano = descifrar(mensajeNuevo, clave).lower()
	print("Texto Cifrado: {}".format(mensajeNuevo))
	print("Texto Plano: {}".format(mensaje_plano))

#Funcion para eliminar
def eliminarEspacios(texto):
	mensajeUnido = "" #Aqui se almacena el mensaje unido
	for letra in texto:
		if letra == " ":
			pass #No hacemos nada
		else:
			mensajeUnido += letra #Añadimos la letra

	return mensajeUnido #Devolvemos el mensaje unido sin espacios

#Funcion para descifrar
def descifrar(texto, clave):

	num_filas = clave #El numero de filas equivale a la clave
	num_col = math.ceil(len(texto)/clave) #El metodo ceil nos devuelve el entero siguiente
	celdas_vacias = num_filas * num_col - len(texto) #Calculamos el numero de letras vacias

	texto_plano = [''] * num_col #Creamos una lista con tantos elementos como columnas

	print(texto_plano)
	col = 0
	fila = 0

	for letra in texto:

		texto_plano[col] += letra
		col += 1

		if (col == num_col) or (col == num_col - 1 and fila >= num_filas - celdas_vacias):
			col = 0
			fila += 1

	return ''.join(texto_plano)


if __name__ == '__main__':
	main()
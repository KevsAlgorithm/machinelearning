#script que cifra o descifra mediante sustitucion simple

from alfabetos import alfabeto_may #importamos alfabeto mayusculas
import random

def main():
	alfabeto = alfabeto_may() #generamos nuestro alfabeto
	print(alfabeto)
	clave = clave_aleatoria(alfabeto) #generamos la clave aleatoria
	print("hola {}".format(clave))
	mensaje = "El bombardeo sera por la tarde" #Aqui va el mensaje
	mensaje = mensaje
	print(mensaje)
	criptograma = cod_mensaje(mensaje, clave, alfabeto) #ciframos el mensaje
	print(criptograma)


def cod_mensaje(texto_plano, clave, alfabeto):#funcion para cifrar o descifrar
	texto_cifrado = "" #aqui va el texto cifrado
	for letra in texto_plano:#para cada letra del texto plano
		if letra in alfabeto: #si la letra esta en el alfabeto
			pos = alfabeto.index(letra) #obtenemos posicion
			letra_cifrada = clave[pos] #obtenemos letra correspondiente
			texto_cifrado += letra_cifrada

		else: #si la letra no esta en el alfabeto
			letra_cifrada = letra #no ciframos la letra
			texto_cifrado += letra_cifrada

	return texto_cifrado


def clave_aleatoria(letras):
	letras_lista = list(letras)
	random.shuffle(letras_lista)
	#print(letras_lista)

	return ''.join(letras_lista)

if __name__ == '__main__':
	main()
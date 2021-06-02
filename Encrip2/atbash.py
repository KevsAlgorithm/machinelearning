#Cifrador Atbash

#alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Alfabeto plano

#cifra = "ZYXWVUTSRQPONMLKJIHGFEDCBA" #Alfabeto cifra

from alfabetos import alfabeto_min, alfabeto_may_inv

alfabeto = alfabeto_min()#"ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Alfabeto plano
cifra = alfabeto_may_inv()#"ZYXWVUTSRQPONMLKJIHGFEDCBA" #Alfabeto cifra

print(cifra)
mensaje = "Hola Mundo" #Aqui va el mensaje
mensaje = mensaje.lower() #Convertimos el mensaje a mayusculas

#Recorrer cada uno de los caracteres del mensaje y obtener su posición en el alfabeto
#así para la posición en cifra para realizar el intercambio

mensaje_cifrado = "" #Aqui va el mensaje cifrado

for letra in mensaje: #Recorremos todas las letras de mensaje

	if letra in alfabeto: #Comprobamos que la letra esta en el alfabeto
		posicion = alfabeto.index(letra) #Obtener la posicion de la letra en el alfabeto
		letra_cifrada = cifra[posicion] #Obtener la letra en el alfabeto cifra
		mensaje_cifrado += letra_cifrada #Añadimos la letra cifrada al mensaje 

	else:
		mensaje_cifrado += letra #Si la letra no esta en el alfabeto, añadimos la letra sin cifrar

print("Texto plano: {}".format(mensaje))
print("Texto cifrado: {}".format(mensaje_cifrado))
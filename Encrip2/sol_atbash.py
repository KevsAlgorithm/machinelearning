#Solucion al cifrador Atbash

alfabeto_cifrado = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
alfabeto_plano = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

mensaje_cifrado = "sloz nfmwl" #Aqui va el mensaje cifrado
mensaje_plano = "" #Aqui va el mensaje plano

for letra in mensaje_cifrado.upper(): #Transformamos a mayusculas el texto cifrado

	if letra in alfabeto_cifrado: #Si la letra existe, buscar posicion
		posicion = alfabeto_cifrado.index(letra)
		letra_plana = alfabeto_plano[posicion] #Relacionamos la posicion con la letra
		mensaje_plano += letra_plana

	else:
		mensaje_plano += letra #Si la letra no esta en el alfabeto, añadimos


print("Texto cifrado: {}".format(mensaje_cifrado))
print("Texto plano: {}".format(mensaje_plano))
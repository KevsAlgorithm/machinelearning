#Script para detectar un idioma

# def leerDiccionario(archivo_diccionario): #Lee el nombre del archivo diccionario.txt
# 	miDiccionario = open(archivo_diccionario)#Abrimos el archivo de texto

# 	for palabra in miDiccionario.read():
# 		print(palabra)

# leerDiccionario('diccionario.txt')

def leerDiccionario2(archivo_diccionario): #Lee el nombre del archivo diccionario.txt
	miDiccionario = open(archivo_diccionario)#Abrimos el archivo de texto

	for palabra in miDiccionario.read().split('\n'):
		print(palabra)
		

leerDiccionario2('diccionario.txt')


# def leerDiccionario(archivo_diccionario): #Lee el nombre del archivo diccionario.txt
# 	miDiccionario = open(archivo_diccionario)#Abrimos el archivo de texto

# 	dic_palabras = {} #Diccionario para almacenar las palabras

# 	for palabra in miDiccionario.read().split('\n'):
# 		dic_palabras[palabra] = 0

# 	return dic_palabras

def detectarIdioma(mensaje, diccionario): #espanol.txt, ingles.txt....
	diccionario = leerDiccionario(diccionario) #cargamos el diccionario deseado
	mensaje = mensaje.upper() #convertimos mensaje a mayusculas

	l_texto = 0 #se almacena la longitud total de las palabras con sentido
	l_total = len(mensaje) #longitud total del mensaje

	for palabra in diccionario:
		if mensaje.find(palabra) == -1: #sumamos la longitud de la palabra
			pass
		else:
			l_texto += len(palabra) #sumamos la longitud de la palabra
			print(palabra)

	ratio = l_texto / l_total #calculamos el ratio de riqueza lexica

# 	if ratio >= 0.5:
# 		return True, ratio
# 	else:
# 		return False, ratio


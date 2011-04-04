#! /usr/bin/python

# Listas

# Es una coleccion ordenada que puede contener cualquier tipo de dato

lista = [22, True, "lista", [1,2]]
print lista

# Acceso a una lista

elem3 = lista[3]
print elem3

# Acceso a una sublista

elem32 = lista[3][1]
print elem32

# Podemos recorrer tambien la lista de atras hacia delante
# usando indices negativos

elem2 = lista[-2]
print elem2

# Python tambien nos ofrece la posibilidad de seleccionar particiones (slicing)
# de la lista mediante rangos, bien sea (inicio:fin) o (inicio:fin:salto)

part = lista[0:2]
print part

part = lista[0:4:2]
print part

# si omitimos el primer o el segundo valor del slicing se tomaran por
# defecto el principio o el final de la lista respectivamente

part = lista[:]
print part

part = lista[2:]
print part

# podemos usar este mecanismo para modificar el contenido de las listas 
# e incluso su tamanho

lista[0:2] = [0,1]
print lista

lista[0:2] = [False]
print lista


# Tuplas 

t = (12,"tupla",True)
print t

# Podemos aplicar todo lo dicho sobre las listas a las tuplas, salvo la 
# modificacion en tiempo de ejecucion, las tuplas son inmutables, no podremos
# modificar su tamanho ni su contenido una vez creadas
# Tienen una ventaja sobre las listas, son mas eficientes espacialmente

# Diccionarios

# Son colecciones de pares clave:valor

dir_pelis = {"Love Actually" : "Richard Curtis",
		 "Kill Bill" : "Quentin Tarantino",
		 "Amelie" : "Jean-Pierre Jeunet"}
print dir_pelis
		
# Los diccionarios no son colecciones ordenadas, para acceder 
# a sus elementos utilizamos su clave y no un indice

kill = dir_pelis["Kill Bill"]
print kill

# Se trata de un mapping que establece una relacion
# entre un valor y una clave

# Es posible utilizar cualquier valor inmutable como clave
# No podemos utilizar valores mutables porque los diccionarios
# estan implementado como tablas hash



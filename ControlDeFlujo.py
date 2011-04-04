#! /usr/bin/python

# Los mecanismos de control de flujo son los habituales:


# Sentencias condicionales

# if 

te_gusta_python = True
if te_gusta_python == True:
	print "Normal..."
	
# Aqui podemos mencionar el tema de la indentacion: en otros 
# lenguajes la indentacion es una cuestion de estilo y legibilidad,
# en Python, al prescindir de llaves u otros elementos para delimitar 
# los bloques en favor de la claridad, la indentacion se convierte en algo 
# obligatorio.

# if ... else ...

if te_gusta_python == True:
	print "Normal..."
else:
	print "Seguro?"
	
# if ... elif ... elif [...] else
numero = 6

if numero < 0: 
	print "Negativo"
elif numero > 0:
	print "Positivo"
else:
	print "Cero"
	

# A if C else B

num = 3
var = "par" if (num % 2 == 0) else "impar"
print num
print var


# Bucles

# While

edad = 21

while edad < 26:
	edad = edad + 1
	print "Con " + str(edad) + "anhos y todavia estudiando?" 

# Interrupcion del flujo: break, continue

# Este pequenho trozo de codigo se repite hasta que el usuario escribe "adios"

while True:
	entrada = raw_input("> ")
	if entrada == "adios":
		break
	else: 
		print entrada
		
i = 0
while i < 10:
	i = i + 1
	if i%2 == 1:
		continue
	print str(i) + " numero par"
	
# for ... in

secuencia = ["uno","dos","tres","cuatro"]
for elemento in secuencia:
	print elemento


		 

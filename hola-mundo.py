# 1. TAREA: imprimir "Hola mundo"
print("Hola mundo")
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Noelle"
print("Hello ",name,"!" )	# con una coma
print("Hello "+name+"!" )	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
nunmber = 42
print("Hello ",nunmber,"!" )	# con una coma
#  print("Hello "+nunmber+"!" )	# con un + - !Este debería darnos un error!
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Me encanta comer {} and {}".format(fave_food1, fave_food2)) # con .format()
print(f"Me encanta comer {fave_food1} and {fave_food2}") # con una cadena f
# PARTE 2
print("Hola mundo!")
minomb = "Alex"
print("Hola ", minomb,"!")
numfav = str(7)
print("Hola "+ numfav) #solo puedo concatenar string + string, se corrige el error incorporando "int()" a la variable
com_fav1 = "Papas fritas"
com_fav2 = "Queso"
print("Me encanta comer {} y {}".format(com_fav1, com_fav2)) # con .format()
print(f"Me encanta comer {com_fav1} y {com_fav2}") # con una cadena f
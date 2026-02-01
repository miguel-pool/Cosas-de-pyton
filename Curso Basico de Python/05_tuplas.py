### TUPLAS ###
# LA TUPLA ES INMUTABLE, NO ES MODIFICABLE PARA AGREGAR VALORES DESPUES DE HABERLOS ASIGNADO, MANTIENE LOS VALORES CONSTANTES
# PARA CAMBIAR VALORES HAY QUE UTILIZAR UNA LISTA

my_tuple = tuple() # 1ra Forma de Definir una Tupla
my_other_tuple = () # Forma directa de definirla

my_other_tuple = (25, 20, 30, 45, 50)
my_tuple = (18, 1.82, "Victor", "Ramirez", "Victor")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0]) # Igual que en listas, podemos elegir el valor que queremos
print(my_tuple[-2]) # Lo mismo a la inversa
#print(my_tuple[5]) IndexError "Porque no hay suficientes datos en los cuales buscar"
#print(my_tuple[-5]) IndexError "Lo mismo"

print(my_tuple.count("Victor")) # Cuenta la cantidad de un mismo dentro de una tupla, en este caso es el valor "Victor"
print(my_tuple.count(18))
print(my_tuple.index("Ramirez")) #La ubicacion del indice dentro de la lista, en orden de primero a ultimo

#my_tuple[-2] = "Bustamante" # No se pueden reasignar valores en la tupla, solo son los valores asignados en principio, osea, constantes.
#print(my_tuple)


Suma_Tuplas = (my_tuple + my_other_tuple) # unificar en una variable
print(my_tuple + my_other_tuple) # Suma de las tuplas "Fusion"
print(Suma_Tuplas)

print(Suma_Tuplas[3:6]) # Para buscar entre valores

# LA UNICA FORMA DE CAMBIAR UN VALOR ES HACIENDO UNA LISTA DE LA TUPLA, MODIFICANDO EL VALOR Y LUEGO HACERLA TUPLA OTRA VEZ

del my_tuple # Borra la tupla y deja de tener valor completo, osea, deja de existir valor para "my_tuple"
#print(my_tuple) # NameError: name 'my_tuple' is not defined





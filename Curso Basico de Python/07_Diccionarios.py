### Diccionarios ###

my_dict = dict()
my_other_dict = {} # Puede definir un set o diccionario, pero en principio, es un DICT

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre:":"Victor", "Apellido":"Ramirez", "Edad":18, 1:"Vitico"} # Es calve-valor, se le asigna un valor a la clave
print(my_other_dict)
print(type(my_other_dict))

my_dict = {"Nombre:":"Victor", "Apellido":"Ramirez", "Edad":18, "Lenguajes":{"Python", "JavaScript", "C++"}, 1:1.82} # El valor puede ser un set
print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Lenguajes"]) # Busco la clave y me imprimira el valor de la clave, en este caso, los lenguajes dentro de la clave "lenguaje"

my_dict["Nombre"] = "Pepe" # Podemos cambiar el valor dentro de la clave de esta manera
print(my_dict["Nombre"])

my_dict["Calle"] = "San Juan" # Se pueden agregar mas clave-valor de esta manera
print(my_dict)

#my_dict.remove no existe, la forma de eliminar un dato es la siguiente:
del my_dict["Calle"]
print(my_dict)

print("Apellido" in my_dict) # Buscamos los datos por clave, no por contenido de la clave
print("Victor" in my_dict)

print(my_dict.items()) # Nos da un listado de los conjuntos de clave-valor del dict
print(my_dict.keys()) # No da solo las claves del dict
print(my_dict.values()) # Nos da los valores de la claves

# Para crear un diccionario con claves
my_new_dict = dict.fromkeys(("Nombre", 1, "Fecha")) # Podemos crear un dict pero que no tiene valores
print(my_new_dict)
# Tambien podemos pasarle una lista para que tenga las claves de la lista
my_list = ["Nombre", 1, "Fecha"]
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
# Le podemos pasar un diccionario y pasa solo las claves sin valor
my_new_dict = dict.fromkeys((my_dict)) 
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Hola") # Agrega SOLO el valor que pongamos. A todas las claves, porque no puede identificar cual va para cual
print(my_new_dict)

valores = my_dict.values()
print(type(valores))

# Solo nos imprime las claves
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))

# Tambien podemos imprimir solo los valores haciendo lo siguiente:
print(list(my_new_dict.values())) # [] en orden
print(tuple(my_new_dict.values())) # () en orden
print(set(my_new_dict.values())) # {} Sin orden y repeticion por ser un set




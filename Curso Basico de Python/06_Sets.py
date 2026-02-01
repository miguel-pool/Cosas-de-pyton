### Sets ###

my_set = set() # Forma de definir el set
my_other_set = {} # Otra forma de definirlo, pero inicia como Tipo "Dict"
print(type(my_set))
print(type(my_other_set)) # Inicialmente es un Diccionario "Dict"

my_other_set = {"Victor", "Ramirez", 18, 1.82} # Se reasigna el tipo cuando agregamos valores al set, pasa de Dict a Set
print(type(my_other_set))

print(len(my_other_set)) # "Cuenta los elementos del set"

#print(my_other_set[3]) # En los sets no se puede acceder a un elemento de esta manera, porque no tiene orden.

my_other_set.add("Vitico") # Agrega el valor de primero y el set esta desordenado
print(my_other_set) # UN SET NO ES UNA ESTRUCTURA ORDENADA

my_other_set.add("Vitico") # Un set no admite elementos repetidos
print(my_other_set)

#Forma de saber si el dato esta en la lista
print("Vitico" in my_other_set)
print("Viti" in my_other_set)

my_other_set.remove("Vitico") # Eliminar un dato/elemento
print(my_other_set)

my_other_set.clear() # elimina todos los elementos del set
print(my_other_set)

del my_other_set # Borra la propiedad del programa, deja de existir esta variable
#print(my_other_set) # NameError: name 'my_other_set' is not defined

# Es posible convertirlo a lista y acceder a sus funciones, asi como ponerle orden al set o lista
my_set = {"Victor", "Ramirez", 18, 1.82}
my_list = list(my_set)

my_other_set = {"Vitico", "Vitoco", "Viti"}

my_new_set = my_set.union(my_other_set) # Los junta sin un orden porque es un set
print(my_new_set)

print(my_new_set.union({"Python", "HTML"})) # Podemos agregar sin asignarlo a una variable, pero solo funciona para este print

print(my_new_set.difference(my_set)) # Descartamos momentaneamente un set y deja el otro u otros que estan definidos con variables


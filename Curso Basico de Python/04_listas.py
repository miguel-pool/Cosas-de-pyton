### Listas ###

my_list = list() #Forma 1 de hacer una lista
my_other_list = [] #Forma 2 de hacer la lista (Mas simple)

print (len(my_list))

my_list = [12, 15, 20, 40, 20, 50, 20, 35, 100] 

print(my_list)
print (len(my_list)) # Mide la longitud de los datos (Cuantos datos hay)

my_other_list = [18, 1.77, "Victor", "Ramirez"]

print(type(my_other_list)) # Imprimo la lista con corchetes y sale clase "list"

print(my_other_list[0]) # Los elementos se cuentan a partir del 0
print(my_other_list[1]) # Encontro la altura
print(my_other_list[2]) # encontro el nombre
print(my_other_list[3]) # encontro el apellido
print(my_other_list[-1]) # Imprimira el ultimo elemento
print(my_other_list.count("Victor"))# Cuenta la cantidad de "Victor" o el valor que sea que haya en lo que definimos.
#"print(my_other_list[-5])" # Es erroneo ya que -4 es el limite de elementos en este caso, lo mismo con el 4
# Esto es desempaquetado "No es recomendable hacer"
age, height, name, surname = my_other_list # Los Organiza por el orden en el que estaba en la primera variable
print(surname)
# Podemos reasignar con los corchetes y el numero en el que esta el dato "No se recomienda hacer"
surname, name, height, age = my_other_list[3], my_other_list[2], my_other_list[1], my_other_list[0]
print(surname)

#Se pueden encadenar o fusionar listas
print(my_list + my_other_list) # En el orden en el que se pongan

# Mas funciones
my_other_list.append("Viticorp") # Agrega uno mas a la lista (Siempre se integra de ultimo)
print(my_other_list)

my_other_list.insert(3, "Naranja") # inserta en la posicion en la que nosotros escojamos
print(my_other_list)

my_other_list[3] = "Verde"
print(my_other_list)

my_other_list.remove("Verde") # Elimina lo que nosotros le indiquemos
print(my_other_list)

my_list.remove(20) # Si se repite en la lista, solo remueve 1, elegimos que numero eliminar
print(my_list)

my_list.pop() # Quita el Ultimo elemento
print(my_list)
print(my_list.pop()) #Sirve para desapilar o sacar uno de los numeros, podemos elegir uno en concreto poniendo la posicion
my_pop = my_list.pop(1) # Podemos darle valor de variable
print(my_pop)

del my_list[0] # Eliminamos un elemento seleccionado por indice, no como en el .remove
print(my_list)

my_new_list = my_list.copy() # Es la copia desde este punto, osea, con todo lo que se ha removido y/o agregado

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse() # Da los valores al reves de la lista que ya teniamos
print(my_new_list)

my_new_list.sort() # Ordena de mayor a menor los valores de la lista
print(my_new_list)

print(my_new_list[1:4]) # Muestra lo que esta entre un valor y en otro

# CAMBIA SIEMPRE SEGUN EL ORDEN EN EL CODIGO, IMPORTANTE EL ORDEN Y NO REPETIR VARIABLE PORQUE PUEDE CAMBIAR
# NO PUEDE HABER VARIABLE CONSTANTE QUE NO SE PUEDA CAMBIAR
my_list = "Hola Python"
print(my_list)

Lista1 = [1,3,5,6,1,3,2,2,5,7]
Lista2 = []

#LISTA SIN REPETIDOS

for i in range (len(Lista1)):
    if Lista1[i] not in Lista2: # Por cada valor de Lista1 que no esta en Lista2, agregamos ese valor a Lista2.
        Lista2.append(Lista1[i])

Lista_orden = Lista2
Lista2.sort() # DA ORDEN NUMERICO
print(Lista_orden)

# Nueva Caracteristica (que aprendi mucho despues de esto)

"""
Podemos utilizar valores booleanos para la posicion en las listas
False = 0
True = 1
A continuacion un Ejemplo.
"""

my_list = "Hola Python"
print(my_list[False])
print(my_list[True])
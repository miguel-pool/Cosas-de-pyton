#Crear una lista con "list"

lista = list(["Sergio Perez","Reacing point",11,"Lance Stroll",28])
print("Esta es mi lista", lista)

#lista = list([23,53,11,96,28])
#print("Esta es mi lista", lista)

#"LEN" nos devuelve la cantidad de elemtentos que tiene una lista
resultado=len(lista)
print("\n")
print("Este es la cantidad de elementos que tiene mi lista:",resultado)

#Agrega elemtentos a la lista con "APPEND"
lista.append(54)
print("\n")
print(lista)

#"INSERT"Agrega valores a la lista dependiendo del indice que tu le digas
lista.insert(5,35)
print("\n")
print(lista)

#"Extend" agregamo varios elementos  a la lista  
print("\n")
lista.extend([52,70,2020])
print(lista)

#"POP" elimina un elemento de la lista con su indice
print("\n")
print(len(lista))
lista.pop(5)
print(len(lista))
print(lista)

#NOTA: SI QUIERES ELIMINAR EL ULTIMO ELEMENTO DE TU LISTA PUEDES PONER UN lista.pop(-1)
print("\n")
lista.pop(-1)
print(lista)

#"REMOVE" REMUEVE EL ELEMNTO DE LA LISTA POR SU VALOR
print("\n")
lista.remove("Lance Stroll")
print(lista)

#"CLEAR" Elimina todos los ELEMENTOS DE LA LISTA
print("\n")
lista.clear()
print(lista)

#"SORT" ORDENA TODOS LOS ELEMENTOS DE MANERA ACENDENTE 
#SOLO FUNCIONA SI LA LISTA NO TIENE CADENAS DE TEXTO
print("\n")
lista.sort()
print(lista)


#Pero si se agrega un revser se ordenan al reves   
print("\n")
lista.sort(reverse=True)
print(lista)

#Invirtiendo los datos de una lista sin ordenarla
print("\n")
lista.reverse()
print(lista)
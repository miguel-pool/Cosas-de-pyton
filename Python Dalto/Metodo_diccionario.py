#Sirve para iterar los items
#Keys
diccionario = {
    "nombre":"Miguel",
    "Apellido":"Pool",
    "susb" : 1000
}

#Nos devuelve objetos dict_item
claves = diccionario.keys()


#Get
#Te devuelve un valor que le coloques dentro del parentesis y tambien funcionan con valores numericos
#Si no encuentra un elemento que no se encuentra en el diccionario te devuelve "NONE"
claves = diccionario.get("nombre")


#Eliminando todo del diccionario
##diccionario.clear()

#Eliminando un elemento del diccionario
#pop solo sirve para eliminar un solo elemento del diccionario
diccionario.pop("susb")
print(diccionario)

#Obteniendo un elemento dict_items_iterable
#Aqui si podemos iterar el diccionario 
#Iterar = recorrer todos los elementos del diccionario
diccionario_iterable = diccionario.items()
print(diccionario_iterable)




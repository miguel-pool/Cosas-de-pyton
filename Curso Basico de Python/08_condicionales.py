### Condicionales ###

my_condition = False #Si es 'True' se ejecuta, si es 'False' no se ejecuta

if my_condition: # No se cumple la condicion porque es False, osea, no se hace el print
    print("Se ejecuta la condicion del if")

my_condition =  5*5 # Se ejecuta el print igual porque no es ni true ni false, siempre y cuando, no se iguale a otro valor en el if

if my_condition == 11: # No se imprimira porque debera ejecutarse si es igual a 11, caso que no es, porque el valor de la condicion es 10
    print("Se ejecuta la condicion del segundo if")

if my_condition == 10: # Aqui se cumple la condicion, porque la condicion es 10 y lo toma como true
    print("Se ejecuta la condicion del segundo if")

if my_condition > 10: 
    print("Es mayor a 10")
else:
    print("Es menor o igual a 10")

# If = Si
# Else = Si no
# Elif = Parecido al if "Necesita una condicion igual a if", como si fuera una comprobacion extra

if my_condition > 10 and my_condition < 20: 
    print("Es mayor a 10 y menor a 20")
elif my_condition == 25: # Es una extra condicion al if
    print("Es igual a 25")
else:
    print("Es menor o igual a 10 o mayor o igual a 20 o distinto a 25")

my_string = "" # Si no hay string, lo valora como False, si hay string o algo escrito, lo valora como true y ejecuta el if

if my_string:
    print("Mi cadena de texto no es vacia")
else:
    print("Nuestra cadena de texto es vacia")

if my_string == "Holaa": # En este caso no se cumple porque el valor del string no dice "Holaa"
    print("Estas cadenas de texto coinciden")

if not my_string: # Si la condicion es false, se cumplira esta parte
    print("Mi cadena de texto es vacia")

print("la ejecucion continua")
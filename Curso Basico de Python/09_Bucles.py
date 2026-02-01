### Bucles ###

# While

myCondition = 0

while myCondition < 10: # Es como un "If" pero infinito hasta que se deje de cumplir alguna de las condiciones
    print(myCondition)
    myCondition += 2 # Va agregando cada vuelta la cantidad que hayamos designado
else: # Es opcional
    print("Mi condicion es mayor a 10")

print("la ejecucion continua")

while myCondition < 20:
    myCondition += 1 
    if myCondition == 15:
        print("Se detiene el bucle")
        break # Para el bucle

    print(myCondition)
    
# For
# Bucle que imprime en base a cuantos elementos tiene nuestra lista o lo que sea.

myList = [20, 50, 15, 40, 30, 70]
for element in myList:
    print(element)

my_tuple = (18, 1.82, "Victor", "Ramirez", "Victor")
for element in my_tuple:
    print(element)

my_other_set = {"Victor", "Ramirez", 18, 1.82}
for element in my_other_set:
    print(element)

my_dict = {"Nombre:":"Victor", "Apellido":"Ramirez", "Edad":18, "Lenguajes":{"Python", "JavaScript", "C++"}, 1:1.82}
for element in my_dict: # Solo imprime las claves en este caso
    print(element)
    if element == "Edad":
        break


for element in my_dict.values():
    print(element)
    if element == 18:
        continue # Hace un mini breack solo a la ejecucion cuando llega al 18 en este caso. Vuelve al for sin ejecutar lo de abajo.
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado")





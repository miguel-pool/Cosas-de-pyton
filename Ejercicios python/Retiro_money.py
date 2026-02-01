Nombre= "Cesar Huerta"
Bienvenida= f" Hola {Nombre} Bienvenido a BBVA "
Saldo= "12000 euros"

Contraseña_guardada= "#11PumasUNAM"
Contraseña_escrita = ""
opcion= ""


print (Bienvenida)
print ("---------------------------------------------")

print (f"Por favor {Nombre} ingrese su contraseña")

print ("-------------------------------------------")

Contraseña_escrita = input (" Ingrese su contraseña ")
if Contraseña_escrita == Contraseña_guardada:
    print (" Acceso concedido... ")
    print("----------------------------------------------")
    print (f"¿Que necesita saber {Nombre}? ")
    print ("1"".-Saldo")
    print ("2"".- Retirar efectivo")
    print ("3"".- Salir")
    opcion = input (" Seleccione una opcion del menu por favor ")
    if opcion == "1":
        print("----------------------------------------------")
        print (" Su saldo es de ", Saldo)
        print("----------------------------------------------")
    if opcion == "2":
        print("----------------------------------------------")
        print (" ¿Desea retirar todo el saldo de su cuenta? ")
        print (" SI ")
        print (" NO ")
        print("----------------------------------------------")
        opcion = input (" Seleccione una de las 2 opciones ")
        if opcion== "SI":
            print("----------------------------------------------")
            print (" Espere un momento... ")
            print("----------------------------------------------")
            print(" Gracias por usar BBVA ")
        else:
            print("----------------------------------------------")
            print (f" De acuerdo {Nombre} que tenga un buen dia :) ")
            print("----------------------------------------------")
    if opcion== "3":
        print (" Gracias por usar BBVA que tenga buen dia :) ")
else:
    print ("Acceso denegado...")           



 

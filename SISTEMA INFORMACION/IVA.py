def Iva(producto):
    return producto * 0.16    
    
active = True
while active:
    
    opcion = int (input("""
Ingresa una opcion:                    
1.-Calcular iva
2.- Salir del menu 
"""))
    
    if opcion == 1:
        print("Ingresa el valor del producto: ")
        producto = float (input("> "))    
        resultado = Iva(producto)
        print("El valor agregado es: ",resultado)
    
    if opcion == 2:
        print("Gracias por usar nuestro programa")
        active = False
    
        
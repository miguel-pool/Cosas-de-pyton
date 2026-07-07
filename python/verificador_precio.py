#Calculadora de descuento
def verificador(precio, descuento):
    return  precio - (precio * descuento / 100)
    

Activo = True

while Activo:
    print("===================================")
    print("Calculadora de precios")
    print("1.-Calcular descuento")
    print("2.-Salir")
    op = input("Ingrese una opcion: ")
    print("===================================")
    
    if op == "1":
        precio = float(input("Ingrese el valor del producto: "))
        descuento = float(input("De cuanto es el descuento: "))
        precio_final = verificador(precio,descuento)
        print("El valor final del producto es ", precio_final)
        
    if op == "2":
        print("Gracias por usar el programa")
        Activo == False
        break
        
        
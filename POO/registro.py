base_datos = {
    
    "manzana": 10.23,
    "pera": 12.22, #Agregamos los datos
    "Uva": 10.32,
    "naranjas": 20.32
}
activo = True
total = 0

while activo:
    
    print("----------------------------------")
    print("|       Marca MK entretaiment    |")      
    print("|        ¿Qué desea hacer?       |")
    print("|      (Seleccione una Opcion)   |")
    print("----------------------------------")

    print("==================================")
    print("1.-Registrar producto")
    print("2.-Valor total del inventario")
    print("3.-Comparador")
    print("4.-Salir")
    op = input("Seleccione una opcion: ")
    print("==================================")
    
    
    #Registro de articulos
    if op == "1":
        print("Ingrese el nombre del producto")
        producto = input("Ingrese el producto: ")
        valor = float(input("Ingrese el valor: "))
        base_datos[producto] = valor
        
        while True:
            
            print("¿Desea agregar otro producto? (s/n)")
            respuesta = input("Ingrese su respuesta: ")
            
            if respuesta.lower() == "s":
                print("Ingrese el nombre del producto")
                producto = input("Ingrese el producto: ")
                valor = float(input("Ingrese el valor: "))
                base_datos[producto] = valor
                
            elif respuesta.lower() == "n":
                break
            
            else:
                print("Opcion no valida, por favor ingrese 's' o 'n'")
        
        print(base_datos)
    
    
     #Calculos de valor total del almacen
    if op == "2":
        for i in base_datos:
            total = total + base_datos[i]
            print("El valor total de almacen es de ", total)
    
    #Conocer el articulo mas caro
    if op == "3":
        for i in base_datos:
            for j in base_datos:
                if base_datos[i] < base_datos[j]:
                    base_datos[i] = base_datos[j]
        print("Este es el articulo mas costoso del almacen", base_datos[i])

    #Salir del programa
    if op == "4":
        print("Gracias por usar el programa :D")
        break
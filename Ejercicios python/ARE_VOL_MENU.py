op = ""
while op != "3":
    print (" 1.- Area \n 2.- Volumen \n 3.- Salir")
    op = int (input (" Seleccione algunas de las opciones "))

        #Menu de areas
        
    if op == 1:
        print (" 1.1- Circulo \n 1.2.- Cuadrado \n 1.3.- Regresar ")
        op = input (" Seleccione algunas de las opciones ")
        #Area del circulo
        if op == "1.1":
            print (" Ingrese el radio del circulo ")
            Radio = float (input (" Radio: "))
            Area = Radio * 3.1416
            Area = round (Area , 2 )
            print ("El area del circulo es", Area )
        #Area del cuadrado
        if op == "1.2":
            print (" Inserte el lado del cuadrado ")
            Lado = int (input (" Lado: "))
            Area = round (Area, 2)
            Area = Lado * Lado 
            print ("El area del cuadrado es ", Area )
        #Opcion regresar 
        if op == "1.3":
            print (" 1.- Area \n 2.- Volumen \n 3.- Salir")
            op = int (input (" Seleccione algunas de las opciones "))
    
    #Menu de volumenes 
    if op == 2:
        print (" 1.1- Esfera \n 1.2- Cubo \n 1.3.- Regresar ")
        op = input (" Selccione algunas de las opciones ")
        
        #Volumen de la esfera
        if op == "1.1":
            print (" Inserte el radio de la esfera ")
            Radio = float (input (" Radio: "))
            Volumen = 4/3 * (3.14 * 3 * Radio )
            Volumen = round (Volumen , 2 )
            print (" El volumen de la esfera es  ", Volumen )
            
            #Volumen del cubo
        if op == "1.2":
            print (" Inserte el lado del cubo ")
            Lado = int (input (" Lado: "))
            Volumen = round (Volumen, 2 )
            Volumen = (Lado * Lado * Lado )
            print (" El volumen del cubo es ", Volumen )
            
            #Op es igual 1.3
        if op == "1.3":
            print (" 1.- Area \n 2.- Volumen \n 3.- Salir")
            op = int (input (" Seleccione algunas de las opciones "))
            
    if op == 3:
        print (" Vuelva pronto :) ")
    break

             
        
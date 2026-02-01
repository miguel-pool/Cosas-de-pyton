op= ""
carne = ""
FyV= ""
Continuar = ""
Acumulador = 0

#Menu general
while op != 5:
    print ("------------------------------------")
    print (" ¿Que desea comprar? ")
    print (" 1.-Carnes ")
    print (" 2.-Frutas ")
    print ("------------------------------------")
    print (" 3.-Quitar productos ")
    print (" 4.-Listo ")
    print (" 5.-.-Salir ")
    op = input (" Eliga alguna de las 5 opciones ")
 
#Menu de las carnes 
if op == "1":
    ("---------------------------------")
    print (" SELECCIONE EL TIPO DE CARNE ")
    print (" 1.- Pollo ")
    print (" 2.- Cerdo ")
    print (" 3.-Pavo ")
    print (" 4.- Cordero ")
    print (" 5.- Vaca ")
    carne = input ("¿Que tipo de carne llevara? ")
        
    #Op == 1 osea Pollo
    if carne == "1":
        print ("---------------------------------")
        kilos = float (input ( "Ingresa el peso en kilos: "))
        Pollo = 40.70 * kilos
        Acumulador = Acumulador + Pollo
        Continuar = input (" ¿Seria todo? \n (1) SI o (2) NO ")
            
        #Si no quiere continuar
        if Continuar == "1" :
            print ("------------------------------------")
            print (" ¿Que desea comprar? ")
            print (" 1.-Carnes ")
            print (" 2.-Frutas ")
            print ("------------------------------------")
            print (" 3.-Quitar productos ")
            print (" 4.-Listo ")
            print (" 5.-.-Salir ")
            op = input (" Eliga alguna de las 5 opciones ")
            
            #Si decide continuar     
        else:
            print ("---------------------------------")
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Pollo = 40.70 * kilos
            Acumulador = Acumulador + Pollo
            Continuar = input (" ¿Seria todo? \n(1) SI (2) NO ")
            
        #OP == 2 osea Cerdo        
        if carne == "2" :
            print ("---------------------------------")      
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Cerdo = 60.90 * kilos
            Acumulador = Acumulador + Cerdo
            Continuar = input (" ¿Seria todo? \n (1) SI O (2) NO ")
            #Si seria todo 
            if Continuar == "1" :
                print ("------------------------------------")
                print (" ¿Que desea comprar? ")
                print (" 1.-Carnes ")
                print (" 2.-Frutas ")
                print ("------------------------------------")
                print (" 3.-Quitar productos ")
                print (" 4.-Listo ")
                print (" 5.-.-Salir ")
                op = input (" Eliga alguna de las 5 opciones ")
            
            #Si se le olvido algo mas  
            else:
                print ("---------------------------------")
                kilos = float (input ( "Ingresa el peso en kilos: "))
                Acumulador = Acumulador + Cerdo
                Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
        
        #OP== 3 osea Pavo    
        if carne == 3 :
            print ("---------------------------------")      
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Pavo = 100 * kilos
            Acumulador = Acumulador + Pavo
            Continuar = input (" ¿Seria todo? \n SI O NO ")
            
            #Si seria todo 
            if Continuar == "SI":
                print ("------------------------------------")
                print (" ¿Que desea comprar? ")
                print (" 1.-Carnes ")
                print (" 2.-Frutas ")
                print ("------------------------------------")
                print (" 3.-Quitar productos ")
                print (" 4.-Listo ")
                print (" 5.-.-Salir ")
                op = input (" Eliga alguna de las 5 opciones ")
            #Si olvido agregar algo
            else:
                print ("---------------------------------")
                kilos = float (input ( "Ingresa el peso en kilos: "))
                Acumulador = Acumulador + Pavo
                Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
        
        #OP== 4 osea Cordero     
        if carne == "4":
            print ("---------------------------------")      
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Cordero = 250 * kilos
            Acumulador = Acumulador + Cordero
            Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
            
            #Si seria todo 
            if Continuar == "1":
                print ("------------------------------------")
                print (" ¿Que desea comprar? ")
                print (" 1.-Carnes ")
                print (" 2.-Frutas ")
                print ("------------------------------------")
                print (" 3.-Quitar productos ")
                print (" 4.-Listo ")
                print (" 5.-.-Salir ")
                op = input (" Eliga alguna de las 5 opciones ")
            #Si se le olvido algo 
            else:
                print ("---------------------------------")
                kilos = float (input ( "Ingresa el peso en kilos: "))
                Acumulador= Acumulador + Cordero
                Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
                
            
        #Si OP== 5 osea Vaca    
        if carne == "5":
            print ("---------------------------------")      
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Vaca = 90.90 * kilos
            Acumulador = Acumulador + Vaca
            Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
        #Si seria todo 
            if Continuar == "1":
                print ("------------------------------------")
                print (" ¿Que desea comprar? ")
                print (" 1.-Carnes ")
                print (" 2.-Frutas ")
                print ("------------------------------------")
                print (" 3.-Quitar productos ")
                print (" 4.-Listo ")
                print (" 5.-.-Salir ")
                op = input (" Eliga alguna de las 5 opciones ")
            else:
                print ("---------------------------------")
                kilos = float (input ( "Ingresa el peso en kilos: "))
                Acumulador = Acumulador + Vaca
                Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
                
    #Menu de Frutas y verduras 
    if op == "2":
        print (" SELECCIONE LAS FRUTAS Y VERDURAS QUE NECESITA ")
        print ("---------------------------------")
        print (" 1.- Manzana ")
        print (" 2.- Platanos ")
        print (" 3.- Uvas ")
        print (" 4.- Naranjas ")
        print (" 5.- Zanahoria ")
        print (" 6.- Papas ")
        print (" 7.- Calabaza ")
        print (" 8.- Lechuga ")
        print ("---------------------------------")
        FyV = input (" ¿Que verdura y fruta llevara? ")
        
        #Si es coge manzana
        Manzana = 35.80
        if FyV == "1":
           print ("---------------------------------")      
           kilos = float (input ( "Ingresa el peso en kilos: "))
           Manzana = 35.80 * kilos
           Acumulador = Acumulador + Manzana 
           Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
           #Si escoge que si
           
        if Continuar == "1":
            print ("------------------------------------")
            print (" ¿Que desea comprar? ")
            print (" 1.-Carnes ")
            print (" 2.-Frutas ")
            print ("------------------------------------")
            print (" 3.-Quitar productos ")
            print (" 4.-Listo ")
            print (" 5.-.-Salir ")
            op = input (" Eliga alguna de las 5 opciones ")
                
            #Si escoge NO
        else:
            print ("---------------------------------")
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Acumulador = Acumulador + Manzana
            Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
                
        #Platano
        if FyV == "2":
            Platanos = 18.20
            print ("---------------------------------")      
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Acumulador = Acumulador + Platanos
            Platanos = 18.20 * kilos
            Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
        #Si escoge que SI
        if Continuar == "1":
            print ("------------------------------------")
            print (" ¿Que desea comprar? ")
            print (" 1.-Carnes ")
            print (" 2.-Frutas ")
            print ("------------------------------------")
            print (" 3.-Quitar productos ")
            print (" 4.-Listo ")
            print (" 5.-.-Salir ")
            op = input (" Eliga alguna de las 5 opciones ")
            
        #Si escoge NO  
        else:
            print ("---------------------------------")
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Acumulador = Acumulador + Platanos
            Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
        
        #UVAS    
        if FyV == "3": 
            print ("---------------------------------")      
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Uvas = 60 * kilos
            Acumulador = Acumulador + Uvas
            Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
        
        #Si escoge que SI
        if Continuar == "1":
            print ("------------------------------------")
            print (" ¿Que desea comprar? ")
            print (" 1.-Carnes ")
            print (" 2.-Frutas ")
            print ("------------------------------------")
            print (" 3.-Quitar productos ")
            print (" 4.-Listo ")
            print (" 5.-.-Salir ")
            op = input (" Eliga alguna de las 5 opciones ")
        
        #Si escoge que NO
        else:
            print ("---------------------------------")
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Acumulador = Acumulador + Platanos
            Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
        
        
        if FyV == "4":
            print ("---------------------------------")      
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Naranjas = 25.20 * kilos
            Acumulador = Acumulador + Naranjas
            Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
        
        #Si dice que SI
        if Continuar == "1":
            print ("------------------------------------")
            print (" ¿Que desea comprar? ")
            print (" 1.-Carnes ")
            print (" 2.-Frutas ")
            print ("------------------------------------")
            print (" 3.-Quitar productos ")
            print (" 4.-Listo ")
            print (" 5.-.-Salir ")
            op = input (" Eliga alguna de las 5 opciones ")
            
        #Si dice que no
        else:
            print ("---------------------------------")
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Acumulador = Acumulador + Naranjas
            Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
        
        #ZANAHORIAS
        if FyV == "5":
            Zanahoria = 15.60
            print ("---------------------------------")      
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Zanahoria = 15.60 * kilos
            Acumulador = Acumulador + Zanahoria
            Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
            
            #Si dice que SI
        if Continuar == "1":
            print ("------------------------------------")
            print (" ¿Que desea comprar? ")
            print (" 1.-Carnes ")
            print (" 2.-Frutas ")
            print ("------------------------------------")
            print (" 3.-Quitar productos ")
            print (" 4.-Listo ")
            print (" 5.-.-Salir ")
            op = input (" Eliga alguna de las 5 opciones ")
            
            #Si dice que NO
        else:
            print ("---------------------------------")
            kilos = float (input ( "Ingresa el peso en kilos: "))
            Acumulador = Acumulador + Zanahoria
            Continuar = input (" ¿Seria todo? \n(1)SI (2)NO ")
                   
    if op == " 3 ":
        print ("¿Qué producto desea remover de la lista? ")
        #Para quitar productos
        print ("---------------------------------")
        print (" Estos son los prodcutos de tu carrito ")
        
    if op == " 4 ":
        print ("---------------------------------")
        Acumulador = round (Acumulador, 2)
        print (" El total de su compra es de ", Acumulador ," Pesos Mexicanos ")
        print ("---------------------------------")
     
        print (" ¿Cual seria su metodo de pago? ")
        print ("1.-Tarjeta \n" "2.- Efectivo "  )
        Metodo_Pago= input (" Selccione su metodo de pago \n 1-TARJETA 2-EFECTIVO: ")
     
        if Metodo_Pago == "1":
            print (" Inserte los 16 digitos de su tarjeta por favor ")
            tarjeta = int (input (" Digitos: "))
         
            print (" Inserte su CVV de 3 digitos ")
            Cvv= int (input (" CVV: "))
         
            Pago= tarjeta + Cvv
            if Pago == 19:
                print (" Su pago fue procesado... Que tenga buen dia :) ")
             
        if Metodo_Pago == "2":
         print (" Inserte el dinero en la caja ")
         print (" Pago completado... Que tenga buen día :) ")
         
    if op == "5":
        print (" ¡VUELA PRONTO! :) ")

            
     
     
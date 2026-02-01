
import math

print (" Bienvenido a calculadora ")
print (" ¿Qué deseas hacer? ")

print (" 1.-Suma \n 2.-Resta \n 3.-Multiplicación \n 4.-División \n 5.-Raiz ")
Opcion = input (" Selecciona una opcion: ")

while True:
    #Suma
    if Opcion == "1":
        print (" Inserte su primer valor ")
        
        #Error de valor
        try:
            Valor_1 = int (input ( " Valor: "))
            print (" Inserte el segundo valor ")
            Valor_2 = int (input ( " Valor: "))
            
        except ValueError:
            print ("Valor no valido ")
            continue 
        
        Resultado = Valor_1 + Valor_2
        print (" El respuesta es ", Resultado)
        
    #Desicion de continuar o no
        print ( " ¿Seria todo? \n SI(1) NO(2) ")
        Continuar = input (" Desicion: ")
        
        if Continuar == "2":
            print (" 1.-Suma \n 2.-Resta \n 3.-Multiplicación \n 4.-División \n 5.-Raiz ")
            Opcion = input (" Selecciona una opcion: ")
        
        if Continuar == "1":
            print (" Esperemos haberle ayudado B) ")
            break

    #Resta 
    if Opcion == "2":
        print (" Inserte su primer valor ")
        #Error de valor
        try:
            Valor_1 = int (input ( " Valor: "))
            print (" Inserte el segundo valor ")
            Valor_2 = int (input ( " Valor: "))
            
        except ValueError:
            print ("Valor no valido ")
            continue 
        
        Resultado = Valor_1 - Valor_2
        print (" El respuesta es ", Resultado)
        
    #Desicion de continuar o no
        print ( " ¿Seria todo? \n SI(1) NO(2) ")
        Continuar = input (" Desicion: ")
        
        if Continuar == "2":
            print (" 1.-Suma \n 2.-Resta \n 3.-Multiplicación \n 4.-División \n 5.-Raiz ")
            Opcion = input (" Selecciona una opcion: ")
        
        if Continuar == "1":
            print (" Esperemos haberle ayudado B) ")
            break
    
    #Multiplicacion
    if Opcion == "3":
        print (" Inserte su primer valor ")
        #Error de valor
        try:
            Valor_1 = int (input ( " Valor: "))
            print (" Inserte el segundo valor ")
            Valor_2 = int (input ( " Valor: "))
       
        except ValueError:
            print ("Valor no valido ")
            continue 
        
        Resultado = Valor_1 * Valor_2
        print (" El respuesta es ", Resultado)
        
    #Desicion de continuar o no
        print ( " ¿Seria todo? \n SI(1) NO(2) ")
        Continuar = input (" Desicion: ")
        
        if Continuar == "2":
            print (" 1.-Suma \n 2.-Resta \n 3.-Multiplicación \n 4.-División \n 5.-Raiz ")
            Opcion = input (" Selecciona una opcion: ")
        
        if Continuar == "1":
            print (" Esperemos haberle ayudado B) ")
            break
        
    #División
    if Opcion == "4":
        print (" Inserte su primer valor ")
        try:
            Valor_1 = int (input ( " Valor: "))
            print (" Inserte el segundo valor ")
            Valor_2 = int (input ( " Valor: "))
        except ValueError:
            print ("Valor no valido ")
            continue 

        Resultado = Valor_1 / Valor_2
        if Valor_2 == 0:
            print (" Error Matematico ")
        else:
            Resultado = round (Resultado,2)
            print (" El respuesta es ", Resultado)
        
    #Desicion de continuar o no
        print ( " ¿Seria todo? \n SI(1) NO(2) ")
        Continuar = input (" Desicion: ")
        
        if Continuar == "2":
            print (" 1.-Suma \n 2.-Resta \n 3.-Multiplicación \n 4.-División \n 5.-Raiz ")
            Opcion = input (" Selecciona una opcion: ")
        
        if Continuar == "1":
            print (" Esperemos haberle ayudado B) ")
            break
        
    #Raiz cuadrada 
    if Opcion =="5":
        try:
            print (" Inserte el valor ")
            Valor_1 = int (input ( " Valor: "))

        except ValueError:
            print ("Valor no valido ")
            continue 
        
        Resultado = math.sqrt(Valor_1)
        Resultado = round (Resultado,2)
        print (" La raiz de ese numero es ", Resultado)
        
    #Desicion de continuar o no
        print ( " ¿Seria todo? \n SI(1) NO(2) ")
        Continuar = input (" Desicion: ")
        
        if Continuar == "2":
            print (" 1.-Suma \n 2.-Resta \n 3.-Multiplicación \n 4.-División \n 5.-Raiz ")
            Opcion = input (" Selecciona una opcion: ")
        
        if Continuar == "1":
            print (" Esperemos haberle ayudado B) ")
            break

    
    
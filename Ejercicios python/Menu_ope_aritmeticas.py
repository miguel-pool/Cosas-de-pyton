import math

total=0
print("Bienvenido al menu de las operaciones artimeticas")
print("1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\n5.-Modulo")
print("Seleccione alguna de las opciones")
op=int(input("Opcion:"))

match op:
    case 1:
        #SUMA
        print("Usted escogio suma")
        print("Inserte los numeros que desea sumar")
        n1=float(input("Numero 1:"))
        n2=float(input("Numero 2:"))
        total=n1+n2
        print("El resultado de la suma es:",total)
    
    case 2:
        #RESTA
        print("Usted escogio resta")
        print("Inserte los numeros que desea sumar")
        n1=float(input("Numero 1:"))
        n2=float(input("Numero 2:"))
        total=n1-n2
        print("El resultado de la resta es:",total)
    case 3:
        #MULTIPLICACION
        print("Usted escogio multiplicacion")
        print("Inserte los numeros que desea sumar")
        n1=float(input("Numero 1:"))
        n2=float(input("Numero 2:"))
        total=n1*n2
        print("El resultado de la multiplicacion es:",total)
    case 4:
        #DIVISION
        print("Usted escogio division")
        print("Inserte los numeros que desea sumar")
        n1=float(input("Numero 1:"))
        n2=float(input("Numero 2:"))
        
        if n2==0:
            print("No puedes dividir entre 0")
        
        total=n1/n2  
        print("El resultado de la division es:",total)
    case 5:
        #MODULO
        print("Usted escogio modulo")
        print("Inserte los valores que desea saber los modulos")
        n1=float(input("Numero 1:"))
        n2=float(input("Numero 2:"))
        
        if n2==0:
            print("No puedes dividir entre 0")
        else:
            total=n1%n2
            
        print("El modulo de esta operacion es:",total)
    
    
    case 8:
        print("Descubriste algo secreto :O")
        print("Aqui solo puedes sacar raiz cuadrada")
        print("Inserta el valor al cual le deseas obtener la raiz")
        n1=float(input("Numero:"))
        
        if n1<0:
            print("No puedes sacar raiz a un numero negativo")
        
        else:
            total=math.sqrt(n1)
            print("Este es la raiz de este numero",total)
        
#Conviertir un dato "str" a un entero "int"
edad = int (input (" Inserte un numero del 1 al 100 "))

if edad <= -1 :
    print (" Numero no valido ")

if edad > 101:
    print ("Numero no valido ")
    
if edad <= 2 and edad >=0:
    print (" Es un bebe ")

if edad >= 2 and edad <= 10:
    print (" Es un niño ")
    
if edad >= 10 and edad <= 14:
    print (" Es un puberto ")

if edad >= 15 and edad <= 17:
    print (" Es un adolecente ")

if edad >= 18 and edad <= 29:
    print (" Eres un adulto joven ")

if edad >= 30 and edad <= 59:
    print (" Eres un adulto mayor ")

if edad >= 60 and edad <= 100:
    print (" Eres un anciano ")



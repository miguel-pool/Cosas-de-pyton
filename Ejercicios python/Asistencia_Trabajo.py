
print ("-----------------------------------------------------------")
print (" Inserte los dias que no asistio el trabajador durante 15 días ")
Faltas = int (input (" Faltas: "))
print ("-----------------------------------------------------------")

print ("-----------------------------------------------------------")
print (" Inserte si el trabajador tuvo algun retardo ")
Retardos = int (input (" Retardos: "))
print ("-----------------------------------------------------------")
if Retardos == 2:
    Faltas = Faltas + 1
if Retardos == 4:
    Faltas = Faltas +2 
if Retardos == 6:
    Faltas = Faltas +3  

print ("-----------------------------------------------------------")
print (" Inserte si el trabajador tiene justifiaciones de su faltas ")
Justifiaciones = int (input (" Justificantes: "))
print ("-----------------------------------------------------------")

Total = Faltas - Justifiaciones


if Total == 0:
    print ("-----------------------------------------------------------")
    print (" El trabajador nunca ha faltado ")
    print (" Entreguenle 250 pesos esto por su entrega ")
    print ("-----------------------------------------------------------")

if Total <= 3 or Total == 4 :
    print ("-----------------------------------------------------------")
    print (" El trabajador a faltado unos cuantos días ")
    print (" Restele 50 pesos de su quincena ")
    print ("-----------------------------------------------------------")

if Total <= 5 or Total <= 7 :
    print ("-----------------------------------------------------------")
    print (" El trabajador ha faltado algunos días ")
    print (" Restele 100 pesos de su quincena ")
    print ("-----------------------------------------------------------")

if Total == 8:
    print ("-----------------------------------------------------------")
    print (" El trabajador ha faltado mucho al trabajo ")
    print (" Restele 250 pesos de su quincena ")
    print ("-----------------------------------------------------------")

if Total <= 9 or Total == 10:
    print ("-----------------------------------------------------------")
    print (" El trabajador ha faltado bastante ")
    print (" Restele 450 pesos de su quincena ")
    print ("-----------------------------------------------------------")

if Total == 15:
    print ("-----------------------------------------------------------")
    print (" El trabajador ha faltado los 15 dias ")
    print (" El trabajor se le dara baja del sistema temporalmente ")
    print ("-----------------------------------------------------------")
    


    
    
    
    
    


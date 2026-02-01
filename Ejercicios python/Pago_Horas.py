sueldo_por_hora= 51
Pregunta = ""

print (" Por favor inserte las horas que trabajo durante la semana ")
horas= int (input (" Horas: "))

print (" ¿Durante la semana hizo horas extras? ")
Pregunta = input (" ¿Hizo horas extras? ")

if Pregunta == ("Si"):
    horas_extras = int (input (" ¿Cuantas horas extras hizo? "))
    
    horas = horas + horas_extras
else:
    print (" Esta bien gracias ")
    

if horas <=23:
    sueldo = sueldo_por_hora * horas 
    
    print ("Tu sueldo correspondiente es de ", sueldo ," Pesos mexicanos")
     

if horas >= 24:
    sueldo = sueldo_por_hora * horas 
    print ("Este es tu sueldo correspondiente es " , sueldo, "Esto es sin el bono" )
    Sueldo_TOT = sueldo * 0.15
    Sueldo_TOT = Sueldo_TOT + sueldo
    
    print ("Tu sueldo correspondiente es de ", Sueldo_TOT, " esto es con el bono ")
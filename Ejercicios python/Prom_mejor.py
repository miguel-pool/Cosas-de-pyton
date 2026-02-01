Bandera = 0
Total = 0
print (" Inserte su nombre completo ")
Nombre= input (" Nombre: ")

print (f" Bienvenido docente {Nombre}")

while Bandera != 6:
    print (" Inserte las calificaciones del estudiante: ")
    Notas_de_alumno = float (input (" Calificaciones: " )) 
    Bandera += 1
    Total = Notas_de_alumno + Notas_de_alumno

Promedio = Notas_de_alumno/Bandera

if Promedio == 6.5 or Promedio <= 7:
    print (Promedio)
    print (f"Felicidades {Nombre} pasaste el semestre con la minima ")


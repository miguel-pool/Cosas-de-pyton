calificaciones = []
total = 0

for vuelta in range(5):
    
    try:
        print("Ingrese las calificaciones: ")
        calificacion = int(input("Notas: "))
        calificaciones.append(calificacion)
        if calificacion < 0 or calificacion > 10:
            raise ValueError("La calificación debe estar entre 0 y 10")
       
    
    except ValueError as error:
        print("Error: ", error)
        continue
        
    
    total = total + calificacion
    
promedio = total / 5
print("El promedio es igual a ", promedio)
    
    
    


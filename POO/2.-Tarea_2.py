# Sistema básico de alumnos

# Lista para guardar nombres
alumnos = [] #Se crea una lista vacia, para guardar a los alumno (nombres)

# Lista para guardar calificaciones
calificaciones = [] #Se crea una lista vacia, para guardar las calificaciones (calificaciones)

print("=== REGISTRO DE ALUMNOS ===")#Mensaje de bienvenida al usuario


# Ciclo para pedir 3 alumnos
for i in range(3): #Se crea un ciclo for para guardar solamente 3 alumnos

    nombre = input("Ingresa el nombre del alumno: ") #Solicitamos al usuario el nombre del alumno y lo guardamos como string
    alumnos.append(nombre) #Lo guardamos en la lista de alumnos

    calificacion = float(input("Ingresa la calificación: ")) #Solicitmos la calificacion del alumno,  y lo guardamos como flotante
    calificaciones.append(calificacion) #Se guarda la calificacion en la lista ya creada

print("\n=== RESULTADOS ===") #Mensaje de presentacion de los resultados

# Variable para promedio
suma = 0

# Recorrer listas
for i in range(3): #Ciclo for para recorrer la lista, de los 3 alumnos

    print("\nAlumno:", alumnos[i]) #imprimimos el nombre del alumno, de la lista de alumnos
    print("Calificación:", calificaciones[i]) #imprimimos la calificacion del alumno de la lista de calificaciones

    # Condicional
    
    #Aplicamos logica al codigo
    if calificaciones[i] >= 6: #Si la calificacion es mayor o igual a 6
        print("Estado: Aprobado") #El alumno esta aprobado
        
    else: #En caso contrario
        print("Estado: Reprobado") #El alumno esta reprobado

    suma += calificaciones[i] #Durante este proceso, se suman las 3 calificaciones de los 3 alumnos

# Calcular promedio
promedio = suma / len(calificaciones) #De la suma de las 3 notas, se divide entre la cantidad de alumnos, que en este caso es 3

print("\nPromedio general:", promedio) #Se imprime el promedio general del grupo

# Comparación final

if promedio >= 6: #Se pone una condicion, si el promedio del grupo es mayor o igual a 6 
    print("El grupo aprobó") #Se imprime el mensaje de que el grupo aprobo
    
    
else: #En caso contrario que no se cumpla la condicion
    print("El grupo reprobó") #Se imprime el siguiente mensaje de que el grupo no aprobo
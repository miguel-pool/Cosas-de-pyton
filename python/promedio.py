def calculador(lista_calificaciones, total_alumnos):
    suma_total = 0
    
    for calificacion_actual in lista_calificaciones:
        suma_total+= calificacion_actual
    promedio = suma_total / total_alumnos
    
    return promedio

calificaciones = []

print("Cantidad de alumnos")
cantidad = int(input("> "))

for alumno in range (cantidad):
    print("Ingresa las calificaciones: ")
    nota = float(input("> "))
    calificaciones.append(nota)

resultado_final = calculador(calificaciones, cantidad)

print("===============================")
print(f"Lista de calificaciones: {calificaciones}")
print(f"El promedio del grupo es: {resultado_final}")
print("===============================")
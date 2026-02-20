print("Bienvenido al programa de fisica (por ahora solo m/s)")

print("Que deseas hacer?")
print("1.-Velocidad")
print("2.-Distancia")
print("3.-Tiempo")
opcion = int(input("Selcciona una opcion"))

distancia =int(input("Inserta distancia: "))
tiempo =int(input("Inserta el tiempo: "))
velocidad = distancia / tiempo
print("Esta es la velocidad", velocidad)


velocidad =int(input("Inserta distancia: "))
tiempo =int(input("Inserta el tiempo: "))
distancia = velocidad * tiempo
print("Este es la distancia", distancia)


distancia =int(input("Inserta distancia: "))
velocidad =int(input("Inserta el velocidad: "))
tiempo = distancia / velocidad
print("El tiempo es", tiempo)
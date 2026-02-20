tiempo_vuelta = [] #Cree la lista para guardar
tiempo_pista = 0
vueltas = 0
print("--Bienvenido al programa de telemetria--")
#Pedimos el tiempo al usuario


while True:    #El programa se ejecutara para siempre hasta que
    tiempo_realizado = float(input("Ingrese el tiempo de vuelta del piloto (Escriba 0 o negativo si desea salir): "))
    
    if tiempo_realizado <= 0: #Hasta que el tiempo sea 0 o se ingrese un -
        print("Finalizacion de la telemetria")
        break
    
    tiempo_vuelta.append(tiempo_realizado) #Guardamos el tiempo ingresado a nuestra lista
    
    
print("Los datos se guardaron exitosamente")
print("Este es la lista de timepos: ", tiempo_vuelta) #Imprimimos la lista ya creada

for tiempo_realizado in tiempo_vuelta:
    
    tiempo_pista = tiempo_pista + tiempo_realizado #Sumamos los segundos para poder obtener el total
    vueltas = vueltas + 1 #Usamos un contador(bandera) para sacar el promedio de vuelta
    promedio_vuelta = tiempo_pista / vueltas #Se saca el promedio de vuelta
     
print("Este es el tiempo total:",tiempo_pista) #Imprimimos el tiempo total de pista
print("Este es el promedio de las vueltas:",promedio_vuelta) #Imprimimos el promedio de vuelta
   
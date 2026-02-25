tiempos_vuelta = [] #Cree la lista para guardar
print("--Bienvenido al programa de telemetria--")
#Pedimos el tiempo al usuario


while True:    #El programa se ejecutara para siempre hasta que
    tiempo_realizado = float(input("Ingrese el tiempo de vuelta del piloto (Escriba 0 o negativo si desea salir): "))
    
    if tiempo_realizado <= 0: #Hasta que el tiempo sea 0 o se ingrese un -
        print("Finalizacion de la telemetria")
        break
    
    tiempos_vuelta.append(tiempo_realizado) #Guardamos el tiempo ingresado a nuestra lista
    
if len(tiempos_vuelta) == 0:
    print("No se registro ningun tiempo")
    
else:
    tiempo_pista = 0
    vueltas = 0
    vuelta_rapida = tiempos_vuelta[0] 
    vuelta_lenta = tiempos_vuelta[0]

    for tiempo_actual in tiempos_vuelta:
        
        tiempo_pista += tiempo_actual #Sumamos los segundos para poder obtener el total
        vueltas += 1 #Usamos un contador(bandera) para sacar el promedio de vuelta
    
        if tiempo_actual < vuelta_rapida:
            vuelta_rapida = tiempo_actual
            
        if tiempo_actual > vuelta_lenta:
            vuelta_lenta = tiempo_actual
        
    promedio_vuelta = tiempo_pista / vueltas #Se saca el promedio de vuelta
    print("\n")
    print("-------------------------------")
    print(f"Se completaron {vueltas} vueltas")
    print(f"Este es el tiempo total: {tiempo_pista} en segundos") #Imprimimos el tiempo total de pista
    print(f"Este es el promedio de las vueltas: {promedio_vuelta}") #Imprimimos el promedio de vuelta
    print(f"Este es la vuelta mas rapida: {vuelta_rapida}")
    print(f"Este es la vuelta mas lenta: {vuelta_lenta}")
    print("-------------------------------")

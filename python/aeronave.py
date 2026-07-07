while True:
    
    print("--- SISTEMA DE AVIACIÓN ---")
    print("--- INGRESE LOS DATOS ---")
    
    altitud = input("Ingrese la altitud: (Escribe MAYDAY para cancelar)\n")
    
    if altitud.upper() == "MAYDAY":
        print("🚨 MAYDAY RECIBIDO: Desconectando piloto automático y cediendo control manual...")
        break
    velocidad = input("Ingrese la velocidad: \n")
    
    if not altitud and not velocidad:
        print("Lectura de sensores en blanco. Recalibrando...")
        continue
    
    altitud_flo = float(altitud)
    velocidad_flo = float(velocidad)
        
    if altitud_flo <= 500 and velocidad_flo <= 250 or (altitud_flo < 100):
        print("💥IMPACTO INMINENTE / STALL DETECTADO")
            
        for protocolo in "123":
            if protocolo == "1":
                print("1.- Despresurizando cabina...")
            elif protocolo == "2":
                print("2.- Abriendo escotillas...")
            elif protocolo == "3":
                print("3.- Inyectando cohetes de eyección...")
        break
    
    elif altitud_flo >= 12000 or velocidad_flo >= 1000:
        print("⚠️ ALERTA ESTRUCTURAL: Límite de altitud o velocidad excedido. Reduciendo aceleración")
            
    elif (altitud_flo >= 8000 and altitud_flo <= 11000) and (velocidad_flo >= 800 and velocidad_flo <= 950):
        print("✅ CRUCERO: Parámetros de vuelo estables y óptimos.")

    else:
        print("PILOTO AUTOMÁTICO: Ajustando alerones y compensando altitud.")
    
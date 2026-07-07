while True:
    print("\n--- Reactor nuclear ---")
    
    print("Ingrese la temperatura:  (SCRAM PARA CANCELAR)\n")
    temperatura = input("TEMPERATURA: ")
    
    if temperatura.upper() == "SCRAM":
        print("🚨 EMERGENCIA MANUAL: Apagando reactor inmediatamente...")
        break
    
    print("Ingrese la presion de la valvula: \n")
    presion = (input("PRESION: "))
    
    if not temperatura and not presion:
        print("Error de lectura en los sensores. Reiniciando escaneo...")
        continue
        
    else:
        temperatura_flo = float(temperatura)
        presion_flo = float(presion)
        
        if temperatura_flo > 1000 or presion_flo > 50:
            print("☢️ PELIGRO CRÍTICO: Fusión de núcleo detectada.")
            
            for protocolo in "12345":
                if protocolo == "1":
                    print("1.- Bajando barra de control...")
                elif protocolo == "2":
                    print("2.- Sellando contención...")
                elif protocolo == "3":
                    print("3.- Desactivando Nucleo")
                elif protocolo == "4":
                    print("3.- Haciendo informe")
                elif protocolo == "5":
                    print("3.- Informando al supervisor")
            break
        
        elif temperatura_flo > 600 or presion_flo > 30 and (temperatura_flo < 1000):
            print("⚠️ ALERTA: Reduciendo inyección de combustible. Sistema inestable.")
        
        elif (temperatura_flo >= 300 and temperatura_flo <= 600) and (presion_flo >= 15 or presion_flo <= 30):
            print("✅ Estado NORMAL: Generación de energía óptima.")
        
        else:
            print("❄️ Estado BAJO: Iniciando secuencia de calentamiento.")
    
    
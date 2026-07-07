while True:
    print("\n--- Escuchando red ---")
    ip_origen= input("Ingrese una IP (Escriba APAGAR para detener): ")
    
    if ip_origen.upper() == "APAGAR":
        print("Firewall desactivado")
        break
    
    puerto = input("Puerto: ")
    protocolo = input("Protoclo (TCP o UDP): ")
    protocolo = protocolo.upper()
    
    if not ip_origen or not puerto or not protocolo:
        print("El paquete esta corrupto por los campos vacios")
        continue
    
    elif protocolo == "ICMP" and puerto == "0":
        print("ALERTA INTENTO DE PING DE LA MUERTE BLOQUEADO")
    
    elif protocolo == "TCP" and (puerto == "80" or puerto == "443"):
        print("Paquete Permitido: Tráfico Web seguro")
    
    elif ip_origen == "66.6.6.6":
        print("ALERTA CRÍTICA: Tráfico desde IP en lista negra")
        
        print("Inciando el aislamiento")
        for action in "123":
            
            if action == "1":
                print("1.- Guardando Logs...")
            elif action == "2":
                print("2.- Asignando red...")
            elif action == "3":
                print("3.- Notificando al admin")
            break
    else:
        print("Paquete Bloqueado: Política por defecto (Drop). No cumple ninguna regla de seguridad.")
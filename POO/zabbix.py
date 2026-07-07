print("--- SISTEMA DE MONITOREO DE RED LITE ---")

#Se crea el diccionario de servidores disponibles
servidores = {
    "WEB_MAIN": "ACTIVO",
    "DB_SQL": "CAIDO",
    "DNS_PRIMARIO": "ACTIVO"
}

alertas_generadas = 0

while True:
    #Menu de opciones
    print("\n--- MENÚ PRINCIPAL ---")
    print("[1] Escanear Red")
    print("[2] Cambiar Estado de Servidor")
    print("[3] Salir")
    
    #Seleccionamos entre las 3 opciones diferentes
    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "3":
        print("Cerrando sistema de monitoreo. La red queda sin supervisión...")
        break
        #Aqui falta un break, si el usuario elige la OP 3, el programa no termina
        
    elif opcion == "1":
        print("\n--- Iniciando escaneo de puertos ---")
        
        #Problemas con el for, se le tiene que agregar .items() para que pueda accerder al contenido del diccionario
        for equipo, estado in servidores.items():
            if estado == "CAIDO":
                print(f"¡ALERTA CRÍTICA! {equipo} no responde al ping.")
                alertas_generadas += 1
                
                #Print colocado adecuadamente
                print(f"Enviando correo al administrador sobre la caída de {equipo}...")
                continue 
                #El mensaje nunca llegara, ya que el "print" se encuentra fuera del if, es por eso que lo colocamos donde debe estar
                
            else:
                print(f"{equipo}: Operando normalmente.")
        
        print(f"\nTotal de alertas enviadas en este escaneo: {alertas_generadas}")

    elif opcion == "2":
        objetivo = input("\nIngrese el nombre del servidor a modificar: ").upper()
        
        # Validamos que el servidor realmente exista antes de cambiarlo
        if not objetivo or servidores:
            print("Error de sintaxis o el equipo no existe en la topología.")
            continue
        
        #En este bloque se que hay un error, pero no se me ocurre como solucionarlo, aqui deje un intento de solucion
        for objetivo,estado in servidores:
            if objetivo.upper() == "CAIDO":
                print(f"Actualmente {objetivo} no responde se encuentra Caido")
                nuevo_estado = input("Ingrese el nuevo estado (ACTIVO o CAIDO): ").upper()
        
        # Actualizamos el estado en la base de datos
        servidores[objetivo] = nuevo_estado
        print(f"Actualización confirmada: {objetivo} ahora está {nuevo_estado}.")

    else:
        print("Opción inválida. Intente de nuevo.")
goles_mundial = {}

while True:
    print("\n--- REGISTRO FIFA MUNDIAL 2026 ---")
    # Convertimos a mayúsculas desde el inicio para estandarizar
    pais = input("Ingrese el nombre del país (Escriba FIN para terminar): ").upper()
    
    if pais == "FIN":
        print("Cerrando registro de partidos...\n")
        break 
        
    goles = int(input(f"Goles anotados por {pais}: "))
    
    # Lógica de Acumulación (Evita la sobreescritura)
    if pais in goles_mundial:
        goles_mundial[pais] += goles # Si ya existe, le sumamos los nuevos goles
    else:
        goles_mundial[pais] = goles  # Si no existe, lo creamos desde cero


# ==========================================
# PROCESAMIENTO DE DATOS (Fuera del while)
# ==========================================

if len(goles_mundial) == 0:
    print("No se registraron datos en el torneo.")
else:
    total = 0
    # Inicializamos nuestro "Rey de la Colina"
    goles_maximos = -1
    pais_goleador = ""
    
    # Usamos .items() para obtener Clave (país) y Valor (goles)
    for pais_actual, goles_actuales in goles_mundial.items():
        
        # 1. Sumamos al total general
        total += goles_actuales
        
        # 2. Buscamos al máximo goleador
        if goles_actuales > goles_maximos:
            goles_maximos = goles_actuales
            pais_goleador = pais_actual

    # Impresión de resultados
    print("==============================================")
    print("|            GOLES EN EL MUNDIAL             |")
    print("|                    2026                    |")
    print("|                MEX-USA-CAN                 |")
    print("==============================================")
    print("\nTABLA DE POSICIONES:")
    print(goles_mundial)
    print("\n================")
    print("| GOLES TOTALES |")
    print(f"|       {total}       |")
    print("================")
    print(f"\n🏆 EL MÁXIMO GOLEADOR ES: {pais_goleador} con {goles_maximos} goles.")
    print("\nSe acabó el mundial... ¡Nos vemos en 2030 :D!")
    
    
    
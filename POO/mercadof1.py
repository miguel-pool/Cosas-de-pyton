print("--- F1 MANAGER 2024: MERCADO DE FICHAJES ---")
#Se crea el diccionario de presupuestos de los equipo
presupuestos = {
    "FERRARI": 100,
    "MERCEDES": 90,
    "WILLIAMS": 30
}
#Los pilotos disponibles a fichar
mercado_pilotos = {
    "BEARMAN": 15,
    "ANTONELLI": 20,
    "COLAPINTO": 10
}
#El diccionario de las alineaciones
alineaciones_custom = {} 

while True:
    
    #Solicitas el nombre del equipo para gestionarlo
    equipo = input("\nIngrese el equipo que desea gestionar (o SALIR): ").upper() 
    
    #En dado caso de que se escriba salir, se termina el programa
    #AUNQUE AQUI ESTA LA PRIMERA TRAMPA, LE FALTA UN BREAK A ESTE BLOQUE
    if equipo == "SALIR":
        print("Cerrando mercado de fichajes...")
        break #Break agregado
    
    #Si no se encuentra algun equipo dentro del diccionario, muestra un mensaje de error y continua su proceso
    if not equipo in presupuestos:
        print("Error: El equipo no existe en la base de datos.")
        continue
    
    #Se pregunta por el piloto para ficharlo
    piloto = input("Ingrese el piloto que desea fichar: ").upper()
    
    #Si no se encuentra en el diccionario, se muestra un mensaje de error de que no esta
    if not piloto in mercado_pilotos:
        print("El piloto no está en el mercado.")
        continue
    
    #De acuerdo al equipo de seleccionado, el presupuesto actual agarra el valor de presupuestos para fichar
    
    presupuesto_actual = presupuestos[equipo]
    
    #De acuerdo al valor del piloto que se busco, la variable costo de piloto adquiere el valor del mercado de piloto
    costo_piloto = mercado_pilotos[piloto]
    
    #Aqui hay otro error, si tu presupuesto actual es menor al valor del piloto, no se tendria que poder ficharlo
    #if presupuesto_actual > costo_piloto:  <--- Asi debio de quedar
    if presupuesto_actual > costo_piloto: #Corregido
        print(f"¡Fichaje exitoso! {piloto} ha firmado un contrato con {equipo}.")
        
        #Casi caigo, pero asi no se guarda un valor en un diccionario
        #alineaciones_custom.append(piloto)
        alineaciones_custom[piloto] = costo_piloto
        
        presupuestos[equipo] -= costo_piloto 
        
    #Si no hay fondos suficientes se muestra un mensaje de aviso de que no hay plata JAJA :(
    else:
        print("Fondos insuficientes. La junta directiva ha rechazado el fichaje.")
        
    #Se muestra el estado actual del mercado de pilotos
    print("\n--- Estado Actual del Mercado ---")
    #Se actualizan los valores de los equipos, al fichar un piloto
    print("Presupuestos restantes:", presupuestos)
    #Se muestran a los pilotos fichados
    print("Alineaciones confirmadas:", alineaciones_custom)
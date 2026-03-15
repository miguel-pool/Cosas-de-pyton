campeonato_2026 = {}
puntos_actuales = 0
puntos_totales = 0
while True:
    piloto = input("Ingresa el nombre de los pilotos de la temporada 2025: ")
    
    if piloto.upper() == "SALIR":
        print("Adios y gracias")
        break
    
    print(f"Inserta los puntos de esta temporada de {piloto}")
    puntos = int(input("Puntos: "))
    
    campeonato_2026[piloto] = puntos 

  
for piloto, puntos_actuales in campeonato_2026.items():
    puntos_totales += puntos_actuales
    
print("Estos son los puntos totales", puntos_totales)
    
    
        
    
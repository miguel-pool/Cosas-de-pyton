contraseña = "python123"
intentos = 0
intentos_max = 3 
acierto = False #bandera

while intentos < intentos_max and acierto == False:
    
    print("Inserte su contraseña ya guardada: ")
    escrito = input("Contraseña: ")
    print()
    if escrito == contraseña:
        print("Bienvenido a su cuenta")
        acierto = True #aqui la bandera cambia de valor a verdadero
    else:
        intentos+=  1
        print("Contraseña erronea")
        print(f"Tienes {intentos_max} maximo y ya tienes {intentos} intentos")
        
    print("\n")        
        
if intentos == intentos_max:      
    print("Ya alcanzaste el maximo de intentos")
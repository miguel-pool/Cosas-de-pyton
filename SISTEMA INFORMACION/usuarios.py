contador = 0

contraseña_guardada = "cisco123"
while True:
    print(
"""
+================================+
| ¡Bienvenido Banca Movil, MK    |
| Introduzca su usuario y        |
| contraseña para acceder        |
| tienes 3 intentos              |
+================================+
""")
    
    contraseña = input("Ingrese su contraseña: ")

    if contraseña != contraseña_guardada:
        print("Te equivocaste... vuelve a intentarlo")
        contador +=1
        print(f"Tienes este {contador} numero de veces intentados")
        
    else:
        print("Accediste al sistema")
        break
    
    if contador == 3:
        print(f"Ya alcanzaste el numero maximo de intentos {contador}")
        break
            
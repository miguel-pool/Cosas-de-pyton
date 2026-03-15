# Variables iniciales
contador = 0
usuario_guardado = "Mike"
contrasena_guardada = "Cisco123"
acceso_concedido = False  # Nuestra "Bandera"

# El banner va afuera para que no haga spam
print(
"""
+================================+
| ¡Bienvenido Banca Movil, MK    |
| Introduzca su usuario y        |
| contraseña para acceder        |
| tienes 3 intentos              |
+================================+
""")

while True:
    usuario = input("Ingrese el usuario: ")
    contrasena = input("Contraseña: ")

    # 1. Primera línea de defensa: Campos vacíos
    if not usuario or not contrasena: # Forma "Pythonica" de evaluar si están vacíos
        print("Error: Los campos no pueden estar vacíos. Intente de nuevo.\n")
        continue # Aquí el continue está bien, no penalizamos por presionar Enter sin querer

    # 2. Segunda línea de defensa: Autenticación
    if usuario == usuario_guardado and contrasena == contrasena_guardada:
        print("\nBienvenido a nuestro sistema, Mike :D")
        acceso_concedido = True # Levantamos la bandera de éxito
        break # Rompemos el while
        
    elif usuario == "admin" and contrasena == "seguridad123":
        print("\nBienvenido Admin, usted tiene todo el acceso.")
        acceso_concedido = True
        break
        
    elif usuario == "invitado" and contrasena == "guest":
        print("\nBienvenido Usuario Invitado. Acceso restringido.")
        acceso_concedido = True
        break
        
    # 3. Si llega hasta aquí, escribió algo pero estaba incorrecto
    else:
        contador += 1
        print(f"Credenciales incorrectas. Intento {contador} de 3.\n")
        
        # Evaluamos si ya se le acabaron los intentos
        if contador == 3:
            print("ALERTA: Ya has alcanzado el máximo de intentos. ¡Sistema BLOQUEADO!")
            break

# --- FUERA DEL WHILE ---
# 4. Secuencia de arranque de servicios (Un solo ciclo for)
if acceso_concedido: # Es lo mismo que decir "if acceso_concedido == True:"
    print("Iniciando servicios...")
    for numero in "123":
        print(f"Cargando servicio de red {numero}...")
    print("Terminal lista.")
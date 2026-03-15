contador = 0

usuario_guardado = "Mike"
contrasena_guardada = "Cisco123"

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
    usuario = input("Ingrese el usuario: ")
    contrasena = input("Contraseña: ")

    
    if usuario == usuario_guardado and contrasena == contrasena_guardada:
        print("Bienvenido a nuestro sistemas :D")
        for numero in "123":
            print(f"Cargando servicio red {numero}...")
        break
    
    elif usuario == "" or contrasena == "":
        print("Alguno de los dos campos no se relleno... Verifique de llenar ambos campos")
        contador +=1
        
    
    elif usuario == "admin" and contrasena == "seguridad123":
        print("Bienvenido admin, usted tiene todo el acceso B)")
        for numero in "123":
            print(f"Cargando servicio red {numero}...")
        break
        
    elif usuario == "invitado" and contrasena == "guest":
        print("Bienvenido Usuario Invitado... ")
        for numero in "123":
            print(f"Acceso restringido {numero}...")
        break
    
    else:
        print("Algo salio mal...Verifique algunos de los dos campos")
        contador +=1
        
    
    if contador == 3:
        print("Ya has alcanzado el maximo de intentos programa BLOQUEADO!!")
        break
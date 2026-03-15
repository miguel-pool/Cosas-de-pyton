modo_privilegiado = False
contraseña = "cisco123"

while True:
    comando = input("Switch >   ")
    
    if not comando:
        continue
    
    if comando.upper() == "SALIR":
        print("Cerrando Conexion")
        break
    
    elif comando.upper() == "ENABLE":
        
        if modo_privilegiado:
            print("Bienvenido al modo privilegiado, ya esta activado")
        else:
            contraseña = input("Contraseña: ")
            if contraseña == "cisco123":
                modo_privilegiado = True
                print(f"Bienvenido, el modo privilegiado esta {modo_privilegiado}")
            else:
                print("Error no es la contraseña")
                
    elif comando.upper() =="CONFIG":
        
        if not modo_privilegiado:
            print("Acceso denegado, requiere modo privilegiado (enable)")
        
        else:
            vlan_input = int(input("Ingrese número de VLAN a configurar (1-1005): "))

            if vlan_input <= 0 or vlan_input > 1005:
                print("VLAN no valida")
                
            else:
                print(f"Iniciando configuración de VLAN {vlan_input}...")
                for paso in "123":
                    if paso == "1":
                        print("1.- Creando VLAN en la base de datos...")
                    elif paso == "2":
                        print("2.- Asignando protocolos de puerto...")
                    elif paso == "3":
                        print("3.- Guardando en NVRAM...")
    else:
        print("Comando no reconocido o incompleto.")
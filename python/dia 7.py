#Diccionario con datos
datos = {80: "HTTP", 443: "HTTPS", 22: "SSH", 21: "FTP"}

print("|----Lista puertos----|")


while True:
    #Pedimos al usuario que puerto desea observar...
    puerto = int(input("Ingresa la clave de los puertos (escribe 0 si deseas salir) "))
    if puerto==0:
        print("Hasta pronto")
        break
    #Verificamos si el puerto se encuentra en el diccionario
    if puerto in datos:
        print("Este es el puerto que solicitas")
        print(datos[puerto])
    #Si no se encuentra, procedemos a printear un mensaje
    else:
        print("Puerto desconocido")
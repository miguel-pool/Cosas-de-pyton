#Mi intento
#inventario = []
#respuesta = ""
#while respuesta != "Salir":
#    respuesta = input("Ingrese nombre del servidor o IP (escriba 'salir' para terminar) \n")
#    inventario.append(respuesta)
#print("Este es el contenido de tu lista", inventario)

#Respuesta
inventario = [] #Mi lista

print("--SISTEMA DE INVENTARIO--")
while True: #Mientras sea verdadero se cumplira la accion
    
    #Se le pide el dato al usuario
    dato = input("Ingrese servidor o IP (escriba 'salir' para terminar):").strip()
    
    #Vereficamos que no sea "salir"
    if dato.lower() == "salir":
        break
    
    #Se agrega el dato a la lista junto con un mensaje de exitso
    inventario.append(dato)
    print(f"Su {dato} fue agregado con exito")
 
#Mostramos mi lista limpia y ordenada  
print("\n--- RESUMEN DE INFRAESTRUCTURA ---")

if len(inventario) > 0:
    for servidor in inventario:
        print(f"-{servidor}")
else:
    print("El inventario esta vacio")
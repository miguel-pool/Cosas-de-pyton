#Agregar tareas y eliminarlas

#lista ya prehecha
lista = ["Instalar python", "Instalar VSC", "Añadir extensiones", "Hacer tu primer Hola mundo"]

print("|----Lista de pasos----|\n")

while True:
    #Mi lista limpia
    print("\nTareas pendientes:")
    for tarea in lista:
        print(f"- {tarea}")
        
    #preguntas por la tarea    
    remover = input("Ya terminaste alguna? (Escribe el nombre exacto): ")
    
    #Si el usuario solo escribe "salir", termina el programa
    if remover.lower()=="salir":
        break
    
    #Si lo que escribe el usuario esta en la lista lo elimnina
    if remover in lista:
        lista.remove(remover)
        print(f"La tarea {remover} fue eliminado")
    else:
        #Si no esta en la lista lo que escribio el usuario, printea un mensaje
        print(f"Error: La tarea '{remover}' no existe en la lista.")

    #Mensaje de felicitaciones
    if len(lista) == 0:
        print("Vientos Terminaste todas las tareas.")
        break
    


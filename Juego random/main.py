import tkinter as tk
from boton_random import dado

main = tk.Tk()
main.title("JUEGO RANDOM")
main.geometry("400x300")

def cambio():
    
    numero_obtenido = dado() #Se llama a la funcion
    
    if numero_obtenido >= 4:
        label_fin.config(
            text = f"Felicidades obtuviste un {numero_obtenido} por lo que GANASTE"
        )
    else:
        label_fin.config (
            text = f"Suerte a la proxima obtuviste un {numero_obtenido} por lo que PERDISTE"
        )
    
h1 = tk.Label(
    main,
    text = "PRUEBA TU SUERTE NE",
   
)
h1.pack()

h2 = tk.Label(
    main,
    text = "Si en el dado sale arriba de 4 GANAS"
)
h2.pack()

boton = tk.Button(
    main,
    text = "SUERTE",
    height= 10,
    width= 10,
    command = cambio
)
boton.pack()

label_fin = tk.Label (
    main,
    text = "" 
)
label_fin.pack()

main.mainloop()
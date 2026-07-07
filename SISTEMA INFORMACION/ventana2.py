import tkinter as tk

#Funcion para obtener el nombre y cambiar el label
def mostrar():
    nombre = entrada.get()
    print("Hola", nombre)
    nombre_label.config(text= f"Hola {nombre}") #cambia el label y agrega el label
    
    
ventana2 = tk.Tk()
ventana2.title("SALUDAR")
ventana2.geometry("400x300")


#Label para el mensaje
label1 = tk.Label(
    ventana2,
    text = "Escribe su nombre"
)
label1.pack()

#Entrada del usuario
entrada = tk.Entry(ventana2)
entrada.pack()

#Boton y comportamiento
boton = tk.Button(
    ventana2,
    text ="Mostrar",
    command = mostrar,
)
boton.pack()


nombre_label = tk.Label(
    ventana2,
    text = ""
)
nombre_label.pack()


ventana2.mainloop()
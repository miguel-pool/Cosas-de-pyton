import tkinter as tk
from IVA import Iva

def cambiar():
    
    texto.config(text="BUSCANDO...", width=20, height=30)
    
ventana = tk.Tk()
ventana.title("QUE ES ESTO?") #TITULO
ventana.geometry("400x300") #Tamaño

texto = tk.Label(ventana, text="PELUCHES RICOS") #Texto
texto.pack() #Es necesario para mostrar el texto en la ventana

boton = tk.Button(ventana, text="BUSCAR", command=cambiar) #Boton
boton.pack() #Es necesario para mostrar el boton en la ventana

ventana.mainloop()
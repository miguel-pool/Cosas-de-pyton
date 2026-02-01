from tkinter import *

ventana =  Tk ()

ventana.geometry ("500x500")
etiqueta = Label (ventana, text = "Hola gente HERMOSAAA ", font = ("Times New Roman", 35, "bold"))
etiqueta.pack()

etiqueta.place ( x=50 , y= 50)

ventana.mainloop()
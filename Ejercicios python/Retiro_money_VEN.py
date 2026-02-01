from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.config (relief= "groove")
ventana.config (bd=20)

def accion():
    messagebox.showinfo (" BBVA "," Iniciando... ")
    pregunta = messagebox.askyesnocancel (" ¿Que deseas hacer? " , " Retirar Efectivo ", )
    print (pregunta)
    
    if pregunta == True:
        #Ventana de retirar dinero
        Ret_dinero = Label (ventana,text= " Retirar dinero ")
        

Usuario = "Cesar Huerta"

#SECTOR DEL USUARIO
Usuario = Label(ventana,text ="Usuario")
Usuario.grid (row = 1,column=0)

entry2= Entry(ventana)
entry2.grid (row=1,column = 1)
    
#PIN
pin = Label (ventana, text="PIN")
pin.grid (row = 2, column=0)

entry3 = Entry(ventana)
entry3.grid (row=2, column=1)
entry3.config (show="*")

boton_listo = Button (ventana, text = " Comprobar ",command= accion)
boton_listo.grid (row = 3, column= 1)

ventana.mainloop()
from tkinter import *
from tkinter import messagebox

def accion ():
    messagebox.showinfo(" Aviso ", " Espere un momento ..." )
    pregunta = messagebox.askyesnocancel (" ¿Que deseas hacer? " , " Retirar Efectivo ", )
    print (pregunta)
    
    
ventana = Tk()
ventana.config (relief= "groove")
ventana.config (bd=20)


#Sector de usuario
usuario = Label (ventana,text=" Usuario" )
usuario.grid (row=1, column= 0)

entry2 = Entry (ventana)
entry2.grid (row=1, column= 1)

#Sector de edad
Edad = Label (ventana , text= " Edad ")  
Edad.grid (row= 2, column=0)

entry3 = Entry (ventana)
entry3.grid (row=2, column= 1)


#Fecha de nacimiento 
Fecha_nacimiento = Label (ventana , text= " Fecha de Nacimiento ")  
Fecha_nacimiento.grid (row= 3, column=0)
entry4 = Entry (ventana)
entry4.grid (row=3, column= 1)

#Contraseña 
Contraseña = Label (ventana , text= " Contraseña ")  
Contraseña.grid (row= 4, column=0)

entry5 = Entry ( ventana)
entry5.grid ( row = 4 , column= 1)
entry5.config (show="*")

boton= Button (ventana, text = " Listo ", command= accion)
boton.grid ( row= 5, column= 1)

ventana.mainloop()
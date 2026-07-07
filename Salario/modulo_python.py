import tkinter as tk
from interfaz import *
from eventos import calcular

boton_suma = tk.Button(
    ventana,
    text="Salario bruto",
    command=lambda: calcular("1", entrada1, entrada2, resultado)
)
boton_suma.pack(pady = (5,5))

boton_resta = tk.Button(
    ventana,
    text="Bono 10%",
    command=lambda: calcular("2", entrada1, entrada2, resultado)
)
boton_resta.pack(pady = (5,5))

boton_multi = tk.Button(
    ventana,
    text="Descuento del 8%",
    command=lambda: calcular("3", entrada1, entrada2, resultado)
)
boton_multi.pack(pady = (5,5))

boton_dividir = tk.Button(
    ventana,
    text="Salario Neto",
    command=lambda: calcular("4", entrada1, entrada2, resultado)
)
boton_dividir.pack(pady = (5,5))

ventana.mainloop()
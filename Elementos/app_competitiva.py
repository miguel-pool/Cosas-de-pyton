import tkinter as tk
from backend_combate import dano

app_competitiva = tk.Tk()
app_competitiva.title("ARENA DE BATALLA")
app_competitiva.geometry("400x400")

def resultado():
    ataque_ingresado = attack.get().upper()
    defensa_ingresada = defence.get().upper()
    
    daño_final = dano(ataque_ingresado, defensa_ingresada)
    # 3. MOSTRAR: Le inyectamos el resultado al texto del Label
    resultados.config(text=daño_final)

h1 = tk.Label (
    text = "COMBATES FRENETICOS",
    font= "Arial",
)
h1.pack()

espacio = tk.Label()
espacio.pack()

mensaje= tk.Label(
    text = "Escribe tu ATAQUE",
    font = "extrabold"
    
)
mensaje.pack()

attack = tk.Entry(
    font="Times_New_Roman",
    width=20,
)
attack.pack()

espacio = tk.Label()
espacio.pack()

mensaje= tk.Label(
    text = "Escribe tu DEFENSA",
    font = "extrabold"
    
)
mensaje.pack()
defence = tk.Entry(
    font="Times_New_Roman",
    width=20,
)
defence.pack()

espacio = tk.Label()
espacio.pack()

calcular = tk.Button(
    
    text = "Calcular",
    font="Arial",
    background="red",
    border="5",
    command=resultado
)
calcular.pack()

resultados = tk.Label(
    font=("Arial", 12, "bold"), # Le puse negrita para que resalte
    width=30,
    text="",
    fg="blue" # Color de letra para que se distinga
)
resultados.pack()

app_competitiva.mainloop()
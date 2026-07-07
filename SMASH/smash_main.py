import tkinter as tk
from combate import generar_partida
from tkinter import messagebox

smash_main = tk.Tk()
smash_main.title("Generador de partidas")
smash_main.geometry("500x500")


def armar_reta():
    # A. Extraemos el Alias
    alias = player1.get()
    
    # B. Extraemos el Listbox (Validando que sí haya elegido algo)
    seleccion = personaje.curselection()
    if not seleccion:
        messagebox.showerror("Error", "¡No olvides elegir a tu personaje!")
        return # Aborta la función si no hay selección
        
    personaje_elegido = personaje.get(seleccion)
    
    # C. Extraemos el Radiobutton (Modo)
    modo_elegido = variable_modo.get()
    
    # D. Extraemos el Checkbutton (Objetos). 1 es encendido, 0 es apagado
    if variable_objetos.get() == 1:
        estado_objetos = "Permitidos"
    else:
        estado_objetos = "Apagados"
        
    # E. Le mandamos todo al Back-End y guardamos lo que nos responde
    resultado_final = generar_partida(alias, personaje_elegido, modo_elegido, estado_objetos)
    
    # F. Mostramos el Pop-up de Windows
    messagebox.showinfo("¡FIGHT!", resultado_final)


h1 = tk.Label(
    text = "SMASH BROS UTG",
    font=("Arial", 20, "bold"),
    fg="orange"   
)
h1.pack()

p1 = tk.Label(
    text= "Ingresa tu Alias >:D",
    font=("Arial", 10, "bold"),
    fg="red"
)
p1.pack()

player1 = tk.Entry(
    font=("Arial"),
)
player1.pack()

p2 = tk.Label(text="\nElige tu Main:", font=("Arial", 10, "bold"))
p2.pack()


personaje = tk.Listbox(height=10)
#List box asi se llenan
#=============================
for fighter in ["Ness", "Mario", "DK", "Link","Checo","Kirby", "Luigui", "Samus", "Lucina", "Lanzaguisantes"]:
    personaje.insert(tk.END, fighter)
personaje.pack()
#====================================

# Para los Radiobuttons (Guardará texto):
p3 = tk.Label(text="\nModo de juego:", font=("Arial", 10, "bold"))
p3.pack()

variable_modo = tk.StringVar(value="Stock") 
radio1 = tk.Radiobutton(smash_main, text="Vidas", variable=variable_modo, value="Stock")
radio2 = tk.Radiobutton(smash_main, text="Tiempo", variable=variable_modo, value="Time")
radio1.pack()
radio2.pack()

# Para el Checkbutton (Guardará 1 si está activado, 0 si está desactivado):
variable_objetos = tk.IntVar()
check_obj = tk.Checkbutton(smash_main, text="Permitir Objetos", variable=variable_objetos)
check_obj.pack(pady=15)


boton = tk.Button(text="Generar Partida", font=("Arial", 12, "bold"), bg="red", fg="white", command=armar_reta)
boton.pack()


smash_main.mainloop()
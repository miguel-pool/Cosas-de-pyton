
import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora de salario")
ventana.geometry("350x300")
ventana.resizable(True, True)


#TITULO
titulo = tk.Label(
    ventana,
    text="Calculador de precio",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

#Numero
lbl_num1 = tk.Label(
    ventana,
    text="Horas trabajada:"
)
lbl_num1.pack()

entrada1 = tk.Entry(
    ventana,
    width=25,
    justify="center"
)
entrada1.pack(pady=5)

# ---------- Numero 2 ----------
lbl_num2 = tk.Label(
    ventana,
    text="Salario por hora"
)
lbl_num2.pack()

entrada2 = tk.Entry(
    ventana,
    width=25,
    justify="center"
)
entrada2.pack(pady=5)

# --------------- RESULTADO ----------
resultado = tk.Label(
    ventana,
    text="Resultado:",
    font=("Arial", 12, "bold")
)
resultado.pack(pady=15)
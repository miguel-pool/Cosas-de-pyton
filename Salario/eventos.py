from operaciones import bruto, bono, descuento, neto 

def calcular(opcion, entrada1, entrada2, resultado):

    num1 = float(entrada1.get())
    num2 = float(entrada2.get())

    if opcion == "1":
        res = bruto(num1, num2)

    elif opcion == "2":
        res = bono(num1, num2)

    elif opcion == "3":
        res = descuento(num1, num2)

    else:
        res = neto(num1, num2)

    resultado.config(text=f"Resultado: {res}")
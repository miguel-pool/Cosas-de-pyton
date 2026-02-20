def conver_fahre(temp):
    calculo = (temp * 9/5) + 32
    return calculo

temperatura_usuario = float(input("Ingrese la temperatura en Celcius: "))
resultado = conver_fahre(temperatura_usuario)
print("Esta es la temperatura covertida de C -> F: ", resultado)

from operaciones_basicas import suma, resta, division,multiplicacion

print("Inserte los 2 valores de a y b")
a = int(input("A > "))
b = int(input("B > "))

resultado_suma = suma(a,b)
resultado_resta = resta(a,b)
resultado_division = division(a,b)
resultado_multiplicacion = multiplicacion(a,b)

print("Resultado de suma: ", resultado_suma)
print("Resultado de resta: ", resultado_resta)
print("Resultado de division: ", resultado_division)
print("Resultado de multiplicacion: ", resultado_multiplicacion)
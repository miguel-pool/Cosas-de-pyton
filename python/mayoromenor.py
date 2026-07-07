def comparador(lista_numeros):
    numero_mayor_actual = lista_numeros[0]
    
    for numero in lista_numeros:
        if numero > numero_mayor_actual:
            numero_mayor_actual = numero
    return numero_mayor_actual

numeros = []

print("Cantidad de numeros")
cantidad = int(input("> "))

for numero in range(cantidad):
    print("Ingresa los numeros que desees")
    digito = int(input("> "))
    numeros.append(digito)
    
print("El numero mas grande es: ",comparador(numeros))
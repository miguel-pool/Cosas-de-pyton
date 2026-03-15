palabra_secreta = "chupacabra"
palabra_insertada = ""

while palabra_insertada != palabra_secreta:
    palabra_insertada = input("Ingresa la palabra: ")
    
    if palabra_insertada == palabra_secreta:
        print("Has dejado el bucle con éxito.")
        break
    
    else:
        print("Sigue intentado")
numero_secreto = 777
numero_ingresado = 0
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

while numero_ingresado != numero_secreto:
    numero_ingresado = int(input("Ingresa el numero: "))
    
    if numero_ingresado == numero_secreto:
        print("¡Bien hecho, muggle! Eres libre ahora.")
        break
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
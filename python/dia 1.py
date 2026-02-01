#Ejercicio dia 1 python
#Club nocturno
entrada = 200
edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("Eres menor de edad mi chavo, no puedes entrar")

else:
    print(f"La cuota es de {entrada} pesos")
    cartera = int(input("¿Cuanto dinero tiene? "))
    dine_total = cartera - entrada
    if cartera < 200:
        print("Lo siento no tienes dinero suficiente")
    else:
        print("Disfruta de la fiesta")
    print(f"Te queda {dine_total} pesos")
    
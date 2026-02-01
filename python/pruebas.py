print("hola soy miguel")

print("    *        " *3)
print("   * *       " *3)
print("  *   *      "*3)
print(" *     *     "*3)
print("***   ***    "*3)
print("  *   *      "*3)
print("  *   *      "*3)
print("  *****      "*3)

print()

print("mi \nnombre \nes \nMiguel. " ,end="") #End dependiendo de lo que coloquemos luego ded el es lo que pondra en la linea de codigo (es como si se fusionara la liena 14 y 15 en una sola)
print("Tengo 19 años")
print( "fish", "chips",sep="&") #Sep es el separador, mostrara el texto, separado de lo que le digamos
print()

print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
print('"Greg\'s book."')

print()

print(0x123) #Valor exadecimal
print(0.0000000000000000000001)
print(1.0000000000000000000000)

print()

print("Me gusta \"Monty Python\"")
print("Soy miguel o tambien \"MKZ para los amigos\"")
print('I\'m Miguel Pool')

print()

print(4 + 4) #Suma normal
print(4 - 2) #Resta normal
print(4 * 4) #Multiplicacion
print(4 ** 4) #Dependiendo de la variable que se encuentra a la derecha es la cantidad
              #De veces que se multiplicara la izquierda
print(4 / 2) #Divison normal
print(4 // 2) #Division entera, da igual que hagas el resultado es entero
print(4 % 2) #Residuo
print(+2)

#Cada uno tiene una prioridad y valor.

juan = 3
maria = 5
adan = 6

manzanas_tot = juan + maria + adan
print("Juan tiene",juan, "manzanas")
print("Maria tiene",maria,"manzanas")
print("Adan tiene", adan, "manzanas")
print("La suma de los 3 da un total de",manzanas_tot,"manzanas")

#Convetidor de millas a kilometros
#print("Bienvenido al convertidor de millas a kilometros")
#kilometros = float(input("Inserte los kilometros: "))
#millas = float(input("Inserte sus millas: "))

#kilometros_a_millas = kilometros /1.61
#millas_a_kilometros =  millas * 1.61

#print(millas,"millas son", round(millas_a_kilometros,4), "kilometros")
#print(kilometros,"kilometros son", round(kilometros_a_millas,4), "millas")

print("*" + 10 * "=" + "*")
print(("|" + " " * 10 + "|\n")* 10, end="")
print("*" + 10 * "=" + "*")

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)



z = y = x = 1
print(x, y, z, sep='*')

n = int(input("Ingresa un numero: "))
resultado = n >= 100
print(resultado)



Espatifilo = input("¿Que plantas deseas? ")


if Espatifilo == "Espatifilo":
    print("Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!")

elif Espatifilo == "espatifilo":
    print("Yo quiero un gran Espatifilo")

else:
    print(f"¡Yo quiero Espatifilo!,NO {Espatifilo}")
    
    
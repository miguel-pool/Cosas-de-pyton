### Operadores Aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(12 % 3)
print(3 / 4)
print(10 / 3) # Este es el ejemplo
print(10 // 3) # Busca aproximar a numeros enteros las divisiones que terminan en decimal
print(3 ** 3) # Significado de las Potencias

print("Elza" + "pato")
print("Hola " * 5)
# print("Hola " * 2.5) # No es valido por ser Float o tener decimal
# print("Hola " * (2.5 * 2)) # No es valido por seguír manteniendo el tipo Float, osea, no seria "5" sino "5.0"

### Forma de solucionarlo ###
#Cambiar el Type
Ola = 2.5 * 2
print("Hola " * int(Ola))
print(Ola)

### Operadores Comparativos ###

print(3 < 4)
print(3 > 4)
print(4 == 4)
print(3 >= 4)
print(3 <= 4)
print(3 != 4)

# Puede ser tambien en Strings
print("Hola" < "zapato")
print("Hola" > "zapato")
print("Hola" <= "zapato")
print("Hola" >= "zapato")
print("Hola" != "zapato")
print("Hola" == "Bola") # Ordenacion alfabetica (Tambien se guia de las mayusculas)

### Operadores logicos ### "Algebra Booleana"

print(3 < 4 and "Hola" < "zapato")
print(3 < 4 or "Hola" < "zapato")
print(3 < 4 and "Zapato" < "Hola")
print(3 < 4 and "Zapato" > "Hola")
print(not(3 < 4)) # Niega la condicion, osea, 4 es mayor a 3, pero se niega.


print("Hola como estamos?")
nombre = str(input("Ingresa tu nombre: "))


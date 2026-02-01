### Funciones Básicas y Variables ###

print("Hola_mundo")

# Variables
nombre, apellido, años, alias = "victor", "ramirez", 18, "Vitico"
print("Mi nombre es:", nombre, apellido, ". Mi edad es:", años, "Y mi alias es:", alias)
x = "Pe"
y = "lona"
z = x + y
num1 = "Zapato"

print("Ariana se va a pintar el cabello, pero se le fué la mano con el tinte, entonces quedó:", z)

# Tipo de cada funcion
print(type("Hola_mundo"))
print(type(5))
print(type(3.2))
print(type(3j))
print(type([1, 2, 3, 4]))
print(type(print(z, num1, x, y))) # Tipo "None Type" (El 'print' no tiene tipo)

# Cadena de varialbles en print
print(x, y, num1, z)

# Len (Cuenta la variable. letras en caso de las palabras)
print(len(num1))

# Inputs
Primer_nombre= input("Cual es tu nombre? ")
Edad= input("Cual es tu edad? ")

print(Primer_nombre)
print(Edad)

# Cambiamos su tipo
Primer_nombre = 18
Edad= "Victor"

# Forzar el tipo de una variable

pepe: str = "25" # Este no
pepe= 25 # se toma como pricipal
print(pepe)
print(type(pepe))
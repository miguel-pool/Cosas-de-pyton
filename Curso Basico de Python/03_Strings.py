### Stings ###

prueba = "Olas"
prueba2 = 'Holas'

print(len(prueba))
print(len(prueba2))

print(prueba + prueba2)

prueba3 = "Este es un String\ncon salto de linea"
print(prueba3)

prueba4 = "\tString con tabulacion"
print(prueba4)

prueba5 = "\tEste es un string\ncombianado"
print(prueba5)

# Formateo
# %s = String
# %d = Enteros/numeros ayuda a la correcion en caso de poner un texto.

name, surname, age = "Vitico", "wao", 18

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Con el .format

print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Con el %s y %d

print("Mi nombre es ", name, surname, ". Y mi edad es: ", age) # Directo con las variables

print(f"Mi nombre es {name} {surname} y mi edad es {age}") # La "f" foramtea e infiere el valor del dato dentro de las llaves.

# Desempaquetado de caracteres

Language = "python"
a, b, c, d, e, f = Language

print(a)
print(c)

# Division

Language2 = Language[1:3] #Empieza a contar desde el 0
print(Language2)

Language2 = Language[1:] #Lo imprime todo desde la 1 en adelante porque solo fija el inicio
print(Language2)

# Reversa

Revez = Language[::-1] # El final inicia en -1 porque no hay un -0
print(Revez)

# Metodos/Funciones del sistema

print(Language.capitalize()) # Empieza por mayuscula las palabras
print(Language.upper()) # Full Mayusculas
print(Language.count("y")) # Cuenta la cantidad de letras que pusimos en el parentesis 
print(Language.isnumeric()) # Dice en formato bool (verdadero o falso)
print("1".isnumeric()) # Identifica si es numero
print(Language.lower()) # Full minusculas
print(Language.upper().islower()) # Combinacion True/False
print(Language.upper().isupper()) # Combinacion True/False
print(Language.startswith("Py")) # Ideentifica si la palabra empieza con la letra dentro del () 
print("Py" == "py") # No son lo mismo

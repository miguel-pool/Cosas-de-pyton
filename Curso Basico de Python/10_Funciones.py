### Funciones ###

def my_function (): # Forma de definir una funcion
    print("Esto es una funcion")

my_function()

x = int(input("Ingresa el primer numero: "))
x1 = int(input("Ingresa el segundo numero: "))
List = [5,6,9,10]
List2 = [3,5,12,7]

def Suma (n, n1):
    print("La suma de tus valores es: ",n + n1)
    
Suma(x, x1) # Es el valor que tendra la funcion
Suma("5", "3")
Suma(1.2, 6.7)
Suma(List, List2)

### Retorno ###

def Suma_con_retorno (n, n1):
    return n + n1

result = Suma_con_retorno (10,5) #Nos sirve para almacenar el dato de la funcion return
print("El resultado es: ", result)

result = Suma_con_retorno (1.2, 5.2) #Nos sirve para almacenar el dato de la funcion return
print("El resultado es: ", result)

### Funciones de orden ###

def Print_name (nombre, apellido, edad):
    print(f"Mi nombre y apellido son {nombre} {apellido} y mi edad: {edad}")

#Print_name("Victor", "Ramirez", 18) #Le doy el valor a las variables en orden.
Print_name(apellido="Ramirez", edad=18, nombre="Victor") #Se pueden poner en desorden pero dandole el valor de la variable.

def Print_name (nombre, apellido, edad = "No se sabe"): #Si no se ingresa el valor de una variable, podemos darle un valor en caso de que no se le haya dado.
    print(f"Mi nombre y apellido son {nombre} {apellido} y mi edad: {edad}")

Print_name("Victor", "Ramirez")
Print_name("Victor", "Ramirez", 18)


def print_text(text):
    print(text)

print_text("Hola")

def print_textos(*textos): #Si le ponemos un asterisco, podemos agregar valores infinitos, todos los que queramos. no es necesario definirlos
    print(textos)

print_textos("Hola", "Mundo", "Somos", "Grandes")

### Se le pueden poner bucles para cambiar sus imprimir o cambiar su forma ###

def print_textos(*textos): #Si le ponemos un asterisco, podemos agregar valores infinitos, todos los que queramos. no es necesario definirlos
    for text in textos:
        print(text.upper())

print_textos("Hola", "Mundo", "Somos", "Grandes")


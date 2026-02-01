### Classes ###

#### Los nombres de las clases en vez de ser asi "Soy_yo", sera asi: SoyYo ####

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson()) # Se puede ejecutar de ambas maneras.


class Person1: #Creacion de una clase
    pass #Es la forma de intentar que se ejecute y no de error si no le damos valor a la clase


## Como guardar valor en la clase y darle una propiedad de valor a la clase.
## El self es necesario como argumento para darle valor a las clases.

class Person:
    def __init__(self, nombre, apellido): #__init__ es reservado para darle la capacidad de recibir un parametro a la clase. (Constructor)
        self.nombre = nombre #Forma de dar valor a una variable de la clase.
        self.apellido = apellido #Forma de almacenar el dato en la clase.
#        pass #Anula

my_person = Person("Victor", "Ramirez")
print(f"Mi nombre es {my_person.nombre} y mi apellido {my_person.apellido}")

## Tambien podemos definir el valor directamente ## 
class Person2:
    def __init__(self):
        self.fullname = "Victor Manuel Ramirez Bustamante" #Valor directo de lo que queremos que tenga la clase.

Nombre_c = Person2()
print(Nombre_c.fullname)

## Tambien podemos definirlo por partes ##

class Person3:
    def __init__(self, name, surname):
        self.nombreF = f"{name} {surname}"

nombre_full = Person3("Vitico", "Ramirez") #Le damos el valor a la variable name y surname 
print(nombre_full.nombreF)


print(type(nombre_full)) #Podemos observar la clase que creamos.

## Ejemplo de como podemos agregar "acciones"/"funciones" ##

class Person4:
    def __init__(self, name, surname, alias = "Sin alias"): #se puede combinar con lo anterior visto.
        self.nombrefull = f"{name} {surname} ({alias})" #Propiedad publica
        self.__name = name #Podemos definir la variable como privada
                             #Podemos definir la variable como privada Con "__variable"

    def get_name (self): #Esto es para poder acceder a la variable __name , pero no podemos modificarla.
        return self.__name 

    def walk (self):
        print(f"{self.nombrefull} esta caminando") #Con self podemos llamar a todos los valores que tenga self Ej: "self.nombreFull"

my_persona = Person4("Victor", "Ramirez") # Si no ponemos un alias, se le da el valor principal.
print(my_persona.nombrefull)
my_persona.walk()

my_persona = Person4("Victor", "Ramirez", "Vitico") # Asignamos name y surname y forma el "nombrefull"
print(my_persona.nombrefull)
my_persona.walk() #Podemos llamar a las funciones he imprimirlas

my_persona.nombrefull = "Vitico (El Humilde)" # Podemos modificarlo despues de creado.
print(my_persona.nombrefull)

my_persona.nombrefull = 2006 # Podemos modificar el tipado como querramos.
print(my_persona.nombrefull)



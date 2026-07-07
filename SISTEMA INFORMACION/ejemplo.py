class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    
persona1 = Persona("Ana", 20)
persona2 = Persona("Luis", 18)

class Carro:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

carro1 = Carro("Rojo", "Nissan Versa")
carro2 = Carro("Negro", "Suzuki Swift")

print(f"Hola mi nombre es {persona1.nombre} y tengo la edad de {persona1.edad} y mi carro es {carro1.marca} de color {carro1.color}")
print(f"Hola mi nombre es {persona2.nombre} y tengo la edad de {persona2.edad} y mi carro es {carro2.marca} de color {carro2.color}")



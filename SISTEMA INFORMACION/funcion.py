#saludo
def saludar(nombre):
    return print("Hola", nombre)

personas = []

print("A cuantas personas quieres saludar hoy?")
saludos = int(input("Saludos: "))

for saludos in range(saludos):
    print("Ingresa el nombre")
    nombre = input("> ")
    personas.append(nombre)

for persona in personas:
    saludar(persona)
    
  
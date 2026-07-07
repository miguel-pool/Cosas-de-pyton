def contador(lista_pilotos, pilotos):
    pilotos_registrados = 0
    
    for pilotos in lista_pilotos:
        pilotos_registrados+=1
    
    return pilotos_registrados

pilotos = []

print("Pilotos a registrar (Cantidad)")
cantidad = int(input("> "))


for alumno in range (cantidad):
    print("Ingrese el nombre de los pilotos")
    piloto = input("Pilotos de F1 > ")
    pilotos.append(piloto)


print("===============================")
print(f"Lista de pilotos: {pilotos}")
print(f"El total de pilotos registrados es: {contador(pilotos, cantidad)}")
print("===============================")
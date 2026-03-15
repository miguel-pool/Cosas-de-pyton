tabla = int(input("Que tabla deseas: "))
rango = int(input("Hasta donde quieres la tabla: "))

for i in range (1,rango+1): 
    print(f"El resultado de {tabla} por {i} es igual a {tabla * i}")
numeros_list = []

for i in range (10):
    numero = int(input(f"Ingrese {i} numeros: "))
    numeros_list.append(numero)
    

numeros_conjunto = set(numeros_list)


print("Esta es la lista: ", numeros_list)
print("Esta es la cantidad de datos sin repetir",len(numeros_conjunto))
print("Este es el conjunto",numeros_conjunto)

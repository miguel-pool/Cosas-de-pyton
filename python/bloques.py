height = 0
blocks = int(input("Ingresa el número de bloques: "))

while blocks >= 0:
    height += 1
    blocks -= height
    print("Altura actual:", height, "Bloques restantes:", blocks)
    
print("La altura de la pirámide es:", height - 1)

    

    


Datos = [10,10,10]

cuenta0 = 0
cuenta1 = 0
cuenta2 = 0
cuenta3 = 0

for i in range (0 , 150):
    if Datos[i] >=259 and Datos[i]<= 400:
        cuenta0 += 1
        
    if Datos[i] >= 329   and Datos[i]<=629:
        cuenta1 += 1
        
    if Datos[i] >= 630 and Datos[i]<=930:
        cuenta2 += 1
        
    if Datos[i] >= 931 and Datos[i]<=1230:
        cuenta3 += 1
        
    

print(cuenta0)
print(cuenta1)
print(cuenta2)
print(cuenta3)


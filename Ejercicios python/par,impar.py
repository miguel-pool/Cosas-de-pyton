
Par = 0
impar = 0


for i in range (10):
    num = int (input (f" Dame 10 numeros enteros de tu elección {i+1}: "))
    
    if num % 2  == 0:
        Par += 1
    else:
        impar += 1
    #Considerar que ahora de imprimir ponerlo fuera del if y else   
print (f" Este es la cantidad numeros pares ", {Par})
print (f" Este es la cantidad de numeros impares ", {impar})
    
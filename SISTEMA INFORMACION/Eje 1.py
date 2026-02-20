print("---Bienvenido a este sistema---")
a = int(input("Inserte el primer valor: "))
b = int(input("Inserte el segundo valor: "))


#Suma
resultado = a + b

#Resta
resul_res = a - b

#Multiplicacion
resul_multi = a * b

#Division
if b == 0:
    print("No se puede dividir entre 0")
else:
    resul_divi = a / b
       
print("La suma de los dos numeros es ", resultado)
print("La resta de los dos numeros es ", resul_res)
print("La multiplicacion de los dos numeros es ", resul_multi)
print("La division de los dos numeros es ", resul_divi)

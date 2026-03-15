print("Porgrama de identificacion")

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num1 > num2:
    print(f"El numero mayor de los es el numero 1 {num1}")
elif num2 == num1:
    print(f"Ambos numeros son iguales {num1} == {num2}")
else:
    print(f"El numero mayor de los es el numero 2 {num2}")
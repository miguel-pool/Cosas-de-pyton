import math
print("Bienvenidos a la calculadora")


print("--Menu--")
print("1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\n5.-Raiz\n6.-Salir")
op =int(input("Selecciona una opcion: "))
    
if op < 1 or op > 6:
  print("Opcion no valida")
  
elif op == 1:
  a = float(input("Inserta el primer valor: "))
  b = float(input("Inserta el segundo valor: "))
  suma = a + b
  print(f"El resultado de la suma de los 2 numeros:{suma}")

elif op == 2:
  a = float(input("Inserta el primer valor: "))
  b = float(input("Inserta el segundo valor: "))
  resta = a - b
  print(f"El resultado de la resta de los 2 numeros: {resta}")
  
elif op == 3:
  a = float(input("Inserta el primer valor: "))
  b = float(input("Inserta el segundo valor: "))
  multiplicacion = a * b
  print(f"El resultado de la multiplicacion de los 2 numeros: {multiplicacion}")
  
elif op == 4:
  a = float(input("Inserta el primer valor: "))
  b = float(input("Inserta el segundo valor: "))
  
  if b == 0:
    print("No se puede divir entre 0")
    b = float(input("Inserta el segundo valor: "))
    
  division = a / b
  print(f"El resultado de la division de los 2 numeros: {division}")

elif op == 5:
  a = float(input("Inserta el valor: "))
  raiz = math.sqrt(a)
  if a <= 0:
    print("No se le puede sacar raiz a un 0 numero negativo ")
    a = float(input("Inserta el primer valor: "))
    
  print(f"La raiz cuadrada de este numero es: {raiz}")
  
elif op == 6:
  print("Vuelva pronto :D")
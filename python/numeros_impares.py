#Verificar cuales son los numeros pares e imprimirlo
for i in range(1, 11):
    if i%2 == 1:
        print(f"El numero {i} es impar")

print("")

#Verificar cual numero es impar e imprimirlo con while
x = 1
while x < 11:
    x +=1
    if x %2 == 1:
        print(f"El numero {x} es impar")

print("")

#Imprimir lo anterior a @
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
    
print("")

#Cambiar ceros por X
for digit in "0165031806510":
    if digit == "0":
        continue
    print(digit, end = "X")
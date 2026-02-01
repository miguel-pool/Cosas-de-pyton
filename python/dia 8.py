def celcius_a_fahrenheit(celsius):
    (celsius * 9/5) + 32
    return celsius

celsius = int(input("ingresa la temperatura: "))
print("Este es el resultado en fahrenheit",celcius_a_fahrenheit)
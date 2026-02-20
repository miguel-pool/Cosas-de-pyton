animales =  ["Caballo","Gato", "Perro", "Loro", "Cocodrilo", "Pez"]
numeros = [10,20,30,40,50,60,70]

#Recorriendo la lista y cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#Recoriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")

#la funcion zip nos ayuda a recorrer 2 listas al mismo tiempo NOTA: SE PUEDE CON MAS DE 2 LISTAS
for numero, animal in zip(animales,numeros):
    print(f"recorrriendo lista 1: {animal}")
    print(f"recorrriendo lista 1: {numero}")

#Con range le decimos al codigo de donde comienza a donde termina NOTA: EL ULTIMO NUMERO NO CUENTA
for num in range (5,11):
    print(num)

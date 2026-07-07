#Verificar mayoría de edad
def comparador(edad):
    if edad >= 18:
        print("Tu edad es de ", edad, ", Asi que eres permitido")

    else:
        print("ALTOO tu edad es de ", edad, ", Asi que no puedes pasar")
        

print("==============================")
print("Verificador de mayoria de edad")
print("Ingresa tu edad")
edad = int(input("> "))
comparador(edad)
print("==============================")
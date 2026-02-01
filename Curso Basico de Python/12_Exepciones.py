### Exepciones (Manejo de errores) ###

print("Inicio de las pruebas")

n0 = 5
n1 = 1
n1 = "1"

# print(n0 + n1) #Error por ser datos diferentes

#if type(n1) == int: # con esto solo podriamos controlar errores especificos que conozcamos.
#    print(n0 + n1)
#else:
#    print("No se cumplio")


### Esta sentencia nos ayuda a hacer pruebas y identificar cuando se produce un error, esto sin que el programa se tilde o quiebre. ###
# try except

try:
    print("La suma de tus numeros es:", n0 + n1)
    print("No se ha producido Error")
except:
    print("Se ha producido un error")

# try except else

try:
    print("La suma de tus numeros es:", n0 + n1)
    print("No se ha producido Error")
except:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")
else: # Opcional
    # Solo se ejecuta si no se ha producido el Error o no se ejecuta la excepcion
    print("La ejecucion continua correctamente") 
finally: # Opcional
    # Se ejecuta siempre, pase lo que pase.
    print("La ejecucion continua")

# Excepcion por tipo
# Nos sirve para capturar errores especificos

try:
    print("La suma de tus numeros es:", n0 + n1)
    print("No se ha producido Error")
except ValueError: # Se ejecuta solo cuando sucede el error que especificamos despues del Except
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un ValueError")
except TypeError: 
    print("Se ha producido un TypeError")

# Captura de la info de la excepcion

try:
    print("La suma de tus numeros es:", n0 + n1)
    print("No se ha producido Error")
except ValueError as error: #Controla el error y nos da la informacion del porque del error. Es la variable que tiene la info del error
    print(error)
except Exception as error2: # Para excepciones genericas
    print(error2)



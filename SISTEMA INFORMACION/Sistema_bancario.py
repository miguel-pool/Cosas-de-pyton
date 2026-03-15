usuario = "usuario"
contraseña = "cisco123"
saldo = 150.00
op = ""

while True:
    print(""""
    |--------------------|
    | Bienvenido al      |
    | sistema bancario   |
    | VVBI               |
    | Ingrese su usuario |
    | y contraseña       |
    |--------------------|
    """)
    
    print("1.-Consulta saldo\n2.-Depositos\n3.-Retiros\n4.-Salir")
    opcion = input("¿Que deseas hacer? ")
    
    if opcion == "1":
        print(f"Su saldo actual es ${saldo} MN")
        print("Desea salir de esta opcion? ")
        print("")
        
    if opcion == "2":
        print("¿Cuanto deseas agregar a tu cuenta?")
        saldo_ingresado = int(input("Saldo: "))
        saldo_total = saldo + saldo_ingresado
        print(f"Su saldo total es {saldo_total}")
    
    if opcion == "3":
        print("¿Cuanto dinero retiraras? ")
        saldo_ingresado = int(input("Retiro: "))
        saldo_total = saldo - saldo_ingresado
        if saldo < saldo_ingresado:
            print("El saldo de retiro es insuficiente")
        else:
            print(f"Se retiro esta cantidad {saldo_ingresado} y le queda {saldo_total}")
    
    if opcion == "4":
        print("Gracias por usar VVBI :D")
        break
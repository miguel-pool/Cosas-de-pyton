saldo = 0
op = 0

while op != 4:
    print("\n--- MENÚ BANCARIO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir del programa\n")

    op = int(input("Seleccione una opción: "))

    if op == 1: #consulta de dinero
        print(f"\nTu saldo es: {saldo}")

    elif op == 2: #deposito de dinero
        saldo_deposito = float(input("\nMonto de la transferencia: "))
        if saldo_deposito > 0:
            saldo += saldo_deposito
            print(round(f"Se han depositado con exito ${saldo_deposito}"))
        else:
            print("Ingresó una cantidad negativa.")
        

    elif op == 3: #retiro de dinero
        print("\n¿Cuanto dinero retiraras? ")
        
        saldo_ingresado = float(input("Retiro: "))
            
        if saldo_ingresado >= 0:
            if saldo < saldo_ingresado:
                print("\nEl saldo de retiro es insuficiente")
            else:
                saldo = saldo - saldo_ingresado
                print(round(f"\nSe retiro esta cantidad ${saldo_ingresado} y le queda ${saldo}"))
        else:
            print("No puede retirar saldo negativo!")

print("Gracias por usar nuestra banca digital!")
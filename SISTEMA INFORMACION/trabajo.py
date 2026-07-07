
monto_ven = float(input("Ingresa un monto de venta: "))

if monto_ven >= 1000:
    descuento = monto_ven * .10
    monto_fin = monto_ven - descuento
    print("El monto final es ", monto_fin)
    print("Su descuento fue de ", descuento)
    
else:
    print("No aplica el descuento, asi que su monto es ", monto_ven)
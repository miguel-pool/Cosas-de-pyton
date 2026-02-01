
print (" Inserte los costos de los productos ")
#Convertir un dato del teclado a float(decimal)... (Para entero recuerda que es INT)
Product_1= float (input (" Precio: "))
Product_2= float (input (" Precio: "))
Product_3= float (input (" Precio: "))
Product_4= float (input (" Precio: "))
Product_5= float (input (" Precio: "))

Total = Product_1 + Product_2 + Product_3 + Product_4 + Product_5

print ("Esto es lo que debe de pagar ", Total )

print (" Inserte el efectivo ")
Efectivo = int (input (" Efectivo "))

if Efectivo > Total:
    Cambio = Efectivo - Total
    #Esto hace que el resultado solo mede en 2 decimales
    Cambio = round (Cambio , 2)
    print ("Su cambio que le corresponde es de ", Cambio )
else: 
    print (" Efectivo faltante ")
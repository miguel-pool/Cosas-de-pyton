Total = 0
Pago = 0


#Cosas generales
print (" Veterinaria Don Lauro ")

Fecha= input(" Fecha: ")
print (" ---------------------------------------------------- ")
#Datos del dueño 
Nombre_del_dueño = input (" Nombre del dueño: ")
Numero_celular = input (" Telefono: ")
Correo_electronico = input (" Correo electronico: ")
print (" ---------------------------------------------------- ")


print (" ---------------------------------------------------- ")
#Datos de la maescota 
Nombre_de_la_mascota = input (" Nombre de la mascota: ")
print (" ¿Que especie es su mascota? ")
Especie = int (input ( "1.- Perro \n 2.- Gato \n 3.- Ave "))

Fecha_de_nacimiento = input (" Fecha de nacimiento: ")
Edad = input (" Edad de la mascota: ")
Vacunas = input (" ¿Que vacunas ya cuenta?: ")
print (" ---------------------------------------------------- ")



print (" ---------------------------------------------------- ")
#Menu de servicios 
Tipo = print (" Que es lo que requiere su mascota: ")
while True:
    
    print ( " 1.- Vacunas  \n 2.- Baño  \n 3.- Corte de Pelo \n 4.- Urgencia ")
    Op = int (input (" Seleccione cual servicio requiere: "))
    print (" ---------------------------------------------------- ")

    if Especie == 1:
        if Op == 1 :
            print (" ---------------------------------------------------- ")
            print (" Usted a seleccionado Vacunas ")
            print (" 1.1 -Rabia \n 2.2 - Parvovirus \n 3.3 - Parainfluenza \n 4.4 -Distemper ")
            Op2= input (" Seleccione la vacuna que su mascota: ")
            print (" ---------------------------------------------------- ")
        
        if Op2 == "1.1":
            print (" Usted escogio antirabica ")
            Total = Pago + 75
            print (" Su servicio sera de ", Total, " Pesos mexicano ")
            
        if Op2== "2.2" (" Usted escogio Parvovirus "):
            Total = Pago + 150
            print (" Su servicio sera de ", Total, " Pesos Mexicanos ")
        
            
        if Op2== "3.3" (" Usted escogio Parainfluenza "):
            Total = Pago + 150
            print (" Su servicio sera de ", Total, " Pesos Mexicanos ")
        
            
        if Op2== "4.4" (" Usted escogio Distemper "):
            Total = Pago + 200
            print (" Su servicio sera de ", Total, " Pesos Mexicanos ")
    
        if Op == 2 :
            print (" ---------------------------------------------------- ")
            print (" Usted a seleccionado baño ")
            Total = Pago + 250
            print (" Su servicio sera de ", Total, " Pesos Mexicanos ")
    
        if Op == 3 :
            print (" ---------------------------------------------------- ")
            print (" Usted a seleccionado Corte de Pelo ")
            Total = Pago + 150
            print (" Su servicio sera de ", Total, " Pesos Mexicanos ")
            print (" ---------------------------------------------------- ")
    
        if Op == 4 :
            print (" ---------------------------------------------------- ")
            print (" Usted a seleccionado Urgencia ")
            print (" Lleve a su mascota a la sucursal mas cercana ")
            print (" ---------------------------------------------------- ")
            
    if Especie == 2:
        
        Pago == 100
        
        if Op == 1 :
            print (" ---------------------------------------------------- ")
            print (" Usted a seleccionado Vacunas ")
            print (" 1.1 -Rabia \n 2.2 - Parvovirus \n 3.3 - Parainfluenza \n 4.4 -Distemper ")
            Op2= float (input (" Seleccione la vacuna que su mascota: "))
            print (" ---------------------------------------------------- ")
        
        if Op2 == 1.1:
            print (" Usted escogio antirabica ")
            Total = Pago + 75
            print (" Su servicio sera de ", Total, " Pesos mexicano ")
            
        if Op2== 2.2 (" Usted escogio Parvovirus "):
            Total = Pago + 150
            print (" Su servicio sera de ", Total, " Pesos Mexicanos ")
        
            
        if Op2== 3.3 (" Usted escogio Parainfluenza "):
            Total = Pago + 150
            print (" Su servicio sera de ", Total, " Pesos Mexicanos ")
        
            
        if Op2== 4.4 (" Usted escogio Distemper "):
            Total = Pago + 200
            print (" Su servicio sera de ", Total, " Pesos Mexicanos ")
    
        if Op == 2 :
            print (" ---------------------------------------------------- ")
            print (" Usted a seleccionado baño ")
            Total = Pago + 250
            print (" Su servicio sera de ", Total, " Pesos Mexicanos ")
    
        if Op == 3 :
            print (" ---------------------------------------------------- ")
            print (" Usted a seleccionado Corte de Pelo ")
            Total = Pago + 150
            print (" Su servicio sera de ", Total, " Pesos Mexicanos ")
            print (" ---------------------------------------------------- ")
    
        if Op == 4 :
            print (" ---------------------------------------------------- ")
            print (" Usted a seleccionado Urgencia ")
            print (" Lleve a su mascota a la sucursal mas cercana ")
            print (" ---------------------------------------------------- ")

nombre = ""
Opcion = ""
Destino = ""
Dinero = 0

print (" Seleccione a su personaje ")
print (" 1.- Infanteria \n 2.- Caballeria \n 3.- Artilleria ")
nombre = input (" Inserte su nombre: ")
Opcion = input (" Personaje: ")

#Personajes a elegir 
if Opcion == "1":
    Vida = 10
    Ataque = 5
    Escudo = 5
    Dinero = 20

if Opcion == "2":
    Vida = 15
    Ataque = 7
    Escudo = 10
    Dinero = 25

if Opcion == "3":
    Vida = 14
    Ataque = 15
    Escudo = 11
    Dinero = 20

#AVENTURA
print (" ------------------------------------------------------------ ")
print (f" Bienvenido a la travesia de tu vida {nombre}")
print (" ¿A donde quieres ir?")
print (" 1.-Taberna \n 2.-Practica de tiro \n 3.- Tienda  ")
Destino = input (" ¿A donde iras? ")
print (" ------------------------------------------------------------ ")

#TABERNA
if Destino == "1":
    print (" ------------------------------------------------------------ ")
    print (" Llegas a la taberna y te dice el dueño del lugar ")
    print (" Bienvenido aventurero ¿que desea? ")
    print (" 1.-Tarro de cerveza \n 2.-Baso de agua \n 3.-Plato de comida ")
    Opcion = input (" ¿Que deseas ordenar? ")
    
    if Opcion == "1":
        Vida = Vida + 2
        Ataque = Ataque - 2
        Escudo = Escudo - 1
        Dinero = Dinero - 5
        print (" Te quedan ", Dinero, " de oro en tu bolsa " )
    
    if Opcion == "2":
        Vida = Vida + 5
        Ataque = Ataque + 5
        Escudo = Escudo + 3
        print (" Te quedan ", Dinero, " de oro en tu bolsa " )
        
    if Opcion == "3":
        Vida = Vida + 5
        Ataque = Ataque + 4
        Escudo = Escudo + 2
        Dinero = Dinero - 5
        print (" Te quedan ", Dinero, " de oro en tu bolsa " )
    
    print (" ------------------------------------------------------------ ")
    print (" Te terminas lo que ordenaste ahora... ")   
    print (" ¿Que deseas hacer? ")
    print ("1.-Quedarte en la taberna \n 2.-Practica de tiro \n 3.- Tienda")
    Destino = input (" ¿A donde vamos? ")
    print (" ------------------------------------------------------------ ")
    
    #QUEDARSE EN LA TABERNA 
    if Destino == "1":
        
        print (" ------------------------------------------------------------ ")
        print (" Decides quedarte en la taberna para pasar el rato hasta que repente... ")
        print (" ???: Bartender deme lo de siempre ")
        print (" ¿Qué deseas hacer? ")
        print (" 1.- Interrogar al sujeto extraño \n 2.- Confrontarlo \n 3.- Retirarte de la taberna ")
        print (" ------------------------------------------------------------ ")
        
        #INTERROGAR AL SUJETO
        Opcion = input (" ¿Que haras? ")
        if Opcion == "1": 
            print (" ------------------------------------------------------------ ")
            print (" Decides interrogar al sujeto extraño sobre quien es el")
            print (" ???: ¿Quien soy? y ¿por que estoy aqui?")
            print (" Porque tendria que decirte eso *Bebe su cerveza* ")
            print (" ------------------------------------------------------------ ")
            print (" 1.-Exgir respuesta \n 2.- Retirarte ")
            Opcion == input (" Selccione su acción: ")
            
            #EXIGIR RESPUESTA
            if Opcion == "1":
                print (" ------------------------------------------------------------ ")
                print (" Procedes a decirle al sujeto extraño ")
                print (" MK: ¿Quien es usted? ")
                print (" ???: *Te mira con cara extrañada* y porque tengo que decirte algo como eso?")
                print (" MK: Es solo curiosidad, no quiero problemas ")
                print (" ???: En ese caso, te dire que ten mucho cuidado con esa curiosidad ")
                print (" Edgar: Mi nombre es Edgar, mucho gusto en concerte ¿Te puedo ayudar el algo?")
                print (" ------------------------------------------------------------ ")
                
                print (" 1.-Consejos en tu aventura \n 2.-Objeto misterioso \n 3.-Retirarte ")
                Opcion = input (" Selccione una opción: ")
                #CONSEJO DE AVENTURA
                if Opcion == "1":
                        print (" ------------------------------------------------------------ ")
                        print (" MK: Tiene algun consejo para mi aventura ")
                        print (" Edgar: Aparte de tener cuidado con la curiosidad ")
                        print (" Edgar: El camino no sera para nada facil, pero sabes veo un gran potencial en ti ")
                        print (" Edgar: Me caiste muy bien, te entregare esto ")
                        print (" Recibiste 4 bendajes, 15 de dinero ")
                        Dinero = Dinero + 15
                        print (" Gracias Edgar jamas olvidare esto", "Tu dinero ahora es ", Dinero, " *Procedes a retirarte* ")
                        print (" ------------------------------------------------------------ ")
                    
        #CONFRONTARLO
        if Opcion == "2":
            print (" ------------------------------------------------------------ ")
            print (" Decides confrontar al sujeto extraño *Te levantas de tu lugar y le dices con voz firme* ")
            print (F"{nombre}: ¿Cual es tu problema? ")
            print (" ???: ¿Asi?, *El vato se levanta y te empuja* ")
            print (" ------------------------------------------------------------ ")
            
            print (" Bienvenido al modo combate ")
            print (" El sujeto lanza el primero golpe ")
            
            #Primer ataque
            print (" ------------------------------------------------------------ ")
            print (" ¿Cual es el nombre de usuario  del creador de este juego en discord? ")
            print (" 1.-MKZ \n 2.-MK \n 3.- Miguelito ")
            Respuesta = input ( "Selecciona: ")
            print (" ------------------------------------------------------------ ")
            
            #OPCION 1
            if Respuesta == "1":
                Vida_del_sujeto = 15
                print (" ------------------------------------------------------------ ")
                print (" ¡ESQUIVASTE EL GOLPE! ")
                print (" 1.-Golpe basico \n 2.-Pistola de mano \n 3.- Descansar ")
                Opcion = input (" ¿Con que atacas? ")
                
                print (" ------------------------------------------------------------ ")
                #ATAQUE 2
                if Opcion == "1":
                    print (" Decides atacar al sujeto " )
                    Vida_del_sujeto = Vida_del_sujeto - Ataque
                    print (" Vida del sujeto ", Vida_del_sujeto)
                    
                if Opcion == "2":
                    print (" Decides atacar al sujeto " )
                    Vida_del_sujeto = Vida_del_sujeto - 5
                    print (" Vida del sujeto ", Vida_del_sujeto)
                
                if Opcion == "3":
                    print (" Decides saltar turno descansando ")
                    if Vida >= Vida:
                        Vida = Vida + 0
                    else:
                        Vida = Vida + 2
                
                print (" ------------------------------------------------------------ ")
                #Ataque 3
                print (" El sujeto decide golpearte nuevamente ")
                print (" ¿Que preferia MK?")
                print (" 1.- Ir a ver un partido de Pumas \n 2.-Ir a un GP de F1 \n 3.- Conocer a Checo y Chino Huerta ")
                Respuesta = input (" Escoge: ")
                print (" ------------------------------------------------------------ ")
                
                print (" ------------------------------------------------------------ ")
                if Respuesta == "1":
                    print (f"{nombre} a recibido un golpe" )
                    print (" Te ha quitado 5 puntos de salud ")
                    Vida = Vida - 5
                    print (" Te vida restante es de ", Vida )
                    
                    print (" ------------------------------------------------------------ ")
                    print (" 1.-Golpe basico \n 2.-Pistola de mano \n 3.- Descansar ")
                    Opcion = input (" ¿Con que atacas? ")
                    print (" ------------------------------------------------------------ ")
                
                    #Opciones de combate
                    if Opcion == "1":
                        print (" Decides atacar al sujeto " )
                        Vida_del_sujeto = Vida_del_sujeto - Ataque
                        print (" Vida del sujeto ", Vida_del_sujeto)
                        
                    
                    if Opcion == "2":
                        print (" Decides atacar al sujeto " )
                        Vida_del_sujeto = Vida_del_sujeto - 5
                        print (" Vida del sujeto ", Vida_del_sujeto)
                
                    if Opcion == "3":
                        print (" Decides saltar turno descansando ")
                        if Vida >= Vida:
                            Vida = Vida + 0
                        else:
                            Vida = Vida + 2
                        print (" Tu vida es de ", Vida)
                    
                print (" ------------------------------------------------------------ ")
                if Respuesta == "2":
                    print (f"{nombre} a recibido un golpe ")
                    print (" Te ha quitado 5 puntos de salud ")
                    Vida = Vida - 5
                    print (" Te vida restante es de ", Vida )
                    print (" 1.-Golpe basico \n 2.-Pistola de mano \n 3.- Descansar ")
                    Opcion = input (" ¿Con que atacas? ")
                    
                    #Opciones de combate
                    if Opcion == "1":
                        print (" Decides atacar al sujeto " )
                        Vida_del_sujeto = Vida_del_sujeto - Ataque
                        print (" Vida del sujeto ", Vida_del_sujeto)
                    
                    if Opcion == "2":
                        print (" Decides atacar al sujeto " )
                        Vida_del_sujeto = Vida_del_sujeto - 5
                        print (" Vida del sujeto ", Vida_del_sujeto)
                
                    if Opcion == "3":
                        print (" Decides saltar turno descansando ")
                        if Vida >= Vida:
                            Vida = Vida + 0
                        else:
                            Vida = Vida + 2
                        print (" Tu vida es de ", Vida)
                
                print (" ------------------------------------------------------------ ")
                if Respuesta =="3":
                    print (" Has esquivado el golpe nuevamente" )
                    print (" 1.-Golpe basico \n 2.-Pistola de mano \n 3.- Descansar ")
                    Opcion = input (" ¿Con que atacas? ")
                    
                    #Opciones de combate
                    if Opcion == "1":
                        print (" Decides atacar al sujeto " )
                        Vida_del_sujeto = Vida_del_sujeto - Ataque
                        print (" Vida del sujeto ", Vida_del_sujeto)
                    
                    if Opcion == "2":
                        print (" Decides atacar al sujeto " )
                        Vida_del_sujeto = Vida_del_sujeto - 5
                        print (" Vida del sujeto ", Vida_del_sujeto)
                
                    if Opcion == "3":
                        print (" Decides saltar turno descansando ")
                        if Vida >= Vida:
                            Vida = Vida + 0
                        else:
                            Vida = Vida + 2
                        print (" Tu vida es de ", Vida)
                print (" ------------------------------------------------------------ ")
                                        
            if Respuesta == "2":
                Vida_del_sujeto = 15
                print (" El sujeto acierta su golpe... ")
                Vida = Vida - 5
                print (" Te vida restante es de ", Vida )
                print (" ¿Con que atacas? ")
                
            if Respuesta == "3":
                Vida_del_sujeto = 15
                print (" El sujeto acierta su golpe... ")
                Vida = Vida - 5
                print (" Te vida restante es de ", Vida )
                print (" ¿Con que atacas? ")
                
        #RETIRARSE
        if Opcion == "3":
            print (" Decides retirarte de la taberna ante la negatividad del sujeto peroo... ")
            print (" ???: Mi nombre es Edgar y soy un guardia de rey solo vengo a relajarme un poco ")
            print (" John decide responder a tus interrogantes ")
            print ( "1.-Seguir con la platica \n 2.- Retirarte")

#PRACTICA DE TIRO    
            
if Destino == "2":
    
    print (" ------------------------------------------------------------ ")
    print (" Llegas a la zona de tiro ")
    print (" Te dice el dueño de la zona ")
    print (" Bienvenido practica todo lo que quieras ")
    
    Ataque = Ataque + 5
    Escudo = Escudo + 5 
    print (" ------------------------------------------------------------ ")
    
    print (" ------------------------------------------------------------ ")
    print (" ¿Terimnas de practicar y que deseas hacer? ")
    print ( "1.-Taberna \n 2.-Seguir practicando tiro \n 3.- Tienda" )
    Destino= input (" ¿A donde vamos? ") 
    print (" ------------------------------------------------------------ ")
    
    
#TIENDA
if Destino == "3":
    
    print (" ------------------------------------------------------------ ")
    print (" LLegas a la tienda y te dice el dueño del local ")
    print (" Dueño: Bienvenido a mi tienda, Aqui tenemos buenos precios, decide con calma ")
    print (" 1.- Carabina $10 \n 2.- Fusil de cerrojo $12 \n 3.- Bayoneta $8 \n 4.-Lanzallamas $25 \n 5.- Casco nivel 2 $15")
    Opcion = input (" ¿Que es lo que necesitas :)? ")
    print (" ------------------------------------------------------------ ")
    
    if Opcion == "1":
        Ataque = Ataque + 5
        Escudo = Escudo + 1
        Dinero = Dinero - 10
        print (" Te quedan ", Dinero, " de oro en tu bolsa " )
    
    if Opcion == "2":
        Ataque = Ataque + 10
        Escudo = Escudo - 3
        Dinero = Dinero - 12
        print (" Te quedan ", Dinero, " de oro en tu bolsa " )
        
    if Opcion == "3":
        Ataque = Ataque + 7
        Escudo = Escudo + 5
        Dinero = Dinero - 8
        print (" Te quedan ", Dinero, " de oro en tu bolsa " )
        
    if Opcion == "4":
        Ataque = Ataque + 20
        Escudo = Escudo - 5
        Dinero = Dinero - 25
        print (" Te quedan ", Dinero, " de oro en tu bolsa " )
        
    if Opcion == "5:":
        Escudo = Escudo + 10
        Dinero = Dinero - 15
        print (" Te quedan ", Dinero, " de oro en tu bolsa " )
        
print ( "¿Seria todo? ")
Opcion = input ("¿?")

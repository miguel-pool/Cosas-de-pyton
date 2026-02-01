Cadena1= "Hola soy Miguel"
Cadena2= "ME GUSTA LA F1"
Cadena3 = "no se que hacer"
Cadena4 = "583324"
Cadena5= "QuehayAmigoSoyMK"
Cadena6= "Racing Point F1"

#Convertidor a Mayusculas 
Mayusc = Cadena1.upper ()
print ("1.-", Mayusc)

#Convertidor a Minusculas
Minus = Cadena2.lower()
print ("2.-",Minus)

#Primer letra Mayuscula 
Primer_Mayus = Cadena3.capitalize()
print (Primer_Mayus)

#Buscamos una cadena en otra cadena, si no encuentra nada te devuelve -1 
Busqueda_cadena = Cadena1.find("M")
print (Busqueda_cadena)

#Busqueda en una cadena en otra cadena, si no encuentra nada te devuelve una excepcion
Busqueda_index = Cadena1.index("l")
print (Busqueda_index)

#Si es numerico devuelve true, si no devuelve false
es_numerico = Cadena4.isnumeric()
print (es_numerico)

#Si es un alfanumerico devuelve true, si no devuelve false, Los espacios en blanco ocasionan el false 
es_alfanumerico = Cadena5.isalpha()
print (es_alfanumerico)

#Solo cuenta las coincidencia en la cadena, Osea cuantas veces se repite cierto "dato" en la cadena.
contar_coincidencias = Cadena2.count("A")
print (contar_coincidencias)

#LEN= SIRVE PARA CONTAR LA CANTIDAD DE CARACTERES QUE TIENE UNA CADENA
contar_caracteres = len(Cadena1)
print(contar_caracteres)

#Verifica si una cadena empeiza con otra cadena dada, si es asi te devuelve True
empieza_con = Cadena1.startswith("Hola")
print(empieza_con)

#Verifica si una cadena termina con otra cadena dada, si es asi te devuelve True
termina_con = Cadena1.endswith("l")
print(termina_con)

#Remplaza el conetido si el valor es 1, si se encuentra en la cadena origianal,remplaza el valor 1 de la misma,por el valor 2
cadena_nueva=Cadena1.replace(" ",",")
cadena_nueva_2=cadena_nueva.upper()
print(cadena_nueva_2)

#SEPARAR CADENAS CON LA CADENA QUE LE DEMOS
cadena_separa=Cadena6.split(" ")
print(cadena_separa[2])
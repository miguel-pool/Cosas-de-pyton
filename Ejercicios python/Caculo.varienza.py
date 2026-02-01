op = 0
op2=0
n_total= 0
N_total=0
var_arriba = 0
var_abajo=0
total=0

print("Bienvenido a este programa que calcula la varianza")

while op != 1:
    print("Primero vamos a sacar la media")
    print("Inserte los valores")
    n1 = float(input("Numero:\n"))
    n_total= n_total+n1
    N_total=N_total+1
    print("Seria todo?")
    print("1.-Si\n2.-No")
    op=int(input("opcion:"))

med = n_total/N_total
print("La media de su problema es:",med)

while op2 !=1:
    print("Vuelva a insertar los numeros que puso")
    print("Inserte los valores")
    n2 = float(input("Numero:\n"))
    var_arriba = (n2-med)*(n2-med)
    total = total+var_arriba
    print("Seria todo?")
    print("1.-SI\n2.-NO")
    op2=int(input("Opcion:"))

var_total=total/N_total-1
print("La varianza de tu problema es:",var_total)
    
    



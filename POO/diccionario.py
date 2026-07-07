bodega = {
    "manzana": 10,
    "pera": 5,
    "Uva": 10,
    "naranjas": 30
}

print("Esto es lo que hay en la bodega: ",bodega)

bodega["manzana"] = 5
bodega["pera"] = 10
bodega["Uva"] = 20

print("Luego de la auditoria esto es lo que hay en la bodega: ",bodega)

del bodega["manzana"]

print("Luego de retirar el stock asi quedo la bodega: ",bodega)
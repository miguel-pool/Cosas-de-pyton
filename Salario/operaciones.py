def bruto(a, b):
    return a * b

def bono(a, b):
    return ((a* b) * 0.10) + (a * b)

def descuento(a, b):
    return (a*b) - ((a * b) *  0.08)

def neto(a, b):
    return (a * b) + ((a*b) * 0.10) - ((a*b)*0.08)
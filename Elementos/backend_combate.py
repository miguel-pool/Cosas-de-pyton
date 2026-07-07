def dano(ataque, defensa):
    ventajas = {
        "FUEGO": "PLANTA", 
        "AGUA": "FUEGO", 
        "PLANTA": "AGUA", 
        "ELECTRICO": "AGUA", 
        "TIERRA": "ELECTRICO"
    }
    
    # 1. Verificamos si el ataque está en nuestro diccionario 
    # Y verificamos si la defensa del rival es su debilidad exacta
    if ataque in ventajas and ventajas[ataque] == defensa:
        return "¡Es súper eficaz! (x2)"      
        
    # 2. Si son del mismo tipo
    elif ataque == defensa:
        return "No es muy eficaz... (x0.5)"
        
    # 3. Si no es ni ventaja directa ni el mismo tipo, es neutro
    else: 
        return "Daño neutro (x1)"
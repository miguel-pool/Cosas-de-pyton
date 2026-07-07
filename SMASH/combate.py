import random

# Ahora la función recibe los datos que el Front-End le manda
def generar_partida(jugador, personaje, modo, objetos):
    
    oponentes = ["Mario", "Lucas", "Ness", "Joker", "Steve","Checo","Fox"] 
    # GUARDAMOS la elección aleatoria en una variable
    oponente_random = random.choice(oponentes)
    
    escenarios = ["Destino Final", "Campo de Batalla", "Estadio Pokémon"]
    escenario_random = random.choice(escenarios)
    
    # Usamos f-string para inyectar las variables reales
    return f"¡NUEVA PARTIDA!\n\n{jugador} usará a {personaje}\nVS\n{oponente_random} en {escenario_random}.\n\nModo: {modo}\nObjetos: {objetos}"
import itertools

COLORES = ["azul", "rojo", "blanco", "negro", "verde", "purpura"]

def generar_combinaciones():
    return list(itertools.product(COLORES, repeat=4))

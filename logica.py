from colores import COLORES

def calcular_retroalimentacion(propuesta, objetivo):
    pos_correctas = sum([p == o for p, o in zip(propuesta, objetivo)])

    colores_propuesta = {color: propuesta.count(color) for color in COLORES}
    colores_objetivo = {color: objetivo.count(color) for color in COLORES}

    total_comunes = sum(min(colores_propuesta[c], colores_objetivo[c]) for c in COLORES)
    colores_correctos = total_comunes - pos_correctas

    return pos_correctas, colores_correctos

def filtrar_combinaciones(espacio, intento, retroalimentacion):
    return [
        comb for comb in espacio
        if calcular_retroalimentacion(comb, intento) == retroalimentacion
    ]

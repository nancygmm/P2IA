
import random
import matplotlib.pyplot as plt

COLORES = ["azul", "rojo", "blanco", "negro", "verde", "morado"]

def generar_combinaciones():
    from itertools import product
    return list(product(COLORES, repeat=4))

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

def simular_juegos(n=200, modo="automatico"):
    resultados = []
    total_intentos = 0

    for _ in range(n):
        secreta = random.choice(generar_combinaciones())
        espacio = generar_combinaciones()
        historial = [len(espacio)]
        intentos = 0

        while True:
            intento = random.choice(espacio)
            intentos += 1
            pos, col = calcular_retroalimentacion(intento, secreta)
            if pos == 4:
                break
            espacio = filtrar_combinaciones(espacio, intento, (pos, col))
            historial.append(len(espacio))
            if not espacio:
                break

        total_intentos += intentos
        resultados.append(historial)

    promedio_intentos = total_intentos / n
    return resultados, promedio_intentos

def promedio_por_paso(resultados):
    max_len = max(len(hist) for hist in resultados)
    suma = [0] * max_len
    conteo = [0] * max_len
    for hist in resultados:
        for i, val in enumerate(hist):
            suma[i] += val
            conteo[i] += 1
    return [s / c if c != 0 else 0 for s, c in zip(suma, conteo)]

def graficar_barras(promedios, promedio_intentos, titulo):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(promedios)), promedios)
    plt.title(f"{titulo}\nPromedio de intentos: {promedio_intentos:.2f}")
    plt.xlabel("Número de Intento")
    plt.ylabel("Tamaño promedio del espacio de búsqueda")
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    resultados_auto, prom_auto = simular_juegos(modo="automatico")
    promedio_auto = promedio_por_paso(resultados_auto)
    graficar_barras(promedio_auto, prom_auto, "Modo Automático (200 juegos)")

    resultados_real, prom_real = simular_juegos(modo="tiempo_real")  # misma lógica para simular tiempo real
    promedio_real = promedio_por_paso(resultados_real)
    graficar_barras(promedio_real, prom_real, "Modo Tiempo Real (200 juegos)")

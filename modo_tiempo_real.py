import random
from colores import generar_combinaciones
from logica import filtrar_combinaciones

def modo_tiempo_real():
    print("Modo Tiempo Real - Mastermind IA")
    espacio = generar_combinaciones()
    intentos = 0

    while True:
        intento = random.choice(espacio)
        intentos += 1
        print(f"\n Intento #{intentos}: {intento}")

        try:
            pos = int(input("¿Cuántas fichas están en la posición correcta? "))
            col = int(input("¿Cuántos colores correctos en posición incorrecta? "))
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")
            continue

        if pos == 4:
            print(f"\n ¡Combinación encontrada en {intentos} intentos!")
            break

        espacio = filtrar_combinaciones(espacio, intento, (pos, col))
        print(f" Combinaciones restantes: {len(espacio)}")

        if not espacio:
            print("No quedan combinaciones posibles. ¿Hubo un error en la retroalimentación?")
            break

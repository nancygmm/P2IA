import random
from colores import generar_combinaciones, COLORES
from logica import calcular_retroalimentacion, filtrar_combinaciones

def leer_combinacion_secreta():
    print("Introduce la combinación secreta de 4 colores (por ejemplo: rojo verde azul negro)")
    print(f"Colores válidos: {', '.join(COLORES)}")

    while True:
        entrada = input("→ Combinación: ").strip().lower()
        entrada = entrada.replace(",", " ").split()

        if len(entrada) != 4 or not all(color in COLORES for color in entrada):
            print("Combinación inválida. Intenta de nuevo.")
        else:
            return entrada

def modo_automatico():
    print("\nModo Automático - Mastermind IA")
    secreta = leer_combinacion_secreta()

    espacio = generar_combinaciones()
    historial_espacio = [len(espacio)]  
    intentos = 0

    while True:
        intento = random.choice(espacio)
        intentos += 1
        pos, col = calcular_retroalimentacion(intento, secreta)

        print(f"Intento #{intentos}: {intento} → Posiciones correctas: {pos}, Colores correctos: {col}")

        if pos == 4:
            print(f"\n¡Combinación encontrada en {intentos} intentos!")
            break

        espacio = filtrar_combinaciones(espacio, intento, (pos, col))
        historial_espacio.append(len(espacio))

        if not espacio:
            print("No quedan combinaciones posibles. ¿Hubo un error en la combinación secreta?")
            break

    print("\n Evolución del espacio de búsqueda:")
    for i, size in enumerate(historial_espacio):
        print(f"  Paso {i}: {size} combinaciones posibles")

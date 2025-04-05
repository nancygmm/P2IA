from modo_tiempo_real import modo_tiempo_real
from modo_automatico import modo_automatico

def main():
    print("Bienvenido a Mastermind con IA")
    print("1. Modo en Tiempo Real")
    print("2. Modo Automático")
    print("0. Salir")

    while True:
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            modo_tiempo_real()
        elif opcion == "2":
            modo_automatico()
        elif opcion == "0":
            print("Que tenga un buen día")
            break
        else:
            print("La opción no es válida, ingrese una opción")

if __name__ == "__main__":
    main()

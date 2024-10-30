from Temporizador import Temporizador

def main():
    print('Dentro de  main')
    TON_00 = Temporizador("Tiempo Bajo", 1)
    TON_01 = Temporizador("Tiempo Alto", 2)

    while True:
        TON_00.entrada = not TON_01.salida
        TON_00.actualizar()

        TON_01.entrada = TON_00.salida
        TON_01.actualizar()

        salida = TON_00.salida and not TON_01.salida

        print("Salida: ", salida)

if __name__ == "__main__":
    main()
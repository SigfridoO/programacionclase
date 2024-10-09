from Temporizador import Temporizador

class Semaforo:
    def __init__(self) -> None:
        print('Dentro de  semaforo')
        TON_00 = Temporizador("TON 0", 5)
        TON_01 = Temporizador("TON 1", 1)
        TON_02 = Temporizador("TON 2", 6)

        while True:
            TON_00.entrada = not TON_02.salida
            TON_00.actualizar()

            TON_01.entrada = TON_00.salida
            TON_01.actualizar()

            TON_02.entrada = TON_01.salida
            TON_02.actualizar()

            rojo = not TON_00.salida
            amarillo = TON_00.salida and not TON_01.salida
            verde = TON_01.salida

            print("Salida: ", rojo, amarillo, verde)

    def iniciar_semaforo(self):
        pass

def main():
    semaforo = Semaforo()

if __name__=="__main__":
    main()
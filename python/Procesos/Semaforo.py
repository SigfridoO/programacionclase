from Temporizador import Temporizador

import threading
import time

class Semaforo:
    def __init__(self) -> None:
        print('Dentro de  semaforo')
        self.TON_00 = Temporizador("TON 0", 5)
        self.TON_01 = Temporizador("TON 1", 1)
        self.TON_02 = Temporizador("TON 2", 6)
        self.intermediario = None
        
        self.tarea = threading.Thread(target=self.iniciar_semaforo)
        self.tarea.start()
        print ("Despues del constructor de semaforo")

    def iniciar_semaforo(self):
        print("Dentro de iniciar semaforro")
        while True:
            print("Dentro del while")
            self.TON_00.entrada = not self.TON_02.salida
            self.TON_00.actualizar()

            self.TON_01.entrada = self.TON_00.salida
            self.TON_01.actualizar()

            self.TON_02.entrada = self.TON_01.salida
            self.TON_02.actualizar()

            rojo = not self.TON_00.salida
            amarillo = self.TON_00.salida and not self.TON_01.salida
            verde = self.TON_01.salida

            if self.intermediario:
                self.intermediario.Y_00 = rojo
                self.intermediario.Y_01 = amarillo
                self.intermediario.Y_02 = verde

            print("Salida: ", rojo, amarillo, verde)
            time.sleep(0.001)



    def establecer_intermediario(self, intermediario):
        self.intermediario = intermediario

def main():
    semaforo = Semaforo()

if __name__=="__main__":
    main()
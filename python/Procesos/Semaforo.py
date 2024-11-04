from Temporizador import Temporizador

import threading
import time

class Semaforo:
    def __init__(self) -> None:
        print('Dentro de  semaforo')
        self.TON_00 = Temporizador("TON 0", 5)
        self.TON_01 = Temporizador("TON 1", 1)
        self.TON_02 = Temporizador("TON 2", 6)

        self.boton_00 = False
        self.boton_01 = False
        self.boton_virtual_00 = False

        self.funcionando = False
        self.intermediario = None
        self.worker = None        
        self.tarea = threading.Thread(target=self.iniciar_semaforo)
        self.tarea.start()
        print ("Despues del constructor de semaforo")

    def iniciar_semaforo(self):
        print("Dentro de iniciar semaforro")
        self.funcionando = True
        while self.funcionando:
            
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
                #Entradas
                self.boton_00 = self.intermediario.X_00
                self.boton_01 = self.intermediario.X_01

                #Salidas
                self.intermediario.Y_00 = rojo
                self.intermediario.Y_01 = amarillo
                self.intermediario.Y_02 = verde
            
            if self.worker:
                # Entradas
                self.worker.senal_botones(0, self.boton_00)
                self.worker.senal_botones(1, self.boton_01)

                # Salidas
                self.worker.senal_luz_roja(rojo)
                self.worker.senal_luz_amarilla(amarillo)
                self.worker.senal_luz_verde(verde)

            print("Salida: ", rojo, amarillo, verde, self.boton_00, self.boton_01, self.boton_virtual_00)
            time.sleep(0.001)

    def activar_boton_vitual(self, estado):
        self.boton_virtual_00 = estado
        if self.intermediario:
            self.intermediario.Y_03 = self.boton_virtual_00

    def establecer_intermediario(self, intermediario):
        self.intermediario = intermediario

    def establecer_worker(self, worker):
        self.worker = worker

    def detener(self):
        self.funcionando = False
        if self.tarea:
            self.tarea.join()

def main():
    semaforo = Semaforo()

if __name__=="__main__":
    main()
from PyQt6.QtWidgets import QApplication
import sys

from Semaforo import Semaforo
from Intermediario import Intermediario
from VentanaSemaforo import VentanaSemaforo
from MotorAPasos import MotorAPasos

class Inicio(VentanaSemaforo):
    def __init__(self):
        super().__init__()

        intermediario = Intermediario()

        intermediario.Y_08 = 1
        intermediario.Y_09 = 1
        intermediario.Y_11 = 1
        intermediario.Y_23 = 1

        self.establecer_electronica(intermediario)

        semaforo = Semaforo()
        semaforo.establecer_intermediario(intermediario)

        self.establecer_controlador(semaforo)
        semaforo.establecer_worker(self.obtener_worker())

        motorAPasos = MotorAPasos()
        motorAPasos.establecer_intermediario(intermediario)
        motorAPasos.z1_arranque = True
        motorAPasos.iniciar()


def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    inicio = Inicio()
    inicio.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
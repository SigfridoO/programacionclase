from PyQt6.QtWidgets import QApplication
import sys

from Semaforo import Semaforo
from Intermediario import Intermediario
from VentanaSemaforo import VentanaSemaforo

class Inicio(VentanaSemaforo):
    def __init__(self):
        super().__init__()
        semaforo = Semaforo()

        intermediario = Intermediario()
        semaforo.establecer_intermediario(intermediario)

        self.establecer_controlador(semaforo)
        semaforo.establecer_worker(self.obtener_worker())

def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    inicio = Inicio()
    inicio.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
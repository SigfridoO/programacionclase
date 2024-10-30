from PyQt6.QtWidgets import QApplication
import sys

from Semaforo import Semaforo
from Intermediario import Intermediario
from VentanaSemaforo import VentanaSemaforo

class Inicio(VentanaSemaforo):
    def __init__(self):
        super().__init__()
        print("Dentro de Inicio")
        intermediario = Intermediario()

        semaforo = Semaforo()
        semaforo.establecer_intermediario(intermediario)
        # semaforo.iniciar_semaforo()

def main():
    print("Dentro de main")
    app = QApplication(sys.argv)
    inicio = Inicio()
    inicio.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
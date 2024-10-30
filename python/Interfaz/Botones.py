__author__ = "Sigfrido"

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
import sys
from pathlib import Path

def abs_path(ruta:str):
    return str( Path(__file__).parent.absolute() / ruta)

class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Riego")
        boton = QPushButton("PRESIONAME")
        # boton.pressed.connect(self.boton_presionado)
        # boton.released.connect(self.boton_liberado)
        # boton.clicked.connect(self.boton_clickeado)

        boton.setCheckable(True)
        boton.clicked.connect(self.boton_alternado)

        self.setCentralWidget(boton)
        self.resize(300, 100)

    def boton_alternado(self, estado):
        print(estado)

        if estado:
            self.setWindowTitle("ON")
        else:
            self.setWindowTitle("OFF")
    # def boton_presionado(self):
    #     print("Botón presionado")

    # def boton_liberado(self):
    #     print("Se ha liberado el boton")

    # def boton_clickeado(self):
    #     print("Se ha clickleado el boton")


def main ():
    app = QApplication(sys.argv)
    ventana  = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
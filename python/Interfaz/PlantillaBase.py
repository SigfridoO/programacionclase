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
        boton.clicked.connect(self.boton_preisonado)

        self.setCentralWidget(boton)
        self.resize(300, 100)

    def boton_preisonado(self):
        print("Botón presionado")

def main ():
    app = QApplication(sys.argv)
    ventana  = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
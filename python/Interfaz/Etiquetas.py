__author__ = "Sigfrido"

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
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
        
        titulo = QLabel("Bienvenido")
        fuente = QFont('Manjari', 24)
        titulo.setFont(fuente)
        # titulo.setAlignment(Qt.AlignmentFlag.AlignHCenter \
        #                     | Qt.AlignmentFlag.AlignBottom )
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        imagen = QPixmap(abs_path("../imagenes/charizard.png"))
        titulo.setPixmap(imagen)
        titulo.setScaledContents(True)

        self.setCentralWidget(titulo)


        self.resize(300, 100)


def main ():
    app = QApplication(sys.argv)
    ventana  = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
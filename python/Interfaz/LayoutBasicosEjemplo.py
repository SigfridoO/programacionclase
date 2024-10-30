__author__ = "Sigfrido"

from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QLabel, QPushButton, QLineEdit, QWidget, \
    QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
import sys
from pathlib import Path

def abs_path(ruta:str):
    return str( Path(__file__).parent.absolute() / ruta)

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")


class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Riego")

        caja1 = Caja("red")
        caja2 = Caja("yellow")
        caja3 = Caja("green")
        caja4 = Caja("pink")

        mi_layout = QVBoxLayout()
        layout_inferior = QHBoxLayout()

        widget = QWidget()
        widget.setLayout(mi_layout)

        caja1.setFixedHeight(80)
        mi_layout.addWidget(caja1)
        mi_layout.addLayout(layout_inferior)

        boton_aceptar = QPushButton("Aceptar")
        boton_aceptar.setFixedSize(120, 30)
        layout_inferior.addWidget(boton_aceptar)
        layout_inferior.addWidget(caja3)
        layout_inferior.addWidget(caja4)


        self.setCentralWidget(widget)
        self.resize(300, 100)

def main ():
    app = QApplication(sys.argv)
    ventana  = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
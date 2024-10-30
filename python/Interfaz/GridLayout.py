__author__ = "Sigfrido"

from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QLabel, QPushButton, QLineEdit, QWidget, QSlider, QSpinBox, \
    QHBoxLayout, QVBoxLayout, QGridLayout
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
        self.setWindowTitle("Controles")

        self.rojo:int = 0
        self.verde:int = 0
        self.azul:int = 0

        caja1 = Caja("#0000FF")
        self.caja2 = Caja("#FF0000")
        controles = QWidget()
        # controles.setStyleSheet(f"background-color: #FFFFFF; \
        #                     border: 2px solid black")
        controles_layout = QGridLayout()
        controles.setLayout(controles_layout)

        mi_layout = QGridLayout()
        mi_layout.addWidget(caja1, 0, 0)
        mi_layout.addWidget(self.caja2, 1, 1, 2, 2)
        mi_layout.addWidget(controles, 1, 4, 3, 2)
        mi_layout.setColumnMinimumWidth(3, 20)
        mi_layout.setColumnStretch(0, 1)
        mi_layout.setColumnStretch(4, 2)
        
        # Modificando self.caja2
        self.caja2.setFixedSize(50, 50)

        # Modificando el layout_controles
        controles_layout.addWidget(QLabel("Rojo"), 0, 0)
        controles_layout.addWidget(QLabel("Verde"), 1, 0)
        controles_layout.addWidget(QLabel("Azul"), 2, 0)

        # Controles rojo
        self.slider_rojo = QSlider(Qt.Orientation.Horizontal)
        self.slider_rojo.setRange(0, 255)
        controles_layout.addWidget(self.slider_rojo, 0, 1)

        self.spinner_rojo = QSpinBox()
        self.spinner_rojo.setRange(0, 255)
        self.spinner_rojo.setFixedSize(80, 40)
        controles_layout.addWidget(self.spinner_rojo, 0, 2)

        # Controles verde
        self.slider_verde = QSlider(Qt.Orientation.Horizontal)
        self.slider_verde.setRange(0, 255)
        controles_layout.addWidget(self.slider_verde, 1, 1)

        self.spinner_verde = QSpinBox()
        self.spinner_verde.setRange(0, 255)
        self.spinner_verde.setFixedSize(80, 40)
        controles_layout.addWidget(self.spinner_verde, 1, 2)

        # Controles azul
        self.slider_azul = QSlider(Qt.Orientation.Horizontal)
        self.slider_azul.setRange(0, 255)
        controles_layout.addWidget(self.slider_azul, 2, 1)

        self.spinner_azul = QSpinBox()
        self.spinner_azul.setRange(0, 255)
        self.spinner_azul.setFixedSize(80, 40)
        controles_layout.addWidget(self.spinner_azul, 2, 2)

        widget = QWidget()
        widget.setLayout(mi_layout)
        self.setCentralWidget(widget)

        # listener
        self.slider_rojo.valueChanged.connect(self.establecer_rojo)
        self.spinner_rojo.valueChanged.connect(self.establecer_rojo)

        self.slider_verde.valueChanged.connect(self.establecer_verde)
        self.spinner_verde.valueChanged.connect(self.establecer_verde)

        self.slider_azul.valueChanged.connect(self.establecer_azul)
        self.spinner_azul.valueChanged.connect(self.establecer_azul)

        self.resize(400, 250)

    def establecer_rojo(self, valor):
        self.rojo = valor
        self.actualizar_controles()

    def establecer_verde(self, valor):
        self.verde = valor
        self.actualizar_controles()

    def establecer_azul(self, valor):
        self.azul = valor
        self.actualizar_controles()

    def actualizar_controles(self):
        self.slider_rojo.setValue(self.rojo)
        self.spinner_rojo.setValue(self.rojo)

        self.slider_verde.setValue(self.verde)
        self.spinner_verde.setValue(self.verde)

        self.slider_azul.setValue(self.azul)
        self.spinner_azul.setValue(self.azul)
        print(self.rojo, self.verde, self.azul)
        self.caja2.setStyleSheet(f"background-color: {self.obtener_hexadecimal()}")

    def obtener_hexadecimal(self):
        return f"#{self.rojo:02X}{self.verde:02X}{self.azul:02X}"
def main ():
    app = QApplication(sys.argv)
    ventana  = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
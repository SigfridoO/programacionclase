__author__ = "Sigfrido"

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, \
    QLineEdit
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
        self.campo_texto = QLineEdit()
        self.campo_texto.textChanged.connect(self.texto_cambiado)
        self.campo_texto.returnPressed.connect(self.enter_presionado)

        self.setCentralWidget(self.campo_texto)
        self.resize(300, 100)

    def enter_presionado(self):
        texto = self.campo_texto.text()
        self.setWindowTitle(texto)

    def texto_cambiado(self, texto:str):
        # print(texto)

        lista_de_palabras = texto.split(" ")
        for indice, palabra  in enumerate(lista_de_palabras):
            print(indice, palabra)

            if palabra == "rojo":
                self.campo_texto.setStyleSheet(f"background-color: red")
                break
            else:
                self.campo_texto.setStyleSheet(f"background-color: white")

def main ():
    app = QApplication(sys.argv)
    ventana  = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
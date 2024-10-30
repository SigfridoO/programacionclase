from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, \
    QWidget, QGridLayout, QVBoxLayout
from PyQt6.QtCore import Qt

import sys

class Caja (QLabel):
    def __init__(self, color:str):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")

class VentanaSemaforo(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        layout_externo = QGridLayout()
        widget.setLayout(layout_externo)

        ## agregando elementos principales
        caja1 = Caja("pink")
        caja2 = Caja("magenta")
        caja3 = Caja("brown")

        etiqueta_titulo = QLabel("Semaforo")
        etiqueta_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta_titulo.setFixedHeight(35)

        layout_externo.addWidget(etiqueta_titulo, 0,0,1, 2)
        layout_externo.addWidget(caja2, 1,0,1, 1)
        layout_externo.addWidget(caja3, 1,1,1, 1)

        layout_derecho = QVBoxLayout()
        caja3.setLayout(layout_derecho)

        # Elementos del layout derecho
        caja4 = self.crear_indicador("red")
        caja5 = self.crear_indicador("yellow")
        caja6 = self.crear_indicador("green")
        caja7 = Caja("gray")
        layout_derecho.addWidget(caja4)
        layout_derecho.addWidget(caja5)
        layout_derecho.addWidget(caja6)
        layout_derecho.addWidget(caja7)

        self.setCentralWidget(widget)
        self.resize(400, 250)
    
    def crear_indicador(self, color):
        caja =  QWidget()
        tamanio_circulo = 50
        caja.setFixedSize(tamanio_circulo, tamanio_circulo)
        caja.setStyleSheet(f"border: 1px solid black; \
                           background-color: {color}; \
                           border-radius: {tamanio_circulo/2}px; \
                           ")
        return caja
def main ():
    print("Dentro de main")
    app = QApplication(sys.argv)
    ventana = VentanaSemaforo()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
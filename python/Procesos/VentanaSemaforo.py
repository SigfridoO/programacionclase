from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, \
    QWidget, QGridLayout, QVBoxLayout
from PyQt6.QtCore import Qt, QRunnable, QThreadPool, pyqtSignal as Signal, QObject
from PyQt6.QtGui import QFontDatabase, QFont

import sys
from pathlib import Path

def abs_path(ruta:str):
    return str( Path(__file__).parent.absolute() / ruta)

class WorkerSignals(QObject):
    luz_roja = Signal(bool)
    luz_amarilla = Signal(bool)
    luz_verde = Signal(bool)

    def __init__(self):
        super().__init__()
        

class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        print ("Dentro de la clase  Worker")
        self.signals = WorkerSignals()

    def run(self):
        pass
        
    def senal_luz_roja(self, estado:bool = False):
        try:
            self.signals.luz_roja.emit(estado)
        except Exception as e:
            print(e)

        
    def senal_luz_amarilla(self, estado:bool = False):
        try:
            self.signals.luz_amarilla.emit(estado)
        except Exception as e:
            print(e)

        
    def senal_luz_verde(self, estado:bool = False):
        try:
            self.signals.luz_verde.emit(estado)
        except Exception as e:
            print(e)


class Caja (QLabel):
    def __init__(self, color:str):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")

class VentanaSemaforo(QMainWindow):
    def __init__(self):
        super().__init__()
        #print (abs_path("fonts/DynaPuf.ttf"))
        QFontDatabase.addApplicationFont(abs_path("fonts/DynaPuff.ttf"))

        widget = QWidget()
        layout_externo = QGridLayout()
        widget.setLayout(layout_externo)

        ## agregando elementos principales
        caja1 = Caja("pink")
        caja2 = Caja("magenta")
        caja3 = Caja("brown")

        etiqueta_titulo = QLabel("Semáforo")
        fuente = QFont("DynaPuff", 18)
        etiqueta_titulo.setFont(fuente)
        etiqueta_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta_titulo.setFixedHeight(35)

        layout_externo.addWidget(etiqueta_titulo, 0,0,1, 2)
        layout_externo.addWidget(caja2, 1,0,1, 1)
        layout_externo.addWidget(caja3, 1,1,1, 1)
        layout_externo.setColumnMinimumWidth(1, 75)
        layout_externo.setColumnStretch(0, 1)


        layout_derecho = QVBoxLayout()
        caja3.setLayout(layout_derecho)

        # Elementos del layout derecho
        self.indicador_rojo = self.crear_indicador("red", QWidget())
        self.indicador_amarillo = self.crear_indicador("yellow", QWidget())
        self.indicador_verde = self.crear_indicador("green", QWidget())
        caja7 = Caja("gray")
        layout_derecho.addWidget(self.indicador_rojo)
        layout_derecho.addWidget(self.indicador_amarillo)
        layout_derecho.addWidget(self.indicador_verde)
        layout_derecho.addWidget(caja7)

        # Elementos del lado izquierdo
        layout_vertical1 = QVBoxLayout()
        caja2.setLayout(layout_vertical1)
        grid_layout1 = QGridLayout()
        grid_layout2 = QGridLayout()
        layout_vertical1.addLayout(grid_layout1)
        layout_vertical1.addLayout(grid_layout2)

        # Elementos del grid_layout1
        caja_izq1 = Caja("cyan")
        caja_izq2 = Caja("orange")
        caja_izq3 = Caja("purple")
        etiqueta_botones = QLabel("Botones")
        etiqueta_botones.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid_layout1.addWidget(etiqueta_botones, 0, 0, 1, 3)        
        grid_layout1.addWidget(caja_izq1, 1, 0, 1, 1)        
        grid_layout1.addWidget(caja_izq2, 1, 1, 1, 1)        
        grid_layout1.addWidget(caja_izq3, 1, 2, 1, 1)     

        # Elementos de grid_layout2
        lista_de_cajas = []   
        for i in range(9):
            lista_de_cajas.append(Caja("white"))
        
        grid_layout2.addWidget(lista_de_cajas[0], 1,0)
        grid_layout2.addWidget(lista_de_cajas[1], 1,1)
        grid_layout2.addWidget(lista_de_cajas[2], 1,2)

        grid_layout2.addWidget(lista_de_cajas[3], 2,0)
        grid_layout2.addWidget(lista_de_cajas[4], 2,1)
        grid_layout2.addWidget(lista_de_cajas[5], 2,2)

        grid_layout2.addWidget(lista_de_cajas[6], 3,0)
        grid_layout2.addWidget(lista_de_cajas[7], 3,1)
        grid_layout2.addWidget(lista_de_cajas[8], 3,2)

        etiqueta_tempo = QLabel("Temporizadores")
        etiqueta_tempo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid_layout2.addWidget(etiqueta_tempo, 0,0,1, 3)

        self.setCentralWidget(widget)
        self.resize(400, 250)

        # Manejo de la clase worker
        self.threadpool = QThreadPool()
        self.worker = Worker()
        self.worker.signals.luz_roja.connect(self.cambiar_luz_roja)
        self.worker.signals.luz_amarilla.connect(self.cambiar_luz_amarilla)
        self.worker.signals.luz_verde.connect(self.cambiar_luz_verde)
        self.threadpool.start(self.worker)

        # Enlace con el control(semaforo)
        self.controlador = None

    def establecer_controlador(self, controlador):
        self.controlador = controlador

    def obtener_worker(self):
        return self.worker
    
    def cambiar_luz_roja(self, estado):
        if estado:
            color = "red"
        else:
            color= "gray"
        caja = self.crear_indicador(color, self.indicador_rojo)

    def cambiar_luz_amarilla(self, estado):
        if estado:
            color = "yellow"
        else:
            color= "gray"
        caja = self.crear_indicador(color, self.indicador_amarillo)

    def cambiar_luz_verde(self, estado):
        if estado:
            color = "green"
        else:
            color= "gray"
        caja = self.crear_indicador(color, self.indicador_verde)


    def crear_indicador(self, color, caja):
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
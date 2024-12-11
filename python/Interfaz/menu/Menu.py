from PyQt6.QtCore import Qt, QPropertyAnimation, QPoint, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, \
    QToolBar, QStatusBar, QDockWidget
from PyQt6.QtGui import QAction, QIcon
import sys

from MdiArea import MdiArea
from Utils import abs_path, Caja

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.construir_menu()
        self.construir_barra_herramientas()
        self.construir_docks()
        self.setStatusBar(QStatusBar())
        self.mdiarea = MdiArea()

        self.setCentralWidget(self.mdiarea)

        # Animación de la barra
        self.animacionSidebar = None


        self.setWindowTitle("Mi menú")
        self.resize(600, 375)


    def construir_docks(self):
        dock1 = QDockWidget()
        dock1.setWindowTitle("DOCK")

        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock1)

    def construir_barra_herramientas(self):
        herramientas = QToolBar('Barra de herramientas')
        self.addToolBar(herramientas)

        action_mostrar = QAction("Mostrar", self)
        icono_pokemon1 = QIcon(abs_path("icono_pokemon1.png"))
        action_mostrar.setIcon(icono_pokemon1)
        action_mostrar.triggered.connect(self.mostrar)
        herramientas.addAction(action_mostrar)

        action_ocultar = QAction("Ocultar", self)
        icono_pokemon2 = QIcon(abs_path("icono_pokemon2.png"))
        action_ocultar.setIcon(icono_pokemon2)
        action_ocultar.triggered.connect(self.ocultar)
        herramientas.addAction(action_ocultar)

    def mostrar(self):
        print("Dentro de mostrar")
        self.animacionSidebar = QPropertyAnimation(self.mdiarea.left_sidebar, b"pos")
        self.animacionSidebar.setDuration(300)
        self.animacionSidebar.setStartValue(QPoint(-self.mdiarea.left_sidebar.width(), 0))
        self.animacionSidebar.setEndValue(QPoint(0, 0))
        self.animacionSidebar.start()

    def ocultar(self):
        print("Dentro de ocultar")
        self.animacionSidebar = QPropertyAnimation(self.mdiarea.left_sidebar, b"pos")
        self.animacionSidebar.setDuration(150)
        self.animacionSidebar.setStartValue(QPoint(0, 0))
        self.animacionSidebar.setEndValue(QPoint(-self.mdiarea.left_sidebar.width(), 0))
        self.animacionSidebar.start()

    def construir_menu(self):
        menu = self.menuBar()
        menuArchivo = menu.addMenu("Archivo")

        icono_pokebola = QIcon(abs_path("icono_pokeball.png"))

        action_salir = QAction("Salir", self)
        action_salir.setIcon(icono_pokebola)
        action_salir.setShortcut("Ctrl+x")
        action_salir.triggered.connect(self.close)

        menuArchivo.addAction(action_salir)
        
        


        menuSimulacion = menu.addMenu("Simulación")


        menu_ayuda = menu.addMenu("Ayuda")
        action_informacion = QAction("Información", self)
        menu_ayuda.addAction(action_informacion)
        menu_ayuda.triggered.connect(self.mostrar_informacion)

    def mostrar_informacion(self):
        print("Mostrando información")
        # dialog = QMessageBox.information(self, "Información", "Esto es un texto informativo")
        # dialog = QMessageBox.critical(self, "Información", "Esto es un texto informativo")
        # dialog = QMessageBox.warning(self, "Información", "Esto es un texto informativo")
        # dialog = QMessageBox.about(self, "Información", "Esto es un texto informativo")
        dialog = QMessageBox.question(self, 
                "Información",
                "Esto es un texto informativo", 
                buttons=QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Cancel)
        

def main ():
    print ("Dentro de main")
    app  = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
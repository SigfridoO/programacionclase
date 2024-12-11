from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMdiSubWindow, QWidget

class ContenidoWidget(QWidget):
    def __init__(self) -> None:
        super(ContenidoWidget, self).__init__()

class Contenido(QMdiSubWindow):
    def __init__(self) -> None:
        super(Contenido, self).__init__()

        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.widget= ContenidoWidget()
        self.setWidget(self.widget)
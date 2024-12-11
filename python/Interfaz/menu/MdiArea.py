from PyQt6.QtWidgets import QMdiArea, QWidget, QMdiSubWindow, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui  import QResizeEvent

from Utils import Caja

class MdiArea(QMdiArea):
    def __init__(self) -> None:
        super(MdiArea, self).__init__()

        self.left_sidebar = LeftSidebar()
        self.addSubWindow(self.left_sidebar)
        

    def resizeEvent(self, resizeEvent:QResizeEvent):
        self.left_sidebar.resize(270, self.height())
# Para la ventanaIzquierda

class SidebarWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.setStyleSheet(f"background-color: red")
        layout.addWidget(Caja("green"))

class LeftSidebar(QMdiSubWindow):
    def __init__(self) -> None:
        super(LeftSidebar, self).__init__()

        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.widget = SidebarWidget()
        self.setWidget(self.widget)
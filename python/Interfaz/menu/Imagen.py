import cv2
import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import QObject, QThread, pyqtSignal as Signal, pyqtSlot as Slot, Qt
from PyQt6.QtGui import QImage, QPixmap

class VideoThread(QThread):

    enviar_pixmap_signal = Signal(np.ndarray)

    def  __init__(self ) -> None:
        super().__init__()
        self.camara_funcionando = False

    def run(self):
        print ("Dentro del método run")
        self.camara = cv2.VideoCapture(0)
        self.camara_funcionando = True
        while self.camara_funcionando:

            if not self.camara.isOpened():
                print("No se pudo encontrar la camara")
                return
            
            if self.camara.isOpened():
                width = self.camara.get(3)
                height = self.camara.get(4)
                fps = self.camara.get(5)

                print (width, height, fps)

            ret, frame = self.camara.read()
            if ret:
                self.enviar_pixmap_signal.emit(frame)
            # cv2.imshow("Prueba", frame)
    

class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camara")
        self.etiqueta = QLabel()
        self.etiqueta.setStyleSheet(f"background-color: red")

        self.setCentralWidget(self.etiqueta)
        self.resize(850, 650)

        self.video = VideoThread()
        self.video.enviar_pixmap_signal.connect(self.actualizar_imagen)
        self.video.start()
        #self.probar_camara()

    @Slot(np.ndarray)
    def actualizar_imagen(self, frame):
        # self.frame  = frame
        qt_img = self.convetir_qt(frame)
        
        self.etiqueta.setPixmap(qt_img)

    def probar_camara(self):
        camara = cv2.VideoCapture(0)


        while True:
            ret, frame = camara.read()
            cv2.imshow("Prueba", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    def convetir_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch* w
        convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        p = convert_to_qt_format.scaled(640, 480, Qt.AspectRatioMode.KeepAspectRatio)
        return QPixmap.fromImage(p)
def main():

    app =QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()

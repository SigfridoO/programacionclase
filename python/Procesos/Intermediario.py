import gpiod
from gpiod.line import Direction, Value

import threading
import time

class Intermediario:
    def __init__(self):
        print("Iniciando el control de la electrónica")
        self.DI_00 = None
        self.DI_01 = None

        self.DO_00 = None
        self.DO_01 = None
        self.DO_02 = None

        # definiendo las variables
        self.X_00 = False
        self.X_01 = False
        
        self.Y_00 = False
        self.Y_01 = False
        self.Y_02 = False

        self.configurar_senales()

    def configurar_senales(self):
        print('Configurando las señales de los pines')
        # Definiendo los pines
        self.DI_00 = 18
        self.DI_01 = 23

        self.DO_00 = 4
        self.DO_01 = 17
        self.DO_02 = 27

        self.chip = gpiod.request_lines(
            "/dev/gpiochip4",
            consumer="intermediario",
            config={
                # entradas
                self.DI_00: gpiod.LineSettings(direction=Direction.INPUT),
                self.DI_01: gpiod.LineSettings(direction=Direction.INPUT),
                
                # salidas
                self.DO_00: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_01: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_02: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
            },
        )
        tarea = threading.Thread(target=self.iniciar)
        tarea.start()

    def iniciar(self):
        self.funcionando_pines = True
        while self.funcionando_pines:
            self.X_00 = True if self.chip.get_value(self.DI_00) == Value.ACTIVE else False
            self.X_01 = True if self.chip.get_value(self.DI_01) == Value.ACTIVE else False
        
        
            self.chip.set_value(self.DO_00, Value.ACTIVE if self.Y_00 == True else Value.INACTIVE)
            self.chip.set_value(self.DO_01, Value.ACTIVE if self.Y_01 == True else Value.INACTIVE)
            self.chip.set_value(self.DO_02, Value.ACTIVE if self.Y_02 == True else Value.INACTIVE)

            # print(self.X_00)
            time.sleep(0.001)

def main():
    intermediario = Intermediario()
    intermediario.Y_00 = True

if __name__ == "__main__":
    main()
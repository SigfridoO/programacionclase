import gpiod
from gpiod.line import Direction, Value

import threading
import time

class Intermediario:
    def __init__(self):
        print("Iniciando el control de la electrónica")
        # Definiendo los pines
        self.DI_00 = 18
        self.DI_01 = 23
        self.DI_02 = 24
        self.DI_03 = 25

        self.DO_00 = 4
        self.DO_01 = 17
        self.DO_02 = 27
        self.DO_03 = 22

        self.DO_04 = 10
        self.DO_05 = 9
        self.DO_06 = 11
        self.DO_07 = 0

        # definiendo las variables
        # Entradas digitales
        self.X_00 = False
        self.X_01 = False
        self.X_02 = False
        self.X_03 = False
        
        # Saidas Digitales
        self.Y_00 = False
        self.Y_01 = False
        self.Y_02 = False
        self.Y_03 = False

        self.Y_04 = False
        self.Y_05 = False
        self.Y_06 = False
        self.Y_07 = False

        self.funcionando_pines = False
        self.configurar_senales()

    def configurar_senales(self):
        print('Configurando las señales de los pines')

        self.chip = gpiod.request_lines(
            "/dev/gpiochip4",
            consumer="intermediario",
            config={
                # entradas
                self.DI_00: gpiod.LineSettings(direction=Direction.INPUT),
                self.DI_01: gpiod.LineSettings(direction=Direction.INPUT),
                self.DI_02: gpiod.LineSettings(direction=Direction.INPUT),
                self.DI_03: gpiod.LineSettings(direction=Direction.INPUT),
                
                # salidas
                self.DO_00: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_01: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_02: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_03: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),

                self.DO_04: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_05: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_06: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_07: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
            },
        )
        self.tarea = threading.Thread(target=self.iniciar)
        self.tarea.start()

    def iniciar(self):
        self.funcionando_pines = True
        while self.funcionando_pines:
            self.X_00 = True if self.chip.get_value(self.DI_00) == Value.ACTIVE else False
            self.X_01 = True if self.chip.get_value(self.DI_01) == Value.ACTIVE else False
            self.X_02 = True if self.chip.get_value(self.DI_02) == Value.ACTIVE else False
            self.X_03 = True if self.chip.get_value(self.DI_03) == Value.ACTIVE else False
        
            self.chip.set_value(self.DO_00, Value.ACTIVE if self.Y_00 == True else Value.INACTIVE)
            self.chip.set_value(self.DO_01, Value.ACTIVE if self.Y_01 == True else Value.INACTIVE)
            self.chip.set_value(self.DO_02, Value.ACTIVE if self.Y_02 == True else Value.INACTIVE)
            self.chip.set_value(self.DO_03, Value.ACTIVE if self.Y_03 == True else Value.INACTIVE)

            self.chip.set_value(self.DO_04, Value.ACTIVE if self.Y_04 == True else Value.INACTIVE)
            self.chip.set_value(self.DO_05, Value.ACTIVE if self.Y_05 == True else Value.INACTIVE)
            self.chip.set_value(self.DO_06, Value.ACTIVE if self.Y_06 == True else Value.INACTIVE)
            self.chip.set_value(self.DO_07, Value.ACTIVE if self.Y_07 == True else Value.INACTIVE)
            # print(self.X_00)
            time.sleep(0.001)
    
    def detener(self):
        self.funcionando_pines = False
        if self.tarea:
            self.tarea.join()

def main():
    intermediario = Intermediario()
    intermediario.Y_00 = True

if __name__ == "__main__":
    main()
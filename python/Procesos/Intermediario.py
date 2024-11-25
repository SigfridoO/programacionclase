import gpiod
from gpiod.line import Direction, Value

import threading
import time

from RegistroDeCorrimiento import RegistroDeCorrimiento

class Intermediario:
    def __init__(self):
        print("Iniciando el control de la electrónica")
        # Definiendo los pines (Físicos)
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

        self.registro = RegistroDeCorrimiento()
        self.registro.establecer_callback(self.escribir_senales_registro)

        self.REG_CLK = 5  # CLK
        self.REG_LATCH = 6  # Latch
        self.REG_DS = 19  # DATA serie

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

        self.Y_08 = False
        self.Y_09 = False
        self.Y_10 = False
        self.Y_11 = False

        self.Y_12 = False
        self.Y_13 = False
        self.Y_14 = False
        self.Y_15 = False

        self.Y_16 = False
        self.Y_17 = False
        self.Y_18 = False
        self.Y_19 = False

        self.Y_20 = False
        self.Y_21 = False
        self.Y_22 = False
        self.Y_23 = False


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

                self.REG_CLK: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
                self.REG_LATCH: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
                self.REG_DS: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
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

            senales_registro = [self.Y_08,self.Y_09,self.Y_10,self.Y_11, self.Y_12,self.Y_13,self.Y_14,self.Y_15, self.Y_16,self.Y_17,self.Y_18,self.Y_19, self.Y_20,self.Y_21,self.Y_22,self.Y_23]
            self.registro.escribir_salidas(senales_registro)
            time.sleep(0.001)
    
    def escribir_senales_registro(self, senal, clk, latch):
            self.chip.set_value(self.REG_DS, Value.ACTIVE if senal == True else Value.INACTIVE)
            self.chip.set_value(self.REG_CLK, Value.ACTIVE if clk == True else Value.INACTIVE)
            self.chip.set_value(self.REG_LATCH, Value.ACTIVE if latch == True else Value.INACTIVE)
        

    def detener(self):
        self.funcionando_pines = False
        if self.tarea:
            self.tarea.join()

def main():
    intermediario = Intermediario()
    intermediario.Y_00 = True

if __name__ == "__main__":
    main()
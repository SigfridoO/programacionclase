import platform
import threading
import time

sistema = platform.system()
plataforma = platform.uname()

#print("sistema:", sistema)
#print("plataforma", plataforma)

if sistema == "Windows":
    print("Estamos en windows")
elif sistema == "Linux":
    print("Estamos en linux")
    if plataforma.node == "raspberrypi":
        print("Es una rapsberry")
        import gpiod

class Controladora:
    def __init__(self):
        print ('Dentro del constructor de controladora')
        #Variables internas
        self.DI_OO = None
        self.DI_O1 = None

        self.DO_OO = None
        self.DO_O1 = None
        self.DO_O2 = None

        self.DO_O3 = None
        self.DO_O4 = None
        self.DO_O5 = None
        self.DO_O6 = None

        self.DO_O7 = None
        self.DO_O8 = None
        self.DO_O9 = None
        self.DO_10 = None

        self.REG_CLK = None
        self.REG_LATCH = None
        self.REG_DS = None

        # Variables externas
        self.X_00 = False
        self.X_01 = False

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

        # Salidas virtuales al Registro de corrimiento
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
        self.Y_24 = False
        self.Y_25 = False
        self.Y_26 = False


        self.estado = False
        
        if plataforma.node == "raspberrypi":
            self.configurarSenales()

            self.tarea = threading.Thread(target=self.run)
            self.tarea.start()

    def configurarSenales(self):

        DI_00 = 23
        DI_01 = 24
        DI_02 = 25
        DI_03 = 8

        # Leds
        DO_00 = 4
        DO_01 = 17
        DO_02 = 27

        # Motor a pasos
        DO_03 = 22
        DO_04 = 10
        DO_05 = 9
        DO_06 = 11

        # PWM
        DO_07 = 12
        DO_08 = 13
        DO_09 = 18
        DO_10 = 19

        # Leds
        REG_CLK = 0  # CLK
        REG_LATCH = 5  # Latch
        REG_DS = 6  # DATA serie

        chip = gpiod.Chip('gpiochip4')

        self.DI_00 = chip.get_line(DI_00)
        self.DI_01 = chip.get_line(DI_01)
        self.DI_02 = chip.get_line(DI_02)
        self.DI_03 = chip.get_line(DI_03)

        self.DI_00.request(consumer="DI_00", type=gpiod.LINE_REQ_DIR_IN)
        self.DI_01.request(consumer="DI_01", type=gpiod.LINE_REQ_DIR_IN)
        self.DI_02.request(consumer="DI_02", type=gpiod.LINE_REQ_DIR_IN)
        self.DI_03.request(consumer="DI_03", type=gpiod.LINE_REQ_DIR_IN)

        # -------------
        self.DO_00 = chip.get_line(DO_00)
        self.DO_01 = chip.get_line(DO_01)
        self.DO_02 = chip.get_line(DO_02)

        self.DO_03 = chip.get_line(DO_03)
        self.DO_04 = chip.get_line(DO_04)
        self.DO_05 = chip.get_line(DO_05)
        self.DO_06 = chip.get_line(DO_06)

        self.DO_07 = chip.get_line(DO_07)
        self.DO_08 = chip.get_line(DO_08)
        self.DO_09 = chip.get_line(DO_09)
        self.DO_10 = chip.get_line(DO_10)

        self.REG_CLK = chip.get_line(REG_CLK)
        self.REG_LATCH = chip.get_line(REG_LATCH)
        self.REG_DS = chip.get_line(REG_DS)

        self.DO_00.request(consumer="DO_00", type=gpiod.LINE_REQ_DIR_OUT)
        self.DO_01.request(consumer="DO_01", type=gpiod.LINE_REQ_DIR_OUT)
        self.DO_02.request(consumer="DO_02", type=gpiod.LINE_REQ_DIR_OUT)

        self.DO_03.request(consumer="DO_03", type=gpiod.LINE_REQ_DIR_OUT)
        self.DO_04.request(consumer="DO_04", type=gpiod.LINE_REQ_DIR_OUT)
        self.DO_05.request(consumer="DO_05", type=gpiod.LINE_REQ_DIR_OUT)
        self.DO_06.request(consumer="DO_06", type=gpiod.LINE_REQ_DIR_OUT)

        self.DO_07.request(consumer="DO_07", type=gpiod.LINE_REQ_DIR_OUT)
        self.DO_08.request(consumer="DO_08", type=gpiod.LINE_REQ_DIR_OUT)
        self.DO_09.request(consumer="DO_09", type=gpiod.LINE_REQ_DIR_OUT)
        self.DO_10.request(consumer="DO_10", type=gpiod.LINE_REQ_DIR_OUT)

        self.REG_CLK.request(consumer="REG_CLK", type=gpiod.LINE_REQ_DIR_OUT)
        self.REG_LATCH.request(consumer="REG_LATCH", type=gpiod.LINE_REQ_DIR_OUT)
        self.REG_DS.request(consumer="REG_DS", type=gpiod.LINE_REQ_DIR_OUT)

    def run(self):
        self.estado = True
        while self.estado:
            self.leerYEscribirPines()
            # pass



    def leerYEscribirPines(self):
        self.X_00 = self.DI_00.get_value()
        self.X_01 = self.DI_01.get_value()
        self.X_02 = self.DI_02.get_value()
        self.X_03 = self.DI_03.get_value()

        self.DO_00.set_value(self.Y_00)
        self.DO_01.set_value(self.Y_01)
        self.DO_02.set_value(self.Y_02)
        # self.DO_03.set_value(self.Y_03)
        # self.DO_04.set_value(self.Y_04)
        # self.DO_05.set_value(self.Y_05)
        # self.DO_06.set_value(self.Y_06)

    def escribirPines2(self, salida_00, salida_01, salida_02, salida_03):
        self.DO_03.set_value(salida_00)
        self.DO_04.set_value(salida_01)
        self.DO_05.set_value(salida_02)
        self.DO_06.set_value(salida_03)

    def escribirPines3(self, salida_00, salida_01, salida_02, salida_03):
        self.DO_07.set_value(salida_00)
        self.DO_08.set_value(salida_01)
        self.DO_09.set_value(salida_02)
        self.DO_10.set_value(salida_03)

    def escribirPines4(self, salida_00, salida_01, salida_02):
        print('Dentro de pines 4')
        self.REG_DS.set_value(salida_00)
        self.REG_CLK.set_value(salida_01)
        self.REG_LATCH.set_value(salida_02)



def main():
    print ('Iniciando')
    controladora = Controladora()
    controladora.Y_00 = False
    controladora.Y_01 = False
    controladora.Y_02 = True


if __name__== '__main__':
    main()
import time

class RegistroDeCorrimiento:
    TIEMPO = 1

    def __init__(self) -> None:
        self.latch = False
        self.clk = False
        self.senal = False
        self.callback:None

    def escribir_salidas(self, senales:list=list()):
        # print("las señales recibidas son: ", senales)
        for i, n in enumerate(senales):
            # print(i, n)
            self.clk = 0
            self.senal = n
            self.latch = 0
            self.escribir()
            time.sleep(self.TIEMPO)
            self.clk = 1
            self.escribir()
            time.sleep(self.TIEMPO)

        self.latch = 1
        self.escribir()
        time.sleep(self.TIEMPO)
        self.latch = 0
        self.escribir()
        time.sleep(self.TIEMPO)

    def establecer_callback(self, callback):
        self.callback = callback

    def escribir(self):
        print(self.senal, self.clk, self.latch)
        if self.callback:
            self.callback(self.senal, self.clk, self.latch)

def main():
    registro = RegistroDeCorrimiento()
    registro.escribir_salidas([0,1,0,1, 1 ,1, 1, 0])

if __name__=="__main__":
    main()
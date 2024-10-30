import time
class Temporizador():
    def __init__(self, nombre:str, tiempo:float, descripcion:str=""):
        self.nombre = nombre
        self.descripcion = descripcion

        self.entrada = False
        self.salida = False
        self.reset = False

        self.tiempo = tiempo
        self.tiempoActual = 0

        self.bandera = False
        self.tiempo_Aux1 = 0
        self.tiempo_Aux2 = 0

    def actualizar(self):
        if self.entrada:
            if self.reset:
                self.salida = False
                self.bandera = False
                self.reset = False

            if not self.bandera:
                self.bandera = True
                self.tiempo_Aux1 = time.time()

            self.tiempo_Aux2 = time.time()
            self.tiempoActual = self.tiempo_Aux2 - self.tiempo_Aux1

            if self.tiempoActual > self.tiempo:
                self.salida = True
        else:
            self.salida = False
            self.bandera = False
    def __str__(self):
        return "%s->%s    %f %s %f %s" % (
        self.nombre, self.descripcion, self.tiempo, self.entrada, self.tiempoActual, self.salida)
    
def main():
    print('Dentro de  main')
    TON_01 = Temporizador("Temporizador de prueba", 5)

    while True:
        TON_01.entrada = True
        TON_01.actualizar()
        print(f"TON_1: {TON_01.entrada}  {TON_01.tiempo}  {TON_01.tiempoActual} {TON_01.salida}")

if __name__ == "__main__":
    main()
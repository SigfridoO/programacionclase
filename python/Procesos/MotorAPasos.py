__author__ = "Sigfrido"
__date__ = "6_nov_2024 08:06:00"

import threading
import time
from Temporizador import Temporizador
from enum import Enum
from blessed import Terminal

term = Terminal()

class estados_motor (Enum):
    home = 0
    estado_1 = 1
    estado_2 = 2
    estado_3 = 3
    estado_4 = 4
    estado_5 = 5
    estado_6 = 6
    estado_7 = 7
    estado_8 = 8

class MotorAPasos:
    def __init__(self):
        self.bobina_A:bool = False
        self.bobina_B:bool = False
        self.bobina_C:bool = False
        self.bobina_D:bool = False

        self.cuenta:int = 0
        self.estado_actual = estados_motor.home
        self.z0_direccion = False
        self.z1_arranque = False

        self.TON_00 = Temporizador(nombre="Tiempo de activación", tiempo=0.05)
        self.funcionando = False
        self.intermediario = None

        self.tarea = threading.Thread(target=self.control_secuencia)
        print(f"{self} Déspues del constructor de MotorAPasos")
        
    def control_secuencia(self):
        print("Dentro de control de secuencia")
        self.funcionando = True 
        while self.funcionando:

            self.TON_00.entrada = not self.TON_00.salida
            self.TON_00.actualizar()
            if self.TON_00.salida:
                # print(f"Se genero un pulso la cuenta es {self.cuenta}")
                self.cuenta += 1

                estado = self.estado_actual

                match estado:
                    case estados_motor.home:
                        self.actualizar_bobinas(False, False, False, False)

                        if self.z1_arranque:
                            self.estado_actual = estados_motor.estado_1
                        else:
                            self.estado_actual = estados_motor.home
                        
                    case estados_motor.estado_1:
                        self.actualizar_bobinas(True, False, False, False)

                        if self.z1_arranque:
                            if self.z0_direccion:
                                self.estado_actual = estados_motor.estado_2
                            else:
                                self.estado_actual = estados_motor.estado_8
                        else:
                            self.estado_actual = estados_motor.home
                                                        
                       
                    case estados_motor.estado_2:
                        self.actualizar_bobinas(True, True, False, False)

                        if self.z1_arranque:
                            if self.z0_direccion:
                                self.estado_actual = estados_motor.estado_3
                            else:
                                self.estado_actual = estados_motor.estado_1
                        else:
                            self.estado_actual = estados_motor.home
                            

                    case estados_motor.estado_3:
                        self.actualizar_bobinas(False, True, False, False)

                        if self.z1_arranque:
                            if self.z0_direccion:
                                self.estado_actual = estados_motor.estado_4
                            else:
                                self.estado_actual = estados_motor.estado_2
                        else:
                            self.estado_actual = estados_motor.home
                            
                    
                    case estados_motor.estado_4:
                        self.actualizar_bobinas(False, True, True, False)

                        if self.z1_arranque:
                            if self.z0_direccion:
                                self.estado_actual = estados_motor.estado_5
                            else:
                                self.estado_actual = estados_motor.estado_3
                        else:
                            self.estado_actual = estados_motor.home
                            

                    case estados_motor.estado_5:
                        self.actualizar_bobinas(False, False, True, False)
                        if self.z1_arranque:
                            if self.z0_direccion:
                                self.estado_actual = estados_motor.estado_6
                            else:
                                self.estado_actual = estados_motor.estado_4
                        else:
                            self.estado_actual = estados_motor.home

                    case estados_motor.estado_6:
                        self.actualizar_bobinas(False, False, True, True)

                        if self.z1_arranque:
                            if self.z0_direccion:
                                self.estado_actual = estados_motor.estado_7
                            else:
                                self.estado_actual = estados_motor.estado_5
                        else:
                            self.estado_actual = estados_motor.home


                    case estados_motor.estado_7:
                        self.actualizar_bobinas(False, False, False, True)

                        if self.z1_arranque:
                            if self.z0_direccion:
                                self.estado_actual = estados_motor.estado_8
                            else:
                                self.estado_actual = estados_motor.estado_6
                        else:
                            self.estado_actual = estados_motor.home


                    case estados_motor.estado_8:
                        self.actualizar_bobinas(True, False, False, True)

                        if self.z1_arranque:
                            if self.z0_direccion:
                                self.estado_actual = estados_motor.estado_1
                            else:
                                self.estado_actual = estados_motor.estado_7
                        else:
                            self.estado_actual = estados_motor.home

                # print(f"{self}estado_actual: {self.estado_actual} {self.z1_arranque} {self.z0_direccion} {term.bold_turquoise3} {self.bobina_A} {self.bobina_B} {self.bobina_C} {self.bobina_D} {term.normal}")

                if self.intermediario:
                    #Entradas
                    self.z0_direccion = self.intermediario.X_00

                    #Salidas
                    self.intermediario.Y_04 = self.bobina_A
                    self.intermediario.Y_05 = self.bobina_B
                    self.intermediario.Y_06 = self.bobina_C
                    self.intermediario.Y_07 = self.bobina_D
                time.sleep(0.001) 

    def actualizar_bobinas(self, a, b, c, d):
        self.bobina_A = a
        self.bobina_B = b
        self.bobina_C = c
        self.bobina_D = d
        
    def iniciar(self):
        self.tarea.start()

    def establecer_intermediario(self, intermediario):
        self.intermediario = intermediario

    def __str__(self) -> str:
        return f"{term.bold_orange} motor: {term.normal}".ljust(10)

class PruebaMotor:
    def __init__(self):
        self.TON_00 = Temporizador("Tiempo base", 8)
        self.TON_01 = Temporizador("Tiempo de 1s", 1)
        self.funcionando_prueba = False
        self.contador = 0
        self.motor: MotorAPasos = None
        self.tarea = threading.Thread(target=self.run_prueba)

    def run_prueba(self):
        self.funcionando_prueba = True
        while self.funcionando_prueba:
            self.TON_00.entrada = True
            self.TON_00.actualizar()

            if self.TON_00.salida:
                # print(f"{self} contador {self.contador}")
                if self.motor and self.contador < 20:
                    self.motor.z1_arranque=True
                else: 
                    self.motor.z1_arranque=False

            self.TON_01.entrada = not self.TON_01.salida
            self.TON_01.actualizar()
            if self.TON_01.salida:
                self.contador += 1


            time.sleep(0.001)

    def establecer_motor(self, motor):
        self.motor = motor

    def iniciar_prueba(self):
        self.tarea.start()

    def __str__(self) -> str:
        return "prueba:".ljust(10)

def main ():
    print("Dentro main")
    motorAPasos = MotorAPasos()
    motorAPasos.iniciar()

    pruebaMotor = PruebaMotor()
    pruebaMotor.establecer_motor(motorAPasos)
    pruebaMotor.iniciar_prueba()

if __name__==  "__main__":
    main()

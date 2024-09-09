

class Alumno:
    def __init__(self):

        self.nombre = "Sin definir"
        self.apellido = "Sin definir"


    def __str__(self):
        return self.nombre + " "  + self.apellido

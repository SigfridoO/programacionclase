class Padre():
    def __init__(self):
        print ('Hola soy padre')

    def trabajar(self):
        print('Hola estoy trabajando')

class Madre():
    def __init__(self):
        print('Hola soy Madre')
    
    def cocinar(self):
        print('Hola estoy cocinando')

class Hijo(Padre, Madre):
    def __init__(self):
        #super().__init__()
        Padre.__init__(self)
        Madre.__init__(self)
        print("Hola soy hijo")

def main ():
    hijo = Hijo()
    hijo.trabajar()

if __name__ == "__main__":
    main()
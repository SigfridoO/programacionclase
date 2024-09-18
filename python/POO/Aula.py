from Alumno import Alumno

def main():
    jesus = Alumno("Jesús", "Cruz Hernández")
    print(jesus)
    jesus.saludar()
    jesus.adios()

    goku = Alumno("Goku", "")
    goku.saludar()
    goku.adios()
    
if __name__ == "__main__":
    main()
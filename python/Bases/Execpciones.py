
def calcular(numero1, numero2):
    print(f"###Intentando dividir {numero1} entre {numero2}" )
    
    try:
        print("resultado:", numero1/numero2)
    except ZeroDivisionError as e:
        print("Error de capa 8, lea bien su código")
    except Exception as e:
        print("Sucedio un error inesperado")
    finally:
        print("Terminando de ejecutar la función")


def main():
    calcular(15,5)
    calcular(0, 5)
    calcular(5, 0)
    calcular(5, "hola")

if __name__ == "__main__":
    main()



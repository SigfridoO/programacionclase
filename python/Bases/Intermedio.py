
def main():
    numero = 5

    # listas
    miListaDeCompras=['Raspberry', 'Monitor', 'Teclado']
    miListaDeComponentes = []

    # diccionario
    calificaciones = {'Programacion': 85, 
                      'Microcontroladores': 80,
                      'Maquinas': -20 }
    proyectoTitulacion = {}

    if numero == 5:
        print("numero es igual a 5")

    if False:
        print("Se ejecuto el false")

    if None:
        print("Se ejecuto el None")

    if miListaDeCompras:
        print(miListaDeCompras)
    
    if miListaDeComponentes:
        print(miListaDeComponentes)

    if calificaciones:
        print(calificaciones)
    
    if proyectoTitulacion:
        print(proyectoTitulacion)

if __name__ == "__main__":
    main()
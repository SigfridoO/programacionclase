from Semaforo import Semaforo
from Intermediario import Intermediario


def main():
    print("Dentro de main")
    intermediario = Intermediario()
    print ("despues d intermediario")
    semaforo = Semaforo()
    semaforo.establecer_intermediario(intermediario)
    semaforo.iniciar_semaforo()


if __name__ == "__main__":
    main()
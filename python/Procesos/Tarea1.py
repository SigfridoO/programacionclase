import time
from datetime import datetime
import threading

def tarea(nombre:str, duracion: float):
    print(f"Iniciando la tarea {nombre} con una duración\
           de {duracion} segundos a las {datetime.now()}")

    time.sleep(duracion)
    print(f"Se ha finalizado la tarea {nombre} a las {datetime.now()}")

def main():
    print("Dentro de main")
    # Cubrebocas
    #tarea_maquina1 = tarea("Máquina 1", 5)
    #tarea_maquina2 = tarea("Maquina 2", 4)

    tarea1 = threading.Thread(target=tarea , args=("Máquina 1", 5))
    tarea2 = threading.Thread(target=tarea , args=("Máquina 2", 4))

    tarea1.start()
    tarea2.start()

if __name__ == "__main__":
    main()
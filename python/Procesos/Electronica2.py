from gpiozero import LED
from time import sleep

# Definir el pin GPIO al cual está conectado el LED (por ejemplo GPIO 17)
led = LED(17)

# Bucle para encender y apagar el LED cada 1 segundo
try:
    while True:
        led.on()    # Encender LED
        sleep(1)    # Esperar 1 segundo
        led.off()   # Apagar LED
        sleep(1)    # Esperar 1 segundo
except KeyboardInterrupt:
    print("Programa terminado")


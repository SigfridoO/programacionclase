# import gpiod
# import time

# LED_PIN = 4
# chip = gpiod.Chip('gpiochip0')
# DO_00 = chip.get_line(LED_PIN)
# DO_00.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

# try:
#    while True:
#        DO_00.set_value(1)
#        time.sleep(1)
#        DO_00.set_value(0)
#        time.sleep(1)
# finally:
#    DO_00.release()

import time
import gpiod
from gpiod.line import Direction, Value

LINE = 17

# Solicitar el control de la línea GPIO sin utilizar 'with'
chip = gpiod.Chip("/dev/gpiochip0")
request = chip.request_lines(
    consumer="blink-example",
    config={
        LINE: gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.INACTIVE
        )
    }
)

try:
    while True:
        # Activar el valor de la línea
        request.set_value(LINE, Value.ACTIVE)
        time.sleep(1)
        
        # Desactivar el valor de la línea
        request.set_value(LINE, Value.INACTIVE)
        time.sleep(1)

except KeyboardInterrupt:
    # Capturar Ctrl+C para salir del bucle
    print("Interrupción del usuario, saliendo...")

finally:
    # Cerrar manualmente la solicitud y liberar los recursos GPIO
    request.release()
    chip.close()
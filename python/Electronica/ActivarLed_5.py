import gpiod
import time

LED_PIN = 4
chip = gpiod.Chip('gpiochip0')
DO_00 = chip.get_line(LED_PIN)
DO_00.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

try:
   while True:
       DO_00.set_value(1)
       time.sleep(1)
       DO_00.set_value(0)
       time.sleep(1)
finally:
   DO_00.release()
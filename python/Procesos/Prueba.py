import gpiod
import time

LED_PIN = 17  # Número del pin GPIO
chip = gpiod.Chip('gpiochip0')  # Para Raspberry Pi 5, se utiliza 'gpiochip4'
led_line = chip.get_line(LED_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        led_line.set_value(1)  # Encender LED
        time.sleep(1)
        led_line.set_value(0)  # Apagar LED
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    led_line.release()

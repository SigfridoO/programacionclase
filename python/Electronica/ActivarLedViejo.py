import time
import gpiod
from gpiod.line import Direction, Value

LINE = 27
BOTON_0 = 18

with gpiod.request_lines(
    "/dev/gpiochip4",
    consumer="blink-example",
    config={
        LINE: gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.ACTIVE
        ),
        BOTON_0: gpiod.LineSettings(
            direction=Direction.INPUT
        )
    },
) as request:
    while True:

        lectura=request.get_value(BOTON_0)
        request.set_value(LINE, lectura)
        # request.set_value(LINE, Value.ACTIVE)
        # time.sleep(1)
        # request.set_value(LINE, Value.INACTIVE)
        # time.sleep(1)

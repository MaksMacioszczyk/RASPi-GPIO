##LIBS##
import time
from utils.GPIO import *

##CONST##
LED_PIN = 4

##VARIABLES##


##INIT##
exportGPIO(LED_PIN, OUT)
##INIT_VARIABLES##
start = time.time()

##MAIN##
while time.time() - start < 10:
    current_pin_value = getGPIOValue(LED_PIN)
    print(current_pin_value)
    setGPIO(LED_PIN, not current_pin_value)
    
    time.sleep(1)
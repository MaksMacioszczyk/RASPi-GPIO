import os
import subprocess

IN = "in"
in_values = [True, 1, "IN", IN]

OUT = "OUT"
out_values = [False, 0, "out", OUT]

HIGH = 1
high_values = [True, HIGH]

LOW = 0
low_values = [False, LOW]

GPIO_DIR = "/sys/class/gpio"
GPIO_EXPORT_DIR = os.path.join(GPIO_DIR, "export")

GPIO_PIN_DIR = lambda pin_number: os.path.join(GPIO_DIR, "gpio" + str(pin_number))
GPIO_DIRECTION_DIR = lambda pin_number: os.path.join(GPIO_PIN_DIR(pin_number), "direction")
GPIO_VALUE_DIR = lambda pin_number: os.path.join(GPIO_PIN_DIR(pin_number), "value")

def setGPIO(pin_number, value):
    isPinValid(pin_number)
    assert not os.path.isdir(GPIO_VALUE_DIR(pin_number))
    
    if value in high_values:
        value = 1
    elif value in low_values:
        value = 0
    else:
        raise "value is not valid"
    
    pin_dir = GPIO_VALUE_DIR(pin_number)
    subprocess.call(f'echo {value} > {pin_dir}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) 
    
def getGPIOValue(pin_number, return_type=bool):
    isPinValid(pin_number)
    assert not os.path.isdir(GPIO_VALUE_DIR(pin_number))
    
    value_dir = GPIO_VALUE_DIR(pin_number)
    
    to_return = os.popen(f'cat {value_dir}').read()[0]

    if return_type == bool:
        to_return = bool(int(to_return))
    elif return_type == int:
        to_return = int(to_return)
    elif return_type == str:
        to_return = str(to_return)

    return to_return

def exportGPIO(pin_number, direction):
    isPinValid(pin_number)
    
    if direction in in_values:
        direction = "in"
    elif direction in out_values:
        direction = "out"
    else:
        raise "direction is not valid"
    
    pin_dir = GPIO_PIN_DIR(pin_number)
    export_dir = GPIO_EXPORT_DIR
    direction_dir = GPIO_DIRECTION_DIR(pin_number)
    
    if os.path.isdir(pin_dir):
        if os.popen(f'cat {direction_dir}').read() != direction:
            subprocess.call(f'echo {direction} > {direction_dir}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    else:
        subprocess.call(f'echo {pin_number} > {export_dir}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) 
    
def isPinValid(pin_number):
    assert isinstance(pin_number, int), f'pin_number is not valid, type is {type(pin_number)} should be int'
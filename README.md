# RASPi-GPIO
Simple Raspberry Pi GPIO library in python

| No. | Function                                    | Action                                                                                                                                                                                                         |
|-----|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | exportGPIO(pin_number, direction)           | Used to init GPIO pin, and set its direction of working<br /><br /><br />pin_number - specify GPIO pin affected<br />direction - "out"/"in" set direction of communication                                     |
| 2   | getGPIOValue(pinNumber, return_type = bool) | Get value of GPIO pin <br /><br /><br />pin_number - specify GPIO pin to get value from<br />return_type - default:bool; int; str, specify type of returned value<br /><br />return: True or False, depends on return_type |
| 3   | setGPIO(pin_number, value)                  | Sets GPIO pin value <br /><br />pin_number - specify GPIO pin affected<br />value - True or False, value set to pin                                                                                                  |

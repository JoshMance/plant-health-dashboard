from Interface import *


x = Interface(ports=['/dev/ttyACM0'], 
              baudrate=9600, 
              timeout=0.1, 
              wait_time = 2)

val = x.get_moisture_values()
print(val)


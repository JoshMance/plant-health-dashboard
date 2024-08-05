from Interface import *
from numpy import mean, std
from json import dumps
from time import time

PORTS = ['/dev/ttyACM0']

interface = Interface(ports=PORTS, baudrate=9600, timeout=0.1, wait_time = 3)

values = interface.get_moisture_values()
if values == None:
    print(None)
else:
    data = dumps({"mean":round(mean(values),2), "sd":round(std(values), 2), "time":time()})
    print(data)
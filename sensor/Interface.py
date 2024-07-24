import serial
from time import time

# port='/dev/ttyACM0', baudrate=9600, timeout=.1

class Interface():
    def __init__(self, sensor_port, baudrate, timeout):
        self.arduino = serial.Serial(sensor_port, baudrate, timeout)

    def read_moisture(self, timeout):
        time_initial = time()
        while ((time()-time_initial) < timeout):
            data = self.arduino.readline().decode("utf-8")
            if (data) != '':
                return data
        return None
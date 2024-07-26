import serial
from time import time

"""
    Interface that reads moisture values from arduino controllers
    via serial port/s
"""
class Interface():

    def __init__(self, ports, baudrate, timeout, wait_time):
        self.wait_time = wait_time
        self.connections = [serial.Serial(port = port, 
                                baudrate = baudrate, 
                                timeout = timeout)
                            for port in ports]

    """ Loops though the list of connections to arduinos
        and attempts to read a value via the respective 
        serial port. This attempt ends if the wait_time is
        reached and/or a value has been recorded for each arduino 
    """
    def get_moisture_values(self):
        time_initial = time()
        values = [None for n in range(len(self.connections))]

        while (None in values):
            if (time()-time_initial) >= self.wait_time:
                break
            for index, arduino in enumerate(self.connections):
                data = arduino.readline().decode("utf-8")
                if (data) != '':
                    values[index] = int(data.strip("\r").strip("\n"))
        return values
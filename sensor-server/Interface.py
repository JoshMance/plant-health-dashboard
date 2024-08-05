import serial
from time import time

"""
    Interface that reads moisture values from arduino controllers
    via serial port/s
"""
class Interface():

    def __init__(self, ports, baudrate, timeout, wait_time):
        self.wait_time = wait_time
        self.connections = []
        for port in ports:
            try:
                self.connections.append(serial.Serial(port = port, baudrate = baudrate, timeout = timeout))
            except:
                raise Exception(f"could not open port {port}") 


    """ Loops though the list of connections to arduinos
        and attempts to read a value via the respective 
        serial port. This attempt ends if the wait_time is
        reached and/or a value has been recorded for each arduino 
    """
    def get_moisture_values(self):
        num_connections = len(self.connections)
        if num_connections == 0:
            return None
        else:
            time_initial = time()
            values = [None]
            num_measurements = 0
            while (num_measurements < num_connections):
                if (time()-time_initial) >= self.wait_time:
                    break
                for index, arduino in enumerate(self.connections):
                    data = arduino.readline().decode("utf-8").strip("\r").strip("\n")
                    if (data) != '':
                        values[index] = int(data)
                        num_measurements += 1
            
            
            return values
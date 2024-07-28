from Interface import *
from numpy import mean, std
from json import dumps
# import redis

# Connect to Redis
# redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Get the value of a key
# value = client.get('key')
# print(f'GET result -> {value.decode("utf-8")}')

PORTS = [] #['/dev/ttyACM0', '/dev/ttyACM1']

interface = Interface(ports=PORTS, baudrate=9600, timeout=0.1, wait_time = 3)

values = interface.get_moisture_values()
if values == None:
    print(None)
else:
    data = dumps({"num_sensors":len(values), "mean":mean(values), "sd":std(values)})
    print(data)
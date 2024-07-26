from Interface import *
# import redis

# Connect to Redis
# redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Get the value of a key
# value = client.get('key')
# print(f'GET result -> {value.decode("utf-8")}')

interface = Interface(ports=['/dev/ttyACM0', '/dev/ttyACM1'], 
              baudrate=9600, 
              timeout=0.1, 
              wait_time = 3)

data = interface.get_moisture_values()
print(data)
from numpy import mean, std
from json import dumps
from random import randint

val = randint(200, 1000)
values = [randint(val-10,val+10) for i in range(3)]

data = dumps({"num_sensors":len(values), "mean":mean(values), "sd":std(values)})
print(data)
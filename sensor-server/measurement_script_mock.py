from numpy import mean, std, round
from json import dumps
from random import randint
from time import time

val = randint(200, 1000)
values = [randint(val-10,val+10) for i in range(3)]

data = dumps({"mean":round(mean(values),2), "sd":round(std(values), 2), "time":time()})
print(data)
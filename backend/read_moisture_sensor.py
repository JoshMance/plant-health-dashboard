import serial

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)

while True:
    data = arduino.readline().decode("utf-8")
    if (data) != '':
        print(data)
        break
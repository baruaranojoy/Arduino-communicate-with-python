# https://pypi.python.org/pypi/pyserial/2.7#downloads
# link to download the package
import serial

ser = serial.Serial('COM3',9600) # establish serial connection


val = 0 # initialize val
data = ""
while 1:
    val = raw_input("0 to turnoff ,1 to turn on") # taking value from python shell
    ser.write(val) # writing value to serial monitor



# import serial liberary
import serial

# connect ot serial monitor
ser = serial.Serial('COM3',9600)

# close previous serial channel
ser.close()
while 1:
    ser.open() # open channel
    x = ser.readline() # reading a line from serial monitor
    print x # print the line
    ser.close() # clsoe the existing channel

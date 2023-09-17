import serial

a = int(input('Enter pixel position : '))
ser = serial.Serial("COM3", 9600)

ser.write([a])
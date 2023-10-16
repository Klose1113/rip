import serial
import time

arduino = serial.Serial('/dev/cu.usbmodem1101',115200)

while True:

    arduino.write(b'4\n')
    arduino.reset_output_buffer()

    time.sleep(3)

    arduino.write(b'5\n')
    arduino.reset_output_buffer()

    time.sleep(3)




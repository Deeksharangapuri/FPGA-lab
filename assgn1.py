
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
print(GPIO.input(12))
print(GPIO.input(15))
print(GPIO.input(16))
print(GPIO.input(18))

no = str(GPIO.input(12))+str(GPIO.input(15))+str(GPIO.input(16))+str(GPIO.input(18));

print(int(no,2))


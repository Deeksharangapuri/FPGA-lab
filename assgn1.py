
import RPi.GPIO as GPIO
import time



no = str(GPIO.input(12))+str(GPIO.input(15))+str(GPIO.input(16))+str(GPIO.input(18));

print(int(no,2))


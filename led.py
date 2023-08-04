import RPi.GPIO as GPIO
from time import sleep

CONTROL_PIN = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
while True:
    GPIO.output(17,GPIO.HIGH)
    print ("LED ON")
    sleep(1)
    GPIO.output(17,GPIO.LOW)
    print ("LED OFF")
    sleep(1)

# Simple single LED control
# program to familiarize with GPIO

# Import Raspberry GPIO library
import RPi.GPIO as GPIO
import time

# Set GPIO Pins as Broadcom interfaced
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO control Pin
led_control_pin = 17

# Set the GPIO pin as Output
GPIO.setup(led_control_pin,GPIO.OUT)

print("LED control pin is set to:")
print(led_control_pin)

while True:
    # Set GPIO PIN to High
    GPIO.output(led_control_pin, GPIO.HIGH)
    print ("LED is ON")
    time.sleep(5)
    
    #Set GPIO PIN to Low
    GPIO.output(led_control_pin, GPIO.LOW)
    print ("LED is OFF")
    time.sleep(5)

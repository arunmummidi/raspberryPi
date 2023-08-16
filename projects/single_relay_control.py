# Simple single relay module control

# Import Raspberry GPIO library
import RPi.GPIO as GPIO
import time

# Set GPIO Pins as Broadcom interfaced
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO control Pin
relay_control_pin = 17

# Set the GPIO pin as relay 1 control
GPIO.setup(relay_control_pin,GPIO.OUT)

for count in range(0, 20):
    # Set GPIO PIN to High
    GPIO.output(relay_control_pin, GPIO.HIGH)
    print ("Relay is ON. Wait 5 seconds")
    time.sleep(5)

    #Set GPIO PIN to Low
    GPIO.output(relay_control_pin, GPIO.LOW)
    print ("Relay is OFF. Wait 5 seconds")
    time.sleep(5)

GPIO.cleanup()
print("Clean up complete. Bye!")

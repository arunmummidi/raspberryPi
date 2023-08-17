# Simple single LED control
# program to familiarize with GPIO

"""Import Raspberry GPIO library"""
import time
from RPi import GPIO

# Set GPIO Pins as Broadcom interfaced
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO control Pin
CONTROL_PIN = 17

# Set the GPIO pin as Output
GPIO.setup(CONTROL_PIN,GPIO.OUT)

print("LED control pin is set to:")
print(CONTROL_PIN)

for count in range(0, 10):
    # Set GPIO PIN to High
    GPIO.output(CONTROL_PIN, GPIO.HIGH)
    print ("LED is ON")
    time.sleep(1)
    
    #Set GPIO PIN to Low
    GPIO.output(CONTROL_PIN, GPIO.LOW)
    print ("LED is OFF")
    time.sleep(1)

GPIO.cleanup()
print("Clean up done")

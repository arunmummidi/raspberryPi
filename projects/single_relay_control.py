# WARNING: If you plan to use relay
# with AC ouptputs, use extreme 
# caution as it could potentialy
# cause injury or death.

# Simple single relay module control.
# 1.5V to 3V LED/DC motor is connected
# to relay output to test the relay 
# operation. This will prevent injury
# or component breakdown due to improper
# AC connections. This project helps to
# familiarize  with the circuit only.


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

for count in range(0, 5):
    # Set GPIO PIN to High
    GPIO.output(relay_control_pin, GPIO.HIGH)
    print ("Relay is ON. Keep state for 5 seconds")
    time.sleep(5)

    #Set GPIO PIN to Low
    GPIO.output(relay_control_pin, GPIO.LOW)
    print ("Relay is OFF. Keep state for 5 seconds")
    time.sleep(5)

GPIO.cleanup()
print("Clean up complete. Bye!")

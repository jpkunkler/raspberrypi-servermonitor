import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT)

while True:
    input_state = GPIO.input(4)
    if input_state == False:
        if GPIO.input(23) == True:
            GPIO.output(23, 0)
        else: 
            GPIO.output(23, 1)
        time.sleep(0.2)


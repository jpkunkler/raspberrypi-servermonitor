import RPi.GPIO as GPIO
import time
import os
from config import OS_PATH

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(17)
    if input_state == False:
        query = "python"+OS_PATH+"get_status.py" 
        os.system(query)
    time.sleep(0.2)

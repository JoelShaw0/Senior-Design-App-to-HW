import RPi.GPIO as GPIO
import time
import os
from datetime import datetime as dt

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)

input_value = GPIO.input(16)

while(1):
    x = dt.now()
    string = x.strftime("%m-%d-%Y%H:%M:%S")
    time.sleep(1)
    
    if GPIO.input(16) == True:
        os.system("libcamera-still -o /home/joel/Pictures/" + string + ".jpg")
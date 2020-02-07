import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
cnt = 0
try:
        while cnt < 3:
                       
                       
                       GPIO.output(14,GPIO.HIGH)
                       GPIO.output(15,GPIO.HIGH)
                       GPIO.output(18,GPIO.HIGH)
                       time.sleep(0.5)
                       
                       cnt += 1
except KeyboardInterrupt:
        GPIO.cleanup()

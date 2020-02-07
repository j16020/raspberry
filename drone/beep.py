import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
cnt = 0
try:
        while cnt < 3:
                       GPIO.output(4,GPIO.HIGH)
                       time.sleep(0.5)

                       GPIO.output(4,GPIO.LOW)
                       time.sleep(0.5)
                       cnt += 1
except KeyboardInterrupt:
        GPIO.cleanup()
GPIO.cleanup()
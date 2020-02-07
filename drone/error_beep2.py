import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

try:


                       GPIO.output(4,GPIO.LOW)
                       GPIO.output(4,GPIO.HIGH)
                       time.sleep(0.1)

                       GPIO.output(4,GPIO.LOW)
                       time.sleep(0.1)
                       GPIO.output(4,GPIO.HIGH)
                       time.sleep(0.1)

                       GPIO.output(4,GPIO.LOW)
                       time.sleep(0.1)
except KeyboardInterrupt:
        GPIO.cleanup()
GPIO.cleanup()

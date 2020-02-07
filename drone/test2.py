import RPi.GPIO as GPIO
import time
import cv2


GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)

from pyparrot.Minidrone import Mambo

mamboAddr = "D0:3A:CD:C4:E6:21"
mambo = Mambo(mamboAddr, use_wifi=False)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    # get the state information
    print("sleeping!!!!!!!!!!!!")
    mambo.smart_sleep(1)
    mambo.ask_for_state_update()
    mambo.smart_sleep(1)
    import func1
    mambo.safe_takeoff(3)

    pic_success = mambo.take_picture()
    import func1

    print("land")
    mambo.safe_land(2)
    mambo.smart_sleep(2)    

    picture_names = mambo.groundcam.get_groundcam_pictures_names()




    path_w = '/home/pi/output'
    for i in range(0, len(picture_names)):
      psn = picture_names[i]
      frame = mambo.groundcam.get_groundcam_picture(psn, True)
      cv2.imwrite(path_w+'/yamada'+str(i)+'.jpg',frame)

    print("disconnect")
    mambo.disconnect()
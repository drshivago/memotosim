from picamera import PiCamera
import time
import datetime

framesize = (640, 480)
camera = PiCamera()
camera.rotation = 180

d = datetime.datetime.now()
timer = str(d.month) + str(d.day) + str(d.hour) + ':' + str(d.minute) + '-' 
for filename in camera.capture_continuous(timer + '{counter:01d}.jpg'):
	print('Captured %s' % filename)
	time.sleep(30) #wait 30 seconds

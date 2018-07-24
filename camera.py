from picamera import PiCamera
import time

framesize = (640, 480)
camera = PiCamera()

try: 
	for filename in camera.capture_continuous('img{counter:03d}.jpg):
		print('Captured %s' % filename)
		sleep(30) #wait 30 seconds

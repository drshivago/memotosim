from picamera import PiCamera
import time

framesize = (640, 480)
camera = PiCamera()


for filename in camera.capture_continuous(f'img{counter:03d}.jpg):
	print('Captured %s' % filename)
	sleep(30) #wait 30 seconds

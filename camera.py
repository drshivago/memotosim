import picamera
import time

framesize = (640, 480)

try: 
	with picamera.PiCamera() as camera:
		camera.resolution = framesize
		
		time.sleep(2)
		

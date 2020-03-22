from time import sleep
from picamera import PiCamera
import adafruit_gps
import serial
import time


def get_coords():
	
	coords = {}
	
	# for a computer, use the pyserial library for uart access
	uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)
	gps = adafruit_gps.GPS(uart, debug=False)  # Use UART/pyserial
	
	while True:
		gps.update()
		
		if len(str(gps.latitude).split('.')[-1]) > 5 and len(str(gps.longitude).split('.')[-1]) > 5:
			coords['lat'] = gps.latitude
			coords['lon'] = gps.longitude
			
			break
	
	return coords

def main():
	camera = PiCamera()
	camera.resolution = (1920, 1080)
	camera.start_preview()
	# Camera warm-up time
	sleep(2)
	camera.capture('foo.jpg')


if __name__ == '__main__':
   print(get_coords())

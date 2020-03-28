import time
import RPi.GPIO as GPIO
from picamera import PiCamera
import adafruit_gps
import serial
import time
from GPSPhoto import gpsphoto
from pathlib import Path


def get_coords():
	'''
	Get GPS coordinates with adafruit GPS module
	:return : (tuple) latitude and longitude coordinates
	
	'''
	
	coords = {}
	
	# for a computer, use the pyserial library for uart access
	uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)
	gps = adafruit_gps.GPS(uart, debug=False)  # Use UART/pyserial
	
	while True:
		gps.update()
		
		if len(str(gps.latitude).split('.')[-1]) > 5 and len(str(gps.longitude).split('.')[-1]) > 5:
			return gps.latitude, gps.longitude
			
			break
	
	
def timestamp():
	'''
	Create filename for picture
	:return : (str) filename (timestamp)
	
	'''
	timestamp = time.strftime("%H%M%S",time.gmtime())
	filename = 'img_' + timestamp + '.jpg'
	
	return filename

	
def edit_exif(path, gps_data):
	'''
	Takes gps coordinates and inserts them to the picture's metadata
	:param path : (str) path to picture
	:parma gps_data : (tuple) (latitude, longitude, altitude)
	
	'''
	photo = gpsphoto.GPSPhoto(path)
	info = gpsphoto.GPSInfo(gps_data)
	photo.modGPSData(info, path)
	
	
def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	camera = PiCamera()
	camera.resolution = (1280, 720)
	preview = camera.start_preview()
	preview.fullscreen = False
	preview.window = (0, 0, 1280, 720)

	while True:
		input_state = GPIO.input(21)
		
		if input_state == False:
			date = time.strftime("%Y-%m-%d", time.gmtime())
			folder = 'IMG/' + date
	
			# Creates a directory for pictures based on the current date
			Path(folder).mkdir(parents=True, exist_ok=True)
	
			coords = get_coords()
	
			filename = timestamp()
			picture_path = folder + '/' + filename
	
			camera.capture(picture_path)
	
			edit_exif(picture_path, coords)
	

if __name__ == '__main__':
	main()

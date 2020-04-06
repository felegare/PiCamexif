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
	
	# Camera settings
	camera = PiCamera()
	camera.resolution = (1280, 720) # Pictures' resolution : 720p
	
	# Preview window settings
	preview = camera.start_preview()
	preview.fullscreen = False
	preview.window = (0, 0, 480, 320) # Resolution of the screen

	while True:
		input_state = GPIO.input(21)
		
		# If button is pressed
		if input_state == False:
			
			# Stores the date and time
			current_date = time.strftime("%Y-%m-%d", time.localtime())
			current_time = time.strftime("%H%M%S", time.localtime())
			
			# Creates a directory for pictures based on the current date
			Path(f'IMG/{current_date}').mkdir(parents=True, exist_ok=True)
			
			# Gets the longitude and latitude coordinates frome the GPS module
			coords = get_coords()
	
			# Creates unique path for the picture from the date and time
			picture_path = f'IMG/{current_date}/IMG_{current_time}.jpeg'
	
			# Takes the picture
			camera.capture(picture_path)
			
			# Writes the coordinates to the picture's EXIF tags
			# Saves the pictures
			edit_exif(picture_path, coords)
	

if __name__ == '__main__':
	main()

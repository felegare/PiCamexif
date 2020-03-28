import time
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
			return gps.latitude, gps.longitude, gps.altitude_m
			
			break
	
	
def timestamp():
	'''
	Create filename for picture
	:return : (str) filename (timestamp)
	
	'''
	timestamp = time.strftime("%H%M%S",time.gmtime())
	filename = 'img_' + timestamp + '.jpg'
	
	return filename


def take_picture(path):
	'''
	Takes picture with Raspberry Pi Camera Module
	:param path : (str) path to picture
	
	'''
	camera = PiCamera()
	camera.resolution = (1280, 720)
	camera.capture(path)
	
def edit_exif(path, gps_data):
	'''
	Takes gps coordinates and inserts them to the picture's metadata
	:param path : (str) path to picture
	:parma gps_data : (tuple) (latitude, longitude, altitude)
	
	'''
	photo = gpsphoto.GPSPhoto(path)
	info = gpsphoto.GPSInfo((gps_data[0], gps_data[1]), int(gps_data[2]))
	photo.modGPSData(info, path)
	
	
def main():
	date = time.strftime("%Y-%m-%d", time.gmtime())
	folder = 'IMG/' + date
	
	# Creates a directory for pictures based on the current date
	Path(folder).mkdir(parents=True, exist_ok=True)
	
	coords = get_coords()
	
	filename = timestamp()
	picture_path = folder + '/' + filename
	
	take_picture(picture_path)
	
	edit_exif(picture_path, coords)
	

if __name__ == '__main__':
	main()

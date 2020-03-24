from time import sleep
from picamera import PiCamera
import adafruit_gps
import serial
import time
import PIL.ExifTags
import PIL.Image
from pathlib import Path


def get_coords():
	
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
	:return : (str) filename (timestamp) for picture
	
	'''
	timestamp = time.strftime("%Y%m%d%H%M%S",time.gmtime())
	filename = 'img_'+ timestamp + '.jpg'
	
	return filename

def take_picture(folder_name, file_name):
	'''
	:param folder : (str) name of dedicated image folder for pictures
	:param name : (str) filename given by the timestamp function
	
	'''
	camera = PiCamera()
	camera.resolution = (1280, 720)
	camera.capture(folder_name + '/' + file_name)
	
	
def main():
	folder = "PiCamexif_IMG"
	Path(folder).mkdir(parents=True, exist_ok=True)
	
	filename = timestamp()
	take_picture(folder, filename)
	

if __name__ == '__main__':
   main()

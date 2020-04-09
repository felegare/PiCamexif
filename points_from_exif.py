import os
from GPSPhoto import gpsphoto
import simplekml
import shutil

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


def send_zip_file(lof):
	
	user_address = os.environ['PI_ADDRESS']
	user_password = os.environ['PI_PASSWORD']
	
	destination = str(input('Enter destination address : '))
	
	msg = MIMEMultipart()
	msg['From'] = user_address
	msg['To'] = destination
	msg['Subject'] = 'Pictures from PiCamexif'
	
	msg.preamble = 'test email sent from python'
	
	for zipfile_path in lof:
		
		zipfile = MIMEBase('application', 'zip')
		zf = open(zipfile_path, 'rb')
		zipfile.set_payload(zf.read())
		encoders.encode_base64(zipfile)
		zipfile.add_header('Content-Disposition', 'attachment', filename=zipfile_path)
		msg.attach(zipfile)
	
	msg = msg.as_string()
	
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(user_address, user_password)
	
	server.sendmail(user_address, destination, msg)
	server.quit


def main():
	
	lof = []
	
	content = os.listdir('IMG/')
	
	for directory in content:
		
		if not directory.endswith('.zip'):
		
			pictures = os.listdir(f'IMG/{directory}')
			kml = simplekml.Kml()
		
			for image in pictures:
				
				if image.endswith('.jpeg'):
					
					picture_path = f'IMG/{directory}/{image}'
					data = gpsphoto.getGPSData(picture_path)
					point = kml.newpoint(name=image, coords=[(data['Longitude'],data['Latitude'])])
					
					pic_path = kml.addfile(picture_path)
					point.description = f'<img src="./{image}" alt="picture" width="400" height="300" align="left" />'
			
			kml.save(f'IMG/{directory}/{directory}.kml')
			
		if not directory.endswith('.zip'):
			shutil.make_archive(f'IMG/{directory}', 'zip', f'IMG/{directory}')
	
			lof.append(f'IMG/{directory}.zip')
		
	send_zip_file(lof)
	
	
if __name__ == '__main__':
	main()

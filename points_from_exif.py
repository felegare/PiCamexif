import os
from GPSPhoto import gpsphoto
import simplekml
import shutil

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def create_kml(folder):
	'''
	Creates a kml points file from the gps data extracted from the pictures
	:param folder : (directory) path of the picture folder
	
	'''
	
	pictures = os.listdir(f'IMG/{folder}')
	kml = simplekml.Kml()
		
	for image in pictures:
				
		if image.endswith('.jpeg'):
					
			picture_path = f'IMG/{folder}/{image}'
			data = gpsphoto.getGPSData(picture_path)
			point = kml.newpoint(name=image, coords=[(data['Longitude'],data['Latitude'])])
					
			pic_path = kml.addfile(picture_path)
			point.description = f'<img src="./{image}" alt="picture" width="500" align="left" />'
			
	kml.save(f'IMG/{folder}/{folder}.kml')
	
	
def create_zipfile(folder, lof):
	'''
	Creates a zipfile containing all the pictures from the same folder and adds its path to a list (lof)
	:param folder : (directory) directory that needs to be compressed 
	:param lof : (list) list of path(s) to zipfile(s)
	
	'''
	# Create zipfile
	shutil.make_archive(f'IMG/{folder}', 'zip', f'IMG/{folder}')
	
	# Append path of the zipfile to the lof
	lof.append(f'IMG/{folder}.zip')



def send_zip_file(lof):
	'''
	Sends all of the zipfile(s) created via email
	:param lof : (list) list of path(s) to zipfile(s)
	
	'''
	# Local environment variables for Raspberri Pi authentification
	user_address = os.environ['PI_ADDRESS']
	user_password = os.environ['PI_PASSWORD']
	
	# User writes the recipient's address
	recipient = str(input('Enter destination address : '))
	
	# Message formating
	msg = MIMEMultipart()
	msg['From'] = user_address
	msg['To'] = recipient
	msg['Subject'] = 'Pictures from PiCamexif'
	
	text = """<body>
<img src="https://github.com/felegare/PiCamexif/blob/master/banner/picamexifbanner.png?raw=true" height="100"/>
<h3>This email was sent from a <i>PiCamexif</i> Raspberry Pi.</h3>
<p>Each zip file attached to this email contains :</p>
<ul>
	<li>A kml file</li>
	<li>Pictures</li>
</ul>
<p>You can open the kml file using Google Earth Pro.<br>To open the kml file :</p>
<ol>
	<li>Make sure Google Earth Pro is installed on your computer (if not, download it <a href="https://www.google.com/earth/versions/#earth-pro">here</a>)</li>
	<li>Download the attachment</li>
	<li>Extract all of its content</li>
	<li>Double click on the kml file.</li>
</ol>
<br/>
<h4>Visit the PiCamexif <a href="https://github.com/felegare/PiCamexif">GitHub page</a></h4>
</body>"""
	
	body = MIMEText(text, 'html')
	msg.attach(body)			   
	
	# Attach zipfile(s)
	for zipfile_path in lof:
		
		zipfile = MIMEBase('application', 'zip')
		zf = open(zipfile_path, 'rb')
		zipfile.set_payload(zf.read())
		encoders.encode_base64(zipfile)
		zipfile.add_header('Content-Disposition', 'attachment', filename=zipfile_path)
		msg.attach(zipfile)
	
	msg = msg.as_string()
	
	# Connection parameters
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(user_address, user_password)
	
	# Sends the message
	server.sendmail(user_address, recipient, msg)
	server.quit


def main():
	
	lof = []
	
	content = os.listdir('IMG/')
	
	for directory in content:
		
		if not directory.endswith('.zip'):
		
			create_kml(directory)
			
			create_zipfile(directory, lof)
		
	send_zip_file(lof)
	
	
if __name__ == '__main__':
	main()

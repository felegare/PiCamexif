import os
from GPSPhoto import gpsphoto
import simplekml
import shutil

def main():
	
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

if __name__ == '__main__':
	main()

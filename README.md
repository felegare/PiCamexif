<p align="center">
<img src="/banner/picamexifbanner.png" width="400">
</p>

---

### Table of Contents
- [PiCamexif Overview](#PiCamexif-Overview)
  * [Hardware Components](#Hardware-Components)
  * [Requirements](#Requirements)
  * [Raspberry Pi Configuration](#Raspberry-Pi-Configuration)
    * [Operating System](#Operating-System)
    * [Activating the Camera](#Activating-the-Camera)
    * [virtualenv](#virtualenv)

* [pi_cam.py](#pi_campy)
* [points_from_exif.py](#points_from_exifpy)

# PiCamexif Overview
PiCamexif is a Raspberry Pi based camera designed to produce pictures containing GPS data. This Raspberry Pi uses a Raspberry Pi Camera Module and Adafruit's GPS Module with a simple python program to write the GPS coordinates in the EXIF tags of the pictures.
This README will go over how the program works and how the hardware is configured. 

All the links for the hardware used for this project are included in the 'Hardware Components' section below. 

## Hardware Components

| # | Components | Image | Comment |
| --- | --- | --- | --- |
| 1 | [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) | <img src="https://www.raspberrypi.org/homepage-9df4b/static/0ac033e17962a041a898d92057e60def/052d8/67d8fcc5b2796665a45f61a2e8a5bb7f10cdd3f5_raspberry-pi-3-1-1619x1080.jpg" width="200"> | |
| 2 | [Micro SD Card](https://www.samsung.com/us/computing/memory-storage/memory-cards/microsdhc-evo-plus-memory-card-w--adapter-32gb--2017-model--mb-mc32ga-am/) | <img src="https://image-us.samsung.com/SamsungUS/home/computing/memory-and-storage/memory-cards/pd/mb-mc32ga-am/gallery-v2/MB-MC32GA_001_Front_red.jpg?$product-details-jpg$" width="200"> | The SD Card is used to for the Raspberry Pi's operating system and for storage. In this case, a 32GB card might be a little overkill so you could use a 16GB or 8GB micro SD card just fine. |    
| 3 | [Raspberry Pi Camera Module](https://www.raspberrypi.org/products/camera-module-v2/) | <img src="https://ae01.alicdn.com/kf/HTB1UmwlgwMPMeJjy1Xbq6AwxVXar/Raspberry-Pi-Camera-Module-V2-Original-RPI-3-Camera-Official-camera-V2-8MP-1080P30.jpg" width="200"> | This 8 megapixel camera is really simple to set up and can be used to take photos and videos | 
| 4 | [Adafruit GPS Module](https://www.adafruit.com/product/746) | <img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimages.esellerpro.com%2F2457%2FI%2F31%2Fadafruit-ultimate-gps-breakout.jpg&f=1&nofb=1" width="200"> | This small GPS module can track up to 22 satellites and offers a surprising level of precision. It also comes with a piece of header you have to solder on to use it with a breadboard. |
| 5 | [TTL Serial Adapter Module USB to UART Converter](https://www.aliexpress.com/item/32774943192.html) | <img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimg.dxcdn.com%2Fproductimages%2Fsku_443779_1.jpg&f=1&nofb=1" width="200"> | This adapater is very useful because you can connect the GPS module to the Raspberry Pi without using any of the GPIO pins for power or data transmission. |
| 6 | [4 Pins Tact Switch](https://grobotronics.com/tact-switch-6x6mm-5mm-4pins.html) | <img src="https://grobotronics.com/images/thumbnails/350/350/detailed/1/Tact_Switch__48812_zoom.jpg" width="200"> | This tiny switch is used as a trigger button for the camera. | 
| 7 | [Kuman 3.5 inch TFT LCD Display](https://www.amazon.ca/gp/product/B072Q3VRXT/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1) | <img src="https://lh3.googleusercontent.com/proxy/D7GPAY6GT_u-lU44Tyi0U5aHZ7fAQ490YwIva4eoqLhbOTOxzkqaRBQLD52fd0RZsqx9ht_tj2a9UIBwWrajPceldp5WvHP7LovQfIeKF3C4IpOEQWZJ" width="200"> | This screen is ideal for this project. It connects to the board with a HDMI to HDMI connector, uses only 26 of the 40 GPIO pins of the Raspberry Pi and works out of the box |
| 8 | [Lithium Ion Polymer Battery - 3.7v 2500mAh](https://www.adafruit.com/product/328) | <img src="https://images-na.ssl-images-amazon.com/images/I/41-gVFOj8CL._SX425_.jpg" width="200"> | Battery |
| 9 | [PowerBoost 1000 Charger](https://www.adafruit.com/product/2465) | <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTRduT1SZFd367tEK3Sw7-SIAWpYiphWkw4MIYBWqUgjh3pmN2l&usqp=CAU" width="200"> | This small board  |

##### This list is not final and will be updated throughout development.

## Requirements
* Python 3.7 with the following librairies :
  - picamera
  - adafruit-circuitpython-gps
  - gpsphoto
  - exifread (required by gpsphoto)
  - pillow (required by gpsphoto)
  - piexif (required by gpsphoto)
  - simplekml
  
## Raspberry Pi Configuration

#### Operating System
You can [download](https://www.raspberrypi.org/downloads/raspbian/) the Raspbian operating system and install it on your Micro SD card using Win32DiskImager. For this project, I used 'Raspbian Buster with desktop and recommended software'. It might work with other Raspbian distros but I have not tested it. 

#### Activating the Camera

Once you boot up the Raspberry Pi, open the Terminal and run :
```shell
sudo raspi-config
```
Using the arrow keys select 'Interfacing options' and press enter. You should now see the 'Camera' option. Select it and press enter again to enable the camera. Finally, reboot the Raspberry Pi.

If you don't see the 'Camera' option, return to the terminal by pressing escape  twice and run :
```shell
sudo apt-get update
```
then

```shell
sudo apt-get upgrade
```
You should now see the 'Camera' option when you are in the 'Interfacing options'. Once the camera is enabled, reboot the Raspberry Pi.

#### virtualenv

If you wish to install virtualenv on your Raspberry Pi, simply run :
```shell
sudo pip install virtualenv
```
You can then set and activate your python environment with the following commands :
```shell
virtualenv YOUR_PATH --python=3.7
source activate YOUR_ENV/bin/activate
pip install picamera adafruit-circuitpython-gps gpsphoto exifread pillow piexif simplekml
```
> Note : You could also install the python librairies without using virtualenv.

# pi_cam.py
This program should run at start-up and open a preview window showing the camera view. You can then press the trigger button to take a picture.

# points_from_exif.py
Creates a compressed folder containing a KML file and the pictures from every directories from the 'IMG' foler. It then compresses the folder containing the kml file and the pictures and sends the zipfile by email.

Content of the email :
><body>
><img src="https://github.com/felegare/PiCamexif/blob/master/banner/picamexifbanner.png?raw=true" height="100"/>
><h3>This email was sent from a <i>PiCamexif</i> Raspberry Pi.</h3>
><p>Each zip file attached to this email contains :</p>
><ul>
>	<li>A kml file</li>
>	<li>Pictures</li>
></ul>
><p>You can open the kml file using Google Earth Pro.<br>To open the kml file :</p>
><ol>
>	<li>Make sure Google Earth Pro is installed on your computer (if not, download it <a href="https://www.google.com/earth/versions/#earth-pro">here</a>)</li>
>	<li>Download the attachment</li>
>	<li>Extract all of its content</li>
>	<li>Double click on the kml file.</li>
></ol>
><br/>
><h4>Visit the PiCamexif <a href="https://github.com/felegare/PiCamexif">GitHub page</a></h4>
></body>





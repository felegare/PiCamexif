### Table of Contents
- [PiCamExif Overview](#PiCamexif-Overview)
  * [Hardware Components](#Hardware-Components-(for-now))
  * [Requirements](#Requirements)
  * [Raspberry Pi Configuration](#Raspberry-Pi-Configuration)
    * [Raspberry Pi](#Raspberry-Pi)
      1. Operating system
      2. Activating the camera
      3. Installing Virtualenv
    * [Python Virtualenv](#Python-Virtualenv)

* PiCam.py


# PiCamexif Overview
PiCamexif is a Raspberry Pi based camera designed to produce pictures containing GPS data. This Raspberry Pi uses a Raspberry Pi Camera Module and Adafruit's GPS Module with a simple python program to write the GPS coordinates in the EXIF tags of the pictures.
This README will go over how the program works and how the hardware is configured. 

All the links for the hardware used for this project are included in the 'Hardware Components' section below. 

## Hardware Components (for now)
1. [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)

<p align="center">
  <img src="https://www.raspberrypi.org/homepage-9df4b/static/0ac033e17962a041a898d92057e60def/052d8/67d8fcc5b2796665a45f61a2e8a5bb7f10cdd3f5_raspberry-pi-3-1-1619x1080.jpg" width="300">
</p>

2. [Micro SD Card](https://www.samsung.com/us/computing/memory-storage/memory-cards/microsdhc-evo-plus-memory-card-w--adapter-32gb--2017-model--mb-mc32ga-am/)

    The SD Card is used to for the Raspberry Pi's operating system and for storage. In this case, a 32GB card might be a little overkill so you could use a 16GB or 8GB micro SD card just fine. 

<p align="center">
  <img src="https://image-us.samsung.com/SamsungUS/home/computing/memory-and-storage/memory-cards/pd/mb-mc32ga-am/gallery-v2/MB-MC32GA_001_Front_red.jpg?$product-details-jpg$" width="250">
</p>

3. [Raspberry Pi Camera Module](https://www.raspberrypi.org/products/camera-module-v2/)

    This 8 megapixel camera is really simple to set up and can be used for picture and video.

<p align="center">
  <img src="https://ae01.alicdn.com/kf/HTB1UmwlgwMPMeJjy1Xbq6AwxVXar/Raspberry-Pi-Camera-Module-V2-Original-RPI-3-Camera-Official-camera-V2-8MP-1080P30.jpg" width="250">
</p>

4. [Adafruit GPS Module](https://www.adafruit.com/product/746)

    This small GPS module can track up to 22 satellites and offers and a surprising level of precision. It also comes with a piece of header you have to solder on in order use it with a breadboard.

<p align="center">
  <img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimages.esellerpro.com%2F2457%2FI%2F31%2Fadafruit-ultimate-gps-breakout.jpg&f=1&nofb=1" width="300">
</p>

5. [TTL Serial Adapter Module USB to UART Converter](https://www.aliexpress.com/item/32774943192.html)

    This adapater allows to get the GPS data to the Raspberry Pi and to power the GPS module so there is no need to use any of the GPIO pins.

<p align="center">
  <img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimg.dxcdn.com%2Fproductimages%2Fsku_443779_1.jpg&f=1&nofb=1" width="250">
</p>

6. [4 Pins Tact Switch](https://grobotronics.com/tact-switch-6x6mm-5mm-4pins.html)

    This tiny switch is used as a trigger button for the camera.

<p align="center">
  <img src="https://grobotronics.com/images/thumbnails/350/350/detailed/1/Tact_Switch__48812_zoom.jpg" width="200">
</p>

##### This list is not final and will be updated throughout development.

## Requirements
* Python 3.7 with the following librairies :
  - picamera
  - adafruit-circuitpython-gps
  - gpsphoto
  - exifread (required by gpsphoto)
  - pillow (required by gpsphoto)
  - piexif (required by gpsphoto)
  
## Configuration

### Raspberry Pi

##### a. Operating system

##### b. Activating the camera

##### c. Installing Virtualenv

### Python Virtualenv
Using Virtualenv, you can set and activate your python environment with the following commands :
```shell
virtualenv YOUR_PATH --python=3.7
source activate YOUR_ENV/bin/activate
pip install picamera adafruit-circuitpython-gps gpsphoto exifread pillow piexif
```

# IReye
An unattended Raspberry PI 3 with webcam and Infrared remote control

### Overview
With a Raspberry PI, equipped with a loudspeaker and optionally with a HDMI screen, you can connect to it to:

issue IR commands to a TV or similar

view the USB camera connected to the PI

listen from the USB microphone connected to the PI

LIBRARIES

The uv4l software platform, with uv4l web and streaming servers run in the PI.

The lirc libray is installed on the PI. 

See the logic diagram below also.

### Prepare your Raspberry
0. I used a [Raspberry PI 3 Model B Scheda madre CPU 1.2 GHz Quad Core, 1 GB RAM](https://www.amazon.it/gp/product/B01CD5VC92/ref=oh_aui_search_detailpage?ie=UTF8&psc=1) bought at Amazon
1. Start from a clean sd: I tested 8M and 32M SD Samsung cards.
2. Install "Raspbian Stretch with Desktop" Raspbian Buster with Desktop" , I tested:
   - Buster "2019-06-20-raspbian-buster-full.img" downloaded and with "installation guide" at [Download Raspbian Stretch](https://www.raspberrypi.org/downloads/raspbian/)
   - Stretch "2017-11-29-raspbian-stretch.img"
   - Buster "2019-06-20-raspbian-buster-full.img" downloaded and with "installation guide" at [Download Raspbian Stretch]
3. (Optional, if you don't have screen, keyboard and mouse) Prepare the SD you just created for headless operations following these instructions. See also [Raspbian Stretch Headless Setup Procedure](https://www.raspberrypi.org/forums/viewtopic.php?t=191252) 

### Install the USB camera and microphone
0. I tested Logitech C525 succesfully. Simply plug it into any USB port. C525 has an integrated microphone but if yours doesn't have it, plug a USB microphone in any USB port.
1. Test your USB webcam with chromium-browser navigating to a site like [webrtc Hacks](https://webrtchacks.github.io/WebRTC-Camera-Resolution/)
2. Test your USB microphone (integrated with the webcam or not) with chromium-browser navigating to https://www.google.com and using the speech recognition 

### Install uv4l library
Install the uv4l library. For details see also [UV4L for Raspberry PI Installation Procedure](https://www.linux-projects.org/uv4l/installation/) 
 
0. Add the uv4l repository to the list of apt repositories
```
$ curl http://www.linux-projects.org/listing/uv4l_repo/lpkey.asc | sudo apt-key add -
```
1. add the following line to the file /etc/apt/sources.list:
```
$ deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/stretch stretch main
```
2. Install (or update if already installed):
```
$ sudo apt-get update
$ sudo apt-get install uv4l uv4l-server uv4l-uvc uv4l-webrtc
```
3. reboot
After rebooting, uv4l is supposed to be installed and available for next use. 

4. Test uv4l-server 
Navigate to [http://localhost:8090](http://localhost:8090)
This page should appear:

5. Click on WEBRTC
This page should appear:
 
6. Clickink on Call (the green button) the image of your camera should appear on the "remote" rectangle

### Add SSL autosigned certificate for uv4l https web server
This is mandatory for recent Google Chrome and other browsers versions.
0. Generate a selfsigned certificate
'''
$ sudo openssl genrsa -out selfsign.key 2048 && openssl req -new -x509 -key selfsign.key -out selfsign.crt -sha256
'''
1. Copy the certificate to the proper folder

1. Add the certificate to uv4l

### Screenshots

### Logic Diagram 

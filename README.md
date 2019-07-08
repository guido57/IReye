# IReye
An unattended Raspberry PI 3 with webcam and Infrared remote control

### Overview
The Raspberry PI, equipped with a loudspeaker and optionally with a HDMI screen lets you to remote connect to:
issue IR commands to a TV or similar
view and listen from the USB camera connected to the PI
The uv4l software platform, with web server runs in the PI.
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

### Install uv4l library
Install the uv4l library. See also [UV4L for Raspberryy PI Installation Procedure](https://www.linux-projects.org/uv4l/installation/) 
 
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
$ sudo apt-get install uv4l uv4l-server uv4l-uvc 
```
Now uv4l is installed and available for next use. 

### Install the USB camera and microphone
0. I tested Logitech C525 succesfully. Simply plug it into any USB port. C525 has an integrated microphone but if yours doesn't have it, plug a USB microphone in any USB port.
1. Test your USB webcam with chromium-browser navigating to a site like [webrtc Hacks](https://webrtchacks.github.io/WebRTC-Camera-Resolution/)
2. Test your USB microphone (integrated with the webcam or not) with chromium-browser navigating to https://www.google.com and using the speech recognition 
 
 
### Screenshots

### Logic Diagram 

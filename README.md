# VPS Monitor Using Raspberry Pi
This package contains scripts used for my personal server monitor.
It currently monitors performance (CPU, Memory Usage) of my Dedicated Root Server as well as Usage of several hosted Services, including Teamspeak 3 Current User Count and GameServer (MineCraft implemented) Clients Online.

If one or multiple services cannot be reached, the Server Monitor will notify you via a red LED and an error notification on display.

#### Services currently monitored:
- SSH Availability
- FTP Availability
- MySQL Availability
- Teamspeak 3 Monitor including Clients Online Status
- Minecraft Server Status
- Website Status

### Pictures:
![alt text](https://github.com/jpkunkler/raspberrypi-servermonitor/blob/master/images/monitor.png)

## Requirements
You need the following:
1. Raspberry Pi (Zero or above)
2. (WiFi / Ethernet Dongle)
3. 16x2 LCD Screen
4. The LCD Display needs to be connected via GPIO Pins. Follow the Instructions in this Video to get identical GPIO connection pattern: https://www.youtube.com/watch?v=cVdSc8VYVBM
5. The lcd.py file mentioned in the video is already included. Just make sure to get your wires correct!

#### Install requirements via pip
pip install -f requirements.txt

#### ADDITIONAL: Manual Installation necessary:
The following two packages are necessary for this package to run!
##### Python-Ts3
Follow installation instructions on  https://github.com/nikdoof/python-ts3


##### MySQLDB
apt-get install python-mysqldb

## Installation

1. After installing the above requirements, open config.py file and adjust settings to your server instances.
2. Once you are done, create a Cronjob to run every 5 minutes (recommended).
3. Optional: create a cronjob to run backlight_off.py some time in the evening/at night if you want the display to shut down.
4. To manually switch the backlight on and off, use backlight_switch.py script.

You can also connect additional tactile buttons to your Pi via GPIO and set those buttons to run:
- update_switch.py to manually update your status monitor
- backlight_switch.py to turn on/off the lcd backlight

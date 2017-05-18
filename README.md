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
pip install -f requirements.txt

#### Manual Installation necessary:
The following two packages are necessary for this package to run!
##### Python-Ts3
Follow installation instructions on  https://github.com/nikdoof/python-ts3


##### MySQLDB
apt-get install python-mysqldb

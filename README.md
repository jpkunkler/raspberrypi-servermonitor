# raspberrypi-servermonitor
This package contains scripts used for my personal server monitor.
It currently monitors performance (CPU, Memory Usage) of my Dedicated Root Server as well as Usage of several hosted Services, including Teamspeak 3 Current User Count and GameServer (MineCraft implemented) Clients Online.

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

from mc import mcStatus, mcPlayers
from ssh import sshStatus, RamFree, cpuUsage
from ftp import ftpStatus
from ts3_status import ts3Status, ts3Clients
from mail import mailStatus
from mysql import mysqlStatus
from website import websiteStatus
import RPi.GPIO as GPIO
from datetime import datetime
from config import * 
import lcd

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

backlight = 23
red = 18

# setup GPIO pins
GPIO.setup(red, GPIO.OUT)
GPIO.setup(backlight, GPIO.OUT)

#Get current time
time_now = datetime.now().strftime('%H:%M')

# initialize LCD screen
lcd.lcd_init()
lcd.lcd_string('Updating...', lcd.LCD_LINE_1, 2)

# check status
mc = mcStatus(MC_PORTS) #Add Ports as list
mc_players = mcPlayers(MC_PORTS)
ssh = sshStatus(SSH_USER, SSH_PW)#Checks if SSH is available
ram_free = round(100.00 - RamFree(SSH_USER, SSH_PW), 1)
cpu_usage = round(cpuUsage(SSH_USER, SSH_PW), 1)
ftp = ftpStatus(SSH_USER, SSH_PW) #Checks if FTP is available
ts3 = ts3Status() #Checks if all teamspeak servers are online
ts3_clients = ts3Clients()
website = websiteStatus(WEBSITE_URL) #Checks if triscle.de is available
db = mysqlStatus(DB_USER, DB_PW)
smtp = mailStatus()

if all([mc, ssh, ftp, ts3, website, db, smtp]):
    lcd.lcd_string('TS3: %s   GS: %s' % (ts3_clients, mc_players), lcd.LCD_LINE_1, 2)
    lcd.lcd_string('M:{}% C:{}%'.format(ram_free, cpu_usage), lcd.LCD_LINE_2, 2)
    GPIO.output(red, 0)
else:
    GPIO.output(red, 1)

if not ts3:
    lcd.lcd_string('Error', lcd.LCD_LINE_1, 2)
    lcd.lcd_string('TS3 Server', lcd.LCD_LINE_2, 2)

if not website:
    lcd.lcd_string('Error', lcd.LCD_LINE_1, 2)
    lcd.lcd_string('Website', lcd.LCD_LINE_2, 2)
    
if not ssh:
    lcd.lcd_string('Error', lcd.LCD_LINE_1, 2)
    lcd.lcd_string('SSH', lcd.LCD_LINE_2, 2)

if not ftp:
    lcd.lcd_string('Error', lcd.LCD_LINE_1, 2)
    lcd.lcd_string('FTP', lcd.LCD_LINE_2, 2)

if not mc:
    lcd.lcd_string('Error', lcd.LCD_LINE_1, 2)
    lcd.lcd_string('Minecraft', lcd.LCD_LINE_2, 2)

if not db:
    lcd.lcd_string('Error', lcd.LCD_LINE_1, 2)
    lcd.lcd_string('MySQL DB', lcd.LCD_LINE_2, 2)

if not smtp:
    lcd.lcd_string('Error', lcd.LCD_LINE_1, 2)
    lcd.lcd_string('Mail Server', lcd.LCD_LINE_2, 2)

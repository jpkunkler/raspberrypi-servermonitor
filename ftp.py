import ftplib
from config import FTP_HOST

def ftpStatus(user, pw):
    try:
        ftp = ftplib.FTP(FTP_HOST, user, pw, timeout=10)
    except:
        return False
    else:
        return True
        ftp.quit()

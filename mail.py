from smtplib import SMTP
from config import SMTP_HOST

def mailStatus():
    try:
        smtp = SMTP(SMTP_HOST)
    except:
        return False
    else:
        return True

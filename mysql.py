import MySQLdb as mdb
from config import HOSTNAME

def mysqlStatus(user, pw):
    try:
        con = mdb.connect(HOSTNAME, user, pw)
    except:
        return False
    else:
        con.close()
        return True

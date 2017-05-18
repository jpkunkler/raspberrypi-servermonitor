import urllib

def websiteStatus(url):
    try:
        status = urllib.urlopen(url).getcode()
        if status == 200:
            return True
        else:
            return False
    except:
        print 'Error'
        return False

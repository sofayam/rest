import urllib2
import time
from datetime import datetime

def logit(text):
    print str(datetime.now()) + " " + text

online = 100

def setOnline(fl):
    global online
    if (online != fl):
        online = fl
        logit({True : "on", False: "off"}[online])

while True:
    try:
        response = urllib2.urlopen('http://piwifi:8000')
        #logit(response.read())
        setOnline(True)
    except:
        #logit("failed")
        setOnline(False)
    time.sleep(10)

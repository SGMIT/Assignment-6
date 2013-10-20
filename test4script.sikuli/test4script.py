import shutil
import os.path
import datetime

filePath = "/Users/stacy/Documents/weltec/Year2/IT6280/A6/"

logfile = open(filePath+str(datetime.date.today()) + "TC4Log.txt", 'w+')

switchApp("safari")

find("1382248253241.png")
click("1382248253241.png")
click("1382234980048.png")
click("1382246298675.png")
click("1382234016042.png")
click("1382234060035.png")

picture = "test4.png"
screenGrab = Screen()
test = screenGrab.capture(0,0,1650,800)

shutil.move(test,os.path.join(filePath, picture))
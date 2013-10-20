import shutil
import os.path
import datetime

filePath = "/Users/stacy/Documents/weltec/Year2/IT6280/A6/"

logfile = open(filePath+str(datetime.date.today()) + "TC9Log.txt", 'w+')

switchApp("safari")

find("1382248253241.png")
click("1382248253241.png")
click("1382247691408.png")
click("1382247714178.png")
picture = "test9a.png"
screenGrab = Screen()
test = screenGrab.capture(0,0,1650,800)

shutil.move(test,os.path.join(filePath, picture))
click("1382247714178.png")

picture = "test9b.png"
screenGrab = Screen()
test = screenGrab.capture(0,0,1650,800)

shutil.move(test,os.path.join(filePath, picture))
import shutil
import os.path
import datetime

filePath = "/Users/stacy/Documents/weltec/Year2/IT6280/A6/"

logfile = open(filePath+str(datetime.date.today()) + "TC8Log.txt", 'w+')

switchApp("safari")

find("1382248253241.png")
click("1382248253241.png")
click("1382248777511.png")
click("1382247714178.png")

picture = "test8.png"
screenGrab = Screen()
test = screenGrab.capture(0,0,1650,800)

shutil.move(test,os.path.join(filePath, picture))
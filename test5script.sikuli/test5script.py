import shutil
import os.path
import datetime

filePath = "/Users/stacy/Documents/weltec/Year2/IT6280/A6/"

logfile = open(filePath+str(datetime.date.today()) + "TC5Log.txt", 'w+')

switchApp("safari")

find("1382248253241.png")
click("1382248253241.png")
click("1382246544937.png")
click("1382246601300.png")
click("1382246619275.png")
click("1382246657629.png")
click("1382246667428.png")
click("1382246676841.png")

picture = "test5a.png"
screenGrab = Screen()
test = screenGrab.capture(0,0,1650,800)

shutil.move(test,os.path.join(filePath, picture))

click("1382246730834.png")
picture = "test5b.png"
screenGrab = Screen()
test = screenGrab.capture(0,0,1650,800)

shutil.move(test,os.path.join(filePath, picture))

click("1382246778415.png")
click("1382246799738.png")
click("1382246812641.png")
picture = "test5c.png"
screenGrab = Screen()
test = screenGrab.capture(0,0,1650,800)

shutil.move(test,os.path.join(filePath, picture))
import shutil
import os.path
import datetime

filePath = "/Users/stacy/Documents/weltec/Year2/IT6280/A6/"

logfile = open(filePath+str(datetime.date.today()) + "TC9Log.txt", 'w+')

switchApp("safari")

hover("1382251897964.png")
picture = "test10a.png"
screenGrab = Screen()
test = screenGrab.capture(0,0,1650,800)

shutil.move(test,os.path.join(filePath, picture))
hover("1382251936198.png")

picture = "test10b.png"
screenGrab = Screen()
test = screenGrab.capture(0,0,1650,800)

shutil.move(test,os.path.join(filePath, picture))
import shutil
import os.path
import datetime

filePath = "/Users/stacy/Documents/weltec/Year2/IT6280/A6/"

logfile = open(filePath+str(datetime.date.today()) + "TC7Log.txt", 'w+')

switchApp("safari")

find("1382248253241.png")
click("1382248253241.png")
click("1382247429545.png")
click("1382247453712.png")
click("1382247429545.png")
click("1382247461872.png")
click("1382247429545.png")

picture = "test7.png"
screenGrab = Screen()
test = screenGrab.capture(0,0,1650,800)

shutil.move(test,os.path.join(filePath, picture))
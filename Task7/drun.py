#!  /usr/bin/python3

import cgi
import subprocess


print()

mydata  = cgi.FieldStorage()

osname  = mydata.getvalue("osname")
imagename = mydata.getvalue("imagename")

cmd = subprocess.getoutput("sudo docker run -dit --name {} {}".format(osname , imagename ))


print(cmd)


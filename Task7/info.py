#!  /usr/bin/python3

import cgi
import subprocess


print()

mydata  = cgi.FieldStorage()

info  = mydata.getvalue("info")


cmd = subprocess.getoutput("sudo "+ info)


print(cmd)


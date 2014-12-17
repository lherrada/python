#!/usr/bin/python
import os

url=' google.com'
command='/usr/bin/curl' + url 
os.execl(command)



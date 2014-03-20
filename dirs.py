#!/usr/bin/python

import shutil
import re
import os

for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
	line = os.path.join(root, name) 
	matchObj = re.match( r'.*/node_modules/[^/\.]*?$', line, re.M|re.I)
	if matchObj:
		if (line.count("node_modules") > 1):
			print matchObj.group()
			shutil.move(line,'./node_modules')

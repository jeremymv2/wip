#!/usr/bin/python

import shutil
import re
import os

wheretostart="./node_modules/grunt-cli/node_modules"

for root, dirs, files in os.walk(wheretostart, topdown=False):
    for name in dirs:
	line = os.path.join(root, name) 
	matchObj = re.match( r'.*/node_modules/[^/\.]*?$', line, re.M|re.I)
	if matchObj:
		if (line.count("node_modules") > 2):
			print "Moving: " + matchObj.group()
			shutil.move(line,wheretostart)

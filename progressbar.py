#!/usr/bin/python3
# Output example: [=======   ] 75%
# Progressbar

import sys
import time
import math
 
# width defines bar width
# percent defines current percentage
def progress(width, percent):
    marks = math.floor(width * (percent / 100.0))
    spaces = math.floor(width - marks) 
    loader = '[' + ('=' * int(marks)) + (' ' * int(spaces)) + ']'
 
    sys.stdout.write("%s %d%%\r" % (loader, percent))
    if percent >= 100:
        sys.stdout.write("\n")
    sys.stdout.flush()
 
# simulate a process
for i in range(100):
    progress(50, (i + 1)) # +1
    time.sleep(0.1) # Slow down for demo
    

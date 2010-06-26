#!/usr/bin/env python
# Are we not men?
# 2010. Jrabbit. GPL v3 or later.
#Support only offered for Lolcat linux
import time
start = time.time()
print "Gee Brain, What do you want to do today?"
print "Same thing we do every day, Pinky -- try to take over the world!"
z = raw_input("Do you dare accept the challenge? y/n")
if z != "yes" or z != "y":
    print "Go on... "
    raw_input("This prompt does nothing.")
raw_input("This prompt might do nothing.")
raw_input("This prompt ?????????????????")
elapsed = (time.time() - start)
print "we just wasted " + str(elapsed) + " seconds"
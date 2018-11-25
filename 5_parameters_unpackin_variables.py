# Terminal, 'argv' & Raw Input ————————————————————————————————————————————————>
# The 'argv' is the "argument variable", this variable holds...
# the arguments you pass to your Python script when you run it.
# the features are technically called 'modules'.
from sys import argv


# Unpacks 'argv' so that, the 4 arguments get assigned to four variables.
# Take whatever is in 'argv', unpack it, and assign it...
# to all these variables on the left in order.
script, first, second, third = argv

# My variables:
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


print "Your fourth variable is:",
fourth = raw_input()
print "Your fifth variable is:",
fourth = raw_input()

# !!!TO RUN THIS ENTIRE THING USE TERMINAL!!!
# Run in [>_] Terminal like this:
# Ex13.py jan dick harry
# Script, first var. second var. third var.

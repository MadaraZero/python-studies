# use in [>_] Terminal ————————————————————————————————————————————————————————>
from sys import argv

script, user_name, surname = argv
prompt = '> '

print "Hi %s %s I'm the %s script." % (user_name, surname, script)
print "I'd like you to ask a few questions."
print "Do you like me %s %s" % (user_name, surname)
likes = raw_input(prompt)
print "-------------------------------------------"

print "Where do you live %s %s?" % (user_name, surname)
lives = raw_input(prompt)
print "-------------------------------------------"

print "What kind of computer do you have?"
computer = raw_input(prompt)
print "-------------------------------------------"

print "Do you want to attack me %s %s?" % (user_name, surname)
attack = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
However, you want to %r me...
""" % (likes, lives, computer, attack)

# Run in [>_] Terminal like this:
# Ex14.py Denis

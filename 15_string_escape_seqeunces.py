# String Escape Seqeunces ---------------------------------------------------->

# \\ used when you want to use '\' in a sentence.
print "10 \\ 5 = 2 \n"

# \' used when you want to use the single quote in a string i.e. display to user.
# this is so you avoid breaking the string since strings are categorized by either
# double quotes or single quotes.
print 'Hello, I\'m a python snake\n'

# \" same as \' but then for double quotes.
print "I remember John said:\"watch out!\"\n"

# a way to be conservative with this specific escape seqeunce is to combine
# double quotes with single-quotes or vice-versa:
print 'I remember John said:"watch out!"\n'

# \a this is used when you want an old computer to express an alert sound.
# \a > Hardware Interaction
print "a\\ > One two three \afour five\n"

# b\ connects words togheter.
print "b\\ > One two three \bour five\n"

# \f It forces the printer to eject the current page and to continue printing
# at the top of another.
# \f > Hardware Interaction
print "f\\ > One two three \ffour five\n"

# \n is used for printing a blank line before the next line gets printed
# mainly used for better overview in interpreter.
print "n\\ > One two three four five\n"

# \r used for hiding words behind/before the escape seqeunce \r
print "One two three \r <r\\ four five\n"

# \t used for making a horizontal tab on the x-axis
print " \t t\\ > One two three four five\n"

# \v used for vertical tab when applicable.
print "v\\ > One two three \vfour five\n"

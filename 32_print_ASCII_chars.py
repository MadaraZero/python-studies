import sys

mytext = u""
mytext += unichr(916) #check the codes for unicode chars here:
                      # http://en.wikipedia.org/wiki/List_of_Unicode_characters

# print mytext.encode(sys.stdout.encoding, errors="replace")

print 5 * unichr(916)

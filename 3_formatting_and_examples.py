# Formatters ——————————————————————————————————————————————————————————————————>
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print "Let's talk about %r." % name
print "He's %d inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth


# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % \
(age, height, weight, age + height + weight)


one_inch = 2.54
one_pound = 0.45


# inch to centimeter converter
inches = 230
# pounds to kilos converter
pounds = 150


# Conversion practice —————————————————————————————————————————————————————————>
# litle practice with converting inches and pounds to
# centimeters and kilos through the use of variables.
print "--------------------------------------------"
print
print "Conversion of %d inches and %d pounds:" % (inches, pounds)
print
print "%d pounds is..." % inches, one_inch * inches
print "%d centimeters is..." % pounds, one_pound * pounds
print
print "--------------------------------------------"


# Formatting exersises ————————————————————————————————————————————————————————>
# the variable x is a string with a number formatted into it.
x = "There are %d types of people." % 10
# the variable binary is a string.
binary = "binary"
# the variable do_not is a string.
do_not = "don't"
# the variable y is a string with two variables formatted in it.
y = "Those who know %s and those who %s." %(binary, do_not)


# prints the variable x to the console.
print x
# prints the variable y to the console.
print y


# prints the string with the variable x formatted into it.
print "I said %r." % x

# prints the string with the variable y formatted into it.
print "I also said: '%s'." % y


# the variable 'hilarious' is False.
hilarious = False
# the variable joke_evalution is a string with the variable
# hilarious formatted into it by %r.
joke_evaluation = "Isn't that joke so funny?! %r"


# prints the string of joke_evaluation with the variable hilarious...
# formatted into it by using the '%r'.
print joke_evaluation % hilarious


# the variable 'w' is a string.
w = "This is the left side of... "
# the variable 'e' is a string.
e = "a string with a right side."


# prints the variable 'w' which is a string and the variable 'e'...
# which is also a string producing a long string.
print w + e


# More formatting —————————————————————————————————————————————————————————————>
# displays the string below to the console.
print "Mary had a little lamb."
# displays the string below to the console with...
# the string 'snow' formatted into it by '%s'.
print "Its fleece was white as %s." % 'snow'
# displays the string below to the console.
print "And everywhere that Mary went."
# displays the result of multiplying the string '.' by 10.
print "." * 10 # what'd that do?


# a column of variables with an alphabetical character.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"


# watch that coma at the end. try removing it to see what happens.
# 'comma' changes how the print displays on to console
print end1 + end2 + end3 + end4 + end5 + end6,
# displays the concatenation of the previous variables.
print end7 + end8 + end9 + end10 + end11 + end12


# More formatting —————————————————————————————————————————————————————————————>
# when using '%r' to format the a string with double-quotes...
# e.g. "Hello World" might be printed with single-quotes...
# 'Hello World' because %r is for debuggin so los of elegancy...
# is acceptable.
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)


# Moreee formatting ———————————————————————————————————————————————————————————>
# here's some new strange stuff, remember type it exactly.


# the variable 'days' contain a string.
days = "Mon Tue Wed Thu Fri Sat Sun"
# the variable 'months' contains a string...
# the '\nString' notation prints the string into a list format.
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"


# displays the sring in the console with the string...
# contained by the days variable.
print "Here are the days", days
print "Here are the months: ", months


# The three double-quotes allow for long strings.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""


# String Formatting ———————————————————————————————————————————————————————————>
# the '\t' notation tabs in the string i.e. moves it to the right.
tabby_cat = "\tI'm tabbed in."
# the '\n' notation makes the string continue on the next line.
persian_cat = "I'm split\non a line."
# the '\\' allows for the backlash character in string.
backlslash_cat = "I'm\\ a \\ cat."


# A variable that contains a list that is tabbed by '\t'.
fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""


print tabby_cat
print persian_cat
print backlslash_cat
print fat_cat


# Escape Seqeunces
# \\ = Backslash (\)
# allows for the backlash character to be used in a string.
print "Black \\ White."


# \' = Single- quote (')
# Allows to use single-quotes inside a string.
print 'Let me \'test\' the single quote.'


# \" = Double- quote (")
# Allows to use double quotes inside a string.
print "Just \"testing\" the double quotes."


# \a = ASCII bell (BEL)
# '\a' Seems like a 'space' mechanism...
print "I have no \aclue what it does."


# \b = ASCII backspace (BS)
# '\b' Seems like 'backspace' mechanism.
print "Neither for \bthis one."


# \f = ASCII formfeed (FF)
# '\f' Creates more space...
print "And, also not for \fthis one."


# \n = ASCII linefeed (LF)
# '\n' makes the string continue on the next line.
print "LOL LOL \nLOL LOL"


# \N{name} = Character named name in the Unicode database (Unicode only)
# ... doesn't work more research required.
print "Ein, zwei, drei \N{Denis} Go!"


# \r = ASCII carriage return (CR)
# '\r' deletes part of the string before the '\r' notation.
print "Well, I \rsuppose you don't come around here much?"


# \t = ASCII horizontal tab (TAB)
# '\t' makes a string indent to the right.
print "...This string indented."


# \uxxxx = Character with 16- bit hex value xxxx (Unicode only)
# ... doesn't work more research required.
print "Lol... wuuuuut \uxxxxweird escape seqeunce notation."


# \Uxxxxxxxx = Character with 32- bit hex value xxxxxxxx (Unicode only)
# ... doesn't work more research required.
print "Doesn't seem to \Uxxxxxxxxwork."


# \v = ASCII vertical tab (VT)
# '\v' makes a string indent to the left!
print "Oeh! a vertical \vtab!!!"


# \ooo = Character with octal value oo
# ... doesn't work more research required.
print "I have no \oooclue about what this does."


# \xhh = Character with hex value hh
# ... doesn't work more research required.
print "Righhhhhttt a Value"


# interesting code that makes the console display the list...
# in seqeunce while on repeat!
while True:
    for i in ["Welcome...", "To!", "Zoo...", "TOPIA", "!!!!"]:
        print "%s\r" % i,

def cool_prompt():
	while keyboard != keyboard.is_pressed(keyboard):
		for i in ["|", "|", "|", " ", " ", " "]:
			print "%s\r" % i,
	else:
		start = raw_input('> ')

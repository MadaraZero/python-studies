# String Formats ------------------------------------------------------------->

# %d formatting is used for displaying integers
print "This is a number ... %d" % 5

# %i formatting is used for displaying integers
print "This is a number ...  %i" % 6.5

# %o formatting is used for displaying unsigned octal
print "This is an octal ... %o" % 64

# %u formatting is used for displaying unsigned decimal integers
print "This is an unsigned integer ... %u" % 1234

# %x formatting is used for unsigned hexadecimal
print "Hexadecimal bro ... %x" % 333

# %X formatting is used for is used for unisgned Hexadecimal uppercase
print "Hexadecimal upper case ... %X" % 333

# %e formatting is used for floating point exponential
print "Floating point exponential ... %e" % 3

# %E formatting is used for floating point exponent Upper case
print "Floating point Uppercase exponential ... %E" % 3

# %f formatting is used for floating point decimal
print "Floating Point decimal ... %f" % 123

# %F formatting is used for Upper case floating point decimal
print "Floating Point decimal Uppercase ... %F" % 123

# %g formatting is same as '%e'...
print "Some type of exponent ... %e" % -10

# %G formatting is same as '%E'...
print "Some type of exponent ... %E" % -11

# %c formatting is used for single character int. or str. (Doesn't work properly on the int. type)
print "int single char %c ... and str single char %c" % (7, "H")

# %r formatting is used for displaying raw data
print "raw data string %r and raw data integer %r" % ('Hello', 565657)

# %s formatting is used for displaying strings
print "I like %s a lot!" % 'cats'

# %% formatting is used for.... (Don' tknow how to use properly)
print "Let's test this then %  result." % 4

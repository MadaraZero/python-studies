# Data Types ----------------------------------------------------------------->

# True and False are boolean operators.
harry = True
if harry == True:
    print 5 + 5

# None is as the name suggest nothing. You could also see it as an empty box
# that may be used to store data at a later point.

basket = None

if basket == None:
    basket = "5 apples" # filling the box
    print "the basket has now %s." % basket

    basket = None # emptying the box
    print "the basket has now %s" % basket

# Strings are sentences constructed out of alphabetical characters or
# other types of characters as long as they are categorized as strings.

print "I am a string." # < this is a string.
print "1, 2, 3, 4,...,99" # < these numbers are also strings because they are
# categorized as such by " "

# Numbers are just whole integers that can be positive or negative.
print "this is a number > ", 9999 # < this is a number data type.
print "this is a string >  9999" # < this is not a number but a string data type.

# floats are decimal numbers. For instance, if you divide 7 by 2, you won't
# 3.5 because python only recognizes decimal numbers if you indicate a number
# as a float. So, the answer will be 3 rounded down.
print 7 / 2
print 7 / 2,'r', 7 % 2 # and its remainder.
print 7.0 / 2

# here is a remainder calculator.
def remainder_calc(a, b):
    whole_number = 0
    remainder = 0

    whole_number += a / b
    remainder += a % b

    print "%d r%d" % (whole_number, remainder)

remainder_calc(4023, 23)

# lists are not really data types but abstract data types which is not about
# the content of the data but the form of the data. In this case a list
# is simply an abstract data type that puts bits of data in row that can be
# visualized from left to right or vice-versa. An analogy would be
# a special type of box that can only contain objects on the x axis.

# notice how the list contains all kinds of data types put in by the user.
a_list = ['apple', 'banana', 500, True, 'orange', [1, 2, 3]]

# Operators ------------------------------------------------------------------>

# + for addition
print "(+) 5 + 5 = %d" % (5 + 5)

# - for subtraction
print "(-) 10 - 4 = %d" % (10 - 4)

# * for multiplication
print "(*) 10 x 5 = %d" % (10 * 5)

# ** raise to the power of the second n
print "(**) 8^3 = %d" % 8**3

# / for division
print "(/) 15 / 3 = %d" % (15 / 3)

# // for floor division (Rounds number to the lowest number possible)
print "(//) 10 // 4 = %d" % (10 // 4)

# % modulo operator for remainder
print "(%) 25 % 4 =", 25 % 4

# < less than
print "(<) 3 < 4 =", 3 < 4

# > greater than
print "(>) 5 > 4 =", 5 > 4

# <= less than or equal
print "(<=) 5 <= 5 =", 5 <= 5
print "(<=) 4 <= 5 =", 4 <= 5

# >= greater than or equal
print "(>=) 10 >= 10 =", 10 >= 10
print "(>=) 10 >= 5 =", 10 >= 5

# == equal to
print "(==) 5 == 5 =", 5 == 5
print "(==) 'str' == 'str' =", 'str' == 'str'

# != not equal to
print "(!=) 4 != 5 =", 4 != 5
print "(!=) 'b' != 'a' =", 'b' != 'a'

# <> not equal to same as !=
print "(<>) 5 <> 4 =", 5 <> 4

# () used for tuples and arguments
print "(()) used for tuples:"
tup_1 = (1, 2, 3); print tup_1

# [] for lists
print "([]) used for lists:"
lst = [1, 2, 3, 4, 5, 6, 7,'...',99]
print lst

# {} for dictionaries
print "({}) used for dictionaries:"
dict = {
    1 : 'First Place',
    2 : 'Second Place',
    3 : 'Third Place'
}
print dict[2]

# . well that is a dot -_-
print "(.) used for calling methods:"
lst = ['One', 'Two']; print "_".join(lst)

# , this is a comma duh...
print "(,) used for separating:"
print "Look a fucking comma ,,,,,,,,,"


# : used for creating code blocks
print "(:) used for creating code blocks:"
print """
def function():
    if a == b:
    do something!
    return something

"""

# = contains or is
box = 'shoes'
print "(=) box = %s" % box

# ; can be used for multiple statements on a line
print "(;) var_a = 1234; print var_a"
var_a = 1234; print var_a

# += update variable by addition and retain the update
print "(+=)"
var_1 = 100
print var_1, "< original var."
var_1 += 50
print var_1, "< updated var. with addition"

# -= update variable by subtracting and retain update
print "(-=)"
var_1 = 100
print var_1, "< original var."
var_1 -= 50
print var_1, "< updated var. with subtraction"

# *= update variable by multiplication and retain update
print "(*=)"
var_1 = 100
print var_1, "< original var."
var_1 *= 4
print var_1, "< updated var. with multiplication"

# /= update variable by division and retain update
print "(/=)"
var_1 = 100
print var_1, "< original var."
var_1 /= 2
print var_1, "< updated var. with division"

# //= update variable by floor division and retain update
print "(//=)"
var_1 = 10
print var_1, "< original var."
var_1 //= 4
print var_1, "< updated var. with floor division"

# %= update variable by modulo operator and retain update
print "(%=)"
var_1 = 25
print var_1, "< original var."
var_1 %= 4
print var_1, "< updated vars. with modulo operator"

# **= update variable by raising power to the second n
print "(**=)"
var_1 = 8
print var_1, "< original var."
var_1 **= 3
print var_1, "< updated var. with raising power"

# @ Decorator. (Don't quite undertand how this works... yet)
print "(@)"
print "Brah...!"

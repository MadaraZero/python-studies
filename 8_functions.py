# Writing A Function ——————————————————————————————————————————————————————————>
# This one is like your scripts with argv...
#  - IMPORTANT POINT def print_two(*args):
#  - (*args) lets decide how many arguments you can use!!!
#  - example: arg1, arg2, arg3 = args, just like the 'argv' method.


def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1


# this one takes no arguments
def print_none():
    print "I got nothing on u, brah"

print
print_two("Denis", "Matei")
print_two_again("Deniss", "Mateii")
print_one("Ferst!")
print_none()


# Integer Checker —————————————————————————————————————————————————————————————>
# Code that checks whether input is an integer (nothing more; or less)
def check_int(number):
	try:
		int(number)
	except ValueError:
		return False
		# print number
	else:
		return True
		print raw_input()


def testing_for_int():
	val = raw_input(">>> ")
	try:
		int(val)
	except ValueError:
		print "That is not a number"
		testing_for_int()
	else:
		print "%s is an integer." % val
		testing_for_int()


def selection():
	gold = check_int(raw_input(">>> "))
	# gold = raw_input(">>> ")
	# check_int(gold)
	if gold == True:
		print "That is a number %d" % gold
	else:
		print "NO NUMBER"


selection()
# check_int()

# First class Functions ———————————————————————————————————————————————————————>
# function that produces as result a square of a number called x
def square(x):
    return x * x

# function that produces as result the cube of a number called x.
def cube(x):
    return x * x * x

# a function that takes 'a function' and 'a list of arguments' as arguments.
def my_map(func, arg_list):
    result = []                   # result is an empty list
    for i in arg_list:            # for item in the arg_list...
        result.append(func(i))    # append the output of item from 'func'
    return result                 # return list that contains the results of
                                  # the application of 'func'.

# a variable that contains a function
# square is the first argument of my_map function
# [1, 2, 3, 4, 5] is the second argument of my_map function
squares = my_map(cube, [1, 2, 3, 4, 5])

# displays the variable that contains the function and its results
print(squares)


# Closure Functions ———————————————————————————————————————————————————————————>
# a function that takes as argument a string and that has a function within it
def logger(msg):

    def log_message():        # a function within a function
        print 'Log:', msg     # prints the argument used in the first function
                              #
    return log_message        # returns itself i.e. the function log_message


# a variable containing a function with an argument 'Hi'.
log_hi = logger('Hi!')
# the variable now can be used to call a function by adding curly brackets '()'
# "variable function" produces Log: Hi!
log_hi()


# closure function_b:
#a function that takes one argument a tag
def html_tag(tag):

    # a function within the function that takes as argument 'msg' which is a string
    def wrap_text(msg):                            #———————————————————————————>
        print('<{0}>{1}</{0}>'.format(tag, msg))   # a method <format>         >
                                                   # I am not familiar with.   >
                                                   #———————————————————————————>
    return wrap_text  # returns the result of the wrap_text function


# a variable containing the html_tag function that contains an argument tag
print_h1 = html_tag('h1')
# the variable has become a function, now you can apply the second function
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')


# closure function_c:
# a closure is an inner function that remembers and has acces to variables
# in the local scope in which it was created even after the outer function
# has finished executing.
def outer_func(msg):
    # a variable 'message' as 'msg' in the outer_func.
    message = msg

    # start of inner function
    def inner_func():
        print(message)#<-------- a closer closes of the free variable <-----.
                               # in its environment.                        |
                               # in this case 'message' as free var.        |
    return inner_func          # returns the data of the closer             |
                               #                                            |
# a variable defined as the out function with the argument 'Hi' .-----------^
hi_func = outer_func('Hi') # -----------------------------------^           |
# a variable defined as the out function with the argument 'Hello'          |
hello_func = outer_func('Hello') # -----------------------------------------^

# the function variable executes the outer_func('Hi')
hi_func()      # Executes: < outer_func('Hi') >
hello_func()   # Executes: < outer_func('Hllo') >

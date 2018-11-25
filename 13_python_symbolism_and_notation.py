# Index of Python Notation and Terminology:
import sys

global_mate = 1

def and_():
    """'and' is a boolean operator that verifies whether two requirements
    are met."""
    one = 1 # tweak variables to change result.
    two = 2
    if one == 1 and two == 2:
        print ">>> and\n"
    else:
        print ">>> not and\n"
and_()

def del_():
    """ 'del' means to delete and is used in lists to delete values."""
    lst = ["ape", "dog", "penguin"]
    del lst[0] # deletes value at index 0 which is "ape
    print lst
del_()

def from_():
    "from is used for importing specific functions from modules for example:"
    from termcolor import colored
    print "* from\n"
from_()

def not_():
    "not is a boolean operator that returns the opposite value"
    print not True
not_()

def while_():
    "while is used for generating loops that run until a condition is not met."
    a_lst = []
    writing = None
    while writing != "stop":
        writing = raw_input('> ')
        print writing
        a_lst.append(writing)
        print
#while_()

def as_():
    """as can be used to rename methods from modules for example:"""
    from termcolor import colored as c
    print c("Hello World", 'green')
    new_lst = ["code", "boi"]
as_()

def elif_():
    """elif is basically 'the next if statement' that comes after 'the previous
    if statement' if 'the previous if statement' was not satisfied."""
    money = "$45"
    if money == "$50":
        print "* 50"

    elif money == "$45":
        print "* 45"
elif_()

def global_():
    """global variables are top level variables and accesible by any python
    function."""
    global global_mate
    if global_mate == 1:
        global_mate += 5
        print "* global"
        print global_mate
global_()

def or_():
    """or is a boolean operator indicating to run a piece of script when the
    case is T or F, T or T, F or T. """
    var_1 = 1
    var_2 = 2
    if var_1 == 3 or var_2 == 2:
        print "* I am the 'or_' function :)"
    else:
        print "* or failed."
or_()

def with_():
    """with > when you have two related operations which you'd like to execute
        as a pair, with a block of code in between."""
    with open('output.txt', 'w') as f:
        f.write('Hi there!!!!!!!!!!!!')
        print "* with statement completed"
with_()

def assert_(a, b):
    """ Python's assert statement is a debugging aid that tests a condition.
    If the condition is true, it does nothing and your program just continues
    to execute. But if the assert condition evaluates to false, it raises an
    AssertionError exception with an optional error message."""
    # function that can only add numbers equal or lower than 15.
    result = a + b
    assert a <= 15; assert b <= 15
    return result
print assert_(15, 15)

def else_():
    """else just expresses the piece of code if the condition from the if
    statement results to false."""
    testing = 2
    if testing == 1:
        print "condition met"
    else:
        print "condition NOT met."
else_()

def if_():
    """if puts a condition on whether a piece of code should run. The 'if'
    statement works similar to daily language. For example: 'buy me a
    chocolate bar if the store is open.' Therefore, if the store is not
    open do not buy chocolate bar. Simple as that..."""
    store = "open"
    if store == "open":
        print "I will buy you a piece of chocolate."
    else:
        print "I will break in the store, and get you a piece of chocolate " \
              "anyway"
if_()

def pass_():
    """pass is a place holder for code that you want to add in the future
    you can't leave empty lines or the interpreter will complain."""
    print "Would you go into room 1 or room 2?"
    answer = raw_input('> ')
    if answer == "1":
        print "YOU WIN!"
    elif answer == "2":
        pass
#pass_()

def generator_():
    """yield is like function that temporarily conserves a variable. hand to
    to use in generators."""

    def search(keyword, filename):
        """yield temporarily conserves a bit of data. yield is useful when you
        build generators. """
        print('generator started')
        f = open(filename, 'r')
        # Looping through the file line by line
        for line in f:
            if keyword in line:
                # If keyword found, return it
                yield line
        f.close()

    the_generator = search("LLEN", 'test2.txt')
    print(the_generator.next()) # 'yield' statement used for generator.
generator_()

def break_():
    """break will stop a 'for loop'."""
    for number in range(0, 8):
        if number != 6:
            print "I hate the number %d!!!" % number
        else:
            print "Used Break.\n"
            break
break_()

def continue_():
    """continue skips a line and continues on the next one."""
    for number in range(0, 8):
        if number != 6:
            print "I am not going to skip the number %d!!!" % number
        else:
            print "I will skip the number %d..." % number
            continue
continue_()

def try_except_finally():
    # specific exception at the top.
    # general exceptions below.

    try:
        f = open('test.txt')
    except IOError as error_name:  # file not found error
        # print 'Sorry. This file does not exist.'
        print(error_name)
    except Exception as error_name:
        # print 'Sorry. Something went wrong.'
        print(error_name)
    else:
        print(f.read())
        f.close()
    finally:
        print "Executing Finally..."

    print "-" * 56

    try:
        f = open('test2.txt')
        if f.name == 'test2.txt':
            raise Exception # can be used to raise your own error.

    except IOError as error_name:  # file not found error
        print(error_name)

    except Exception as error_name:
        print 'Error!'

    else:
        print(f.read())
        f.close()

    finally:
        print "Executing Finally..."
try_except_finally()

def import_():
    """import is used to import modules, also used together with from x
    import y, to import only one method from the module. Rather than the
    entire module."""
    import webbrowser
    print "webbrowser imported\n"
    from termcolor import colored
    print "color from termcolor imported\n"
import_()

def raise_():
    """raise can be used to create your own types of errors."""
    bad_variable = 5
    if bad_variable == 5:
        raise Exception('> Variable Contains int 5 <')
# raise_() # piece of code raises our own error, thus, it is commented out.

def print_():
    """print is used for displaying data in the Terminal most common
    data is 'strings'."""
    print "I am a string.\n"
    print '_' * 56
print_()

# ———< CLASS >——————————————————————————————————————————————————————————————————
class User(object):
    """A class is a programmer defined data structure. For example,
        a tax-form is also a class. The content of the tax-form from an
        individual is an instance, and from another indvidiual also an
        instances. """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def __str__(self):
        return "User ID: %s\nPassword: %s" % (self.username, self.password)

# USER DATA
jack = User('Zer0Tw0', 'derPa_123!')
jackie = User('Overl0rd', '123abc')
jeniffer = User('JennyX_X', 'lelele123')

dict = {
    'jack' : jack,
    'jackie' : jackie,
    'jeniffer' : jeniffer
}

# retrieve data by raw input

def retrieve_class():
    input = str(raw_input('> '))
    for key in dict:
        if key == input:
            print dict[key]
retrieve_class()

# ———< \CLASS >—————————————————————————————————————————————————————————————————

def exec_():
    """exec() executes code from a string or code object."""
    piece_of_code = """a = 10\nb = 7\nprint a + b
    """
    exec(piece_of_code)
exec_()

def in_():
    """the in statement checks for substrings or memberships depending to
    what in refers to:"""
    print "abc" in "abcdefg"
    print "abc" in ["abc", "dickie", "lol"]
in_()
print

def is_():
    """compares whether variables point at the same thing."""
    lst_a = [1, 2, 3]
    lst_b = lst_a
    print lst_a == lst_b # checks for equality
    print lst_a is lst_b # checks whether both variables point at the
    # contents of the lists.
    lst_c = list(lst_a)  # making a copy of the list
    print lst_a == lst_c
    print lst_a is lst_c # produces false, because lst_c is a copy of lst_a
is_()

def return_(a, b):
    """The return statement causes your function to exit and hand back a
    value to its caller."""
    return_here = 0
    return_here += a + b
    return return_here

print return_(10, 33)

def def_():
    """def is abbreviation of definition, def defines a new function."""

def for_():
    """for is a looping function that loops over data."""
    lst = []
    for n in range(0, 7):
        lst.append(n)
        print lst
for_()

def lambda_():
    double = lambda x: x * 2


"""^"""
# https: // www.youtube.com / watch?v = 25
# ovCm9jKfA

# Lists ———————————————————————————————————————————————————————————————————————>
# To create a list out of a string or to split a string use:

lst = "One Two Three"   # Prints the string like usual.
print lst               # >>> One Two Three

lst_a = lst.split(' ')  # When you (' ') turns all words into string objects.
print lst_a             # >>> ['One', 'Two', 'Three']

lst_b = lst.split('#')  # When you ('#') turns entire string in 1 list object.
print lst_b             # >>> ['One Two Three']

# Console:
# >>> One Two Three
# >>> ['One', 'Two', 'Three']
# >>> ['One Two Three']

# Use pop() to pop the last item out of a list.
original_list = ['Een', 'Twee', 'Drie']     # Original list.
after_pop_function = original_list.pop()    # >>> Drie
after_pop_function_2 = original_list.pop(0) # pop(x) x is the index of the item.

print original_list
print after_pop_function

# Console:
# >>> ['Een', 'Twee']
# >>> Drie
# >>> Een


# Playing with lists: —————————————————————————————————————————————————————————>
# A variable containing a string with 6 words.
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# Prints a string that expresses a fact about the variable 'ten_things'.
print "Wait there's not 10 things in that list, let's fix that."

# A variable containing the 'ten_things' variable modified with '.split(' ').
# The split() function creates a list out of a string.
# Produces ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar'].
stuff = ten_things.split(' ')


# A list called 'more_stuff' containing 8 strings.
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl",
              "Boy"]

# A while loop that executes when the length of 'stuff' does not equal 10.
# 'stuff' is a created list out of the variable 'ten_things' by using split().
while len(stuff) != 10:
    # This variable is defined as being the last item from the list 'more_stuff'.
    # This is done through the pop() method, that pops of the last item of a list.
    # You can also specify which item to pop() by indicating the index: pop(1)
    next_one = more_stuff.pop()
    # Prints a string announcing which item is going to be added.
    print "Adding: ", next_one
    # Using the append() method to append 'next_one' to 'stuff'
    stuff.append(next_one)
    # Prints a string displaying the updated version of the list 'stuff'
    # showing how long the list is now.
    # Loop repeats until stuff becomes a list of 10 items.
    print "There's %d items now." % len(stuff)

# Prints the last updated version of the list 'stuff' contaning 10 items.
print "There we go: ", stuff

# Prints a string announcing what is to comen next.
print "Let's do some things with stuff."

# Prints the second item of the list 'stuff' 1 is 2 because the count is ordinal.
print stuff[1]
# Prints last item of the list 'stuff' because of minus symbol '-1'.
print stuff[-1]
# Prints the last item of the list because pop()'s default is to do so, if
# not assigned by an index.
print stuff.pop()
# Joins the list by a space written as ' '.
# Because of the previous pop() of the item Corn, the
# list retains it modification.
print ' '.join(stuff)
# Join the list by using a hash written as '#', but do this to the third and
# fourth word written as, [3:5].
print '#'.join(stuff[3:5])

# ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy',...]
#     ^          ^         ^          ^         ^         ^       ^    ^
#     0          1         2          3         4         5       6   ...
# [3:5] transelate to:                |         |         |
#                                    [3    :    4]   ==   5]
#                                     |         |
#                                   Telephone#Light

# list['One', 'Two', 'Three']
# Only use numbers to get items out of a list list[1] is 'Two'


# Show a list of methods: —————————————————————————————————————————————————————>
lst = [1, 2, 3]
print dir(lst)  # This dir(x) shoes a list of the applicable methods on xself.

# Console:
# >>> ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__',
# 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# List comprehension: —————————————————————————————————————————————————————————>
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [i ** 2 for i in range(1,12) if i % 2 == 0]
print even_squares

# More list comprehension:
threes_and_fives = [n for n in range(1,16) if n % 3 == 0 or n % 5 == 0]
print threes_and_fives
# produces [3, 5, 6, 9, 10, 12, 15]


# List slicing elaborated: ————————————————————————————————————————————————————>
to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]

print middle_third
# prints 8, 9, 10, 11, 13, 14


# .zip function: ——————————————————————————————————————————————————————————————>
# zip(lst1, lst2) zip is used for pairing lists into tuples.
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
print(list(names_and_dogs_names))

# Produces:
# [('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'), ('Sam', 'Carter'),
# ('Grace', 'Ralph')]

lst1 = [1, 2, 3, 4, 5]
lst2 = ['a', 'b', 'c', 'd', 'e']

zip_lst1_&_lst2 = zip(lst1, lst2)
print list(zip_lst1_&_lst2)

# Produces:
# [(1, a), (2, b), (3, c), (4, d), (5, e)]


# List adding and order: ——————————————————————————————————————————————————————>
mark = ["X"]
all_ages = mark + [1, 2, 3]
all_ages_2 = [1, 2, 3] + mark

print all_ages
print all_ages_2

# Produces:
# ['X', 1, 2, 3]
# [1, 2, 3, 'X']


# Counting items in a list: ———————————————————————————————————————————————————>
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake',
 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie',
 'Jake', 'Jake', 'Cassie', 'Laurie']

# .count() function counts how many of the same items are in a list:
# list.count(<item to be counted>)
jake_votes = votes.count('Jake')
print(jake_votes)

# Produces:
# 9

lst = [1, 1, 1, 2, 3, 4]
count_lst = lst.count(1)
print count_lst

# Produces:
# 3


# sorted(list): ———————————————————————————————————————————————————————————————>
# In contrast to sort .sort() sorted creates a new list that is the sorted
# version of a list. E.g. sorted_list = sorted(list)
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)

print(games)
print(games_sorted)

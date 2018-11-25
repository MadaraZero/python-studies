# For Loops ———————————————————————————————————————————————————————————————————>
# a list of integers.
the_count = [1, 2, 3, 4, 5]
# a list of strings.
fruits = ['apples', 'oranges', 'pears', 'apricots']
# a list of integers and strings.
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list.
# for 'an element' in the list 'the_count' do this(x)
for number in the_count:
	# this(x)
	print "This is count %d" % number

# same as above.
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too.
# notice we have to use %r since we don't know what's in it.
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one.
elements = []

# then use the range function to do 0 to 5 counts.
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i

# assigning range to variable is possible.
test = range(0, 5)
print test

for i in test:
	print "Element was: %d" % i

empty_list = []

empty_list.append(range(0, 10))

print empty_list

downtown_zoo_animals = ['Jaguar', 'Lion', 'Tiger']
print "Downtown Zoo Animals:", downtown_zoo_animals
print
newyork_zoo_animals = ['Penguin', 'Dolphin']
print "New York Zoo Animals:", newyork_zoo_animals

for animal in downtown_zoo_animals:
	newyork_zoo_animals.append(animal)

print
print "New York Zoo Animals:", newyork_zoo_animals


# While Loops —————————————————————————————————————————————————————————————————>
# variable 'i' contains '0'.
i = 0
# variable called 'numbers' that contains an empty list.
numbers = []

# while the variable i contains an integer less than 6
# do something...|
while i < 6:
	# |... print string with 'i' formatted into it.
	print "At the top i is %d" % i
	# also, append the 'i' the code is currently on to the list 'numbers'
	numbers.append(i)
	# after all of that, increment the i by 1.
	i += 1
	# print string, and the 'updated list' by the previous lines.
	print "Numbers now: ", numbers
	# print string, and the last number appended to the 'numbers' list.
	print "At the bottom i is %d\n" % i


print "The numbers:"

# since our list called numbers is not empty anymore, but contains 5 numbers
# due the append.() function.
# the code below will print each element referred to as 'num' from numbers.
for num in numbers:
	print num

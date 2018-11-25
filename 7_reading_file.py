# File methods ————————————————————————————————————————————————————————————————>
# close —Closes the file. Like File- >Save.. in your editor.
# read —Reads the contents of file. You can assign the result to a variable.
# readline —Reads just one line of a text file.
# truncate —Empties the file. Watch out if you care about the file.
# write(stuff) —Writes stuff to the file.
# these are modifiers 'w+' , 'r+' 'a+' example:
# open(filename, 'w'), open(filename, 'r'), open(filename, 'a')

# Seek method —————————————————————————————————————————————————————————————————>

# seek() # filepointer.seek(offset, from_what) position of file.
# where fp is the file pointer you're working with; offset means
# how many positions you will move; from_what defines your point of reference:

# 0: means your reference point is the beginning of the file
# 1: means your reference point is the current file position
# 2: means your reference point is the end of the file


# use in [>_] Terminal ————————————————————————————————————————————————————————>
# script below gets us a 'txt' file and displays it in the Terminal.
from sys import argv

script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# Ex15.py sample.txt

# +------+       +------+       +------+       +------+       +------+
# |`.     `.     |\      \      |      |      /      /|     .'     .'|
# |  `+------+   | +------+     +------+     +------+ |   +------+'  |
# |   |      |   | |      |     |      |     |      | |   |      |   |
# +   |      |   + |      |     |      |     |      | +   |      |   +
# `. |      |    \|      |     |      |     |      |/    |      | .'
#  `+------+     +------+     +------+     +------+     +------+'


  #  .+------+     +------+     +------+     +------+     +------+.
 # .'      .'|    /      /|     |      |     |\      \    |`.      `.
# +------+'  |   +------+ |     +------+     | +------+   |  `+------+
# |      |   |   |      | |     |      |     | |      |   |   |      |
# |      |   +   |      | +     |      |     + |      |   +   |      |
# |      | .'    |      |/      |      |      \|      |    `. |      |
# +------+'      +------+       +------+       +------+      `+------+

# Open Images —————————————————————————————————————————————————————————————————>
from PIL import Image
img = Image.open('main_room.png')
img.show()


# More file theory: ———————————————————————————————————————————————————————————>
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")


# Add your code below!
for item in my_list:
  my_file.write(str(item))
  my_file.write("\n")

my_file.close()

my_file = open("output.txt", "r")
print my_file.read()
my_file.close()

my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()


# with as: ————————————————————————————————————————————————————————————————————>
# this initializes the __exit__() method for files:
with open("text.txt", "w") as textfile:
  textfile.write("Success!")


# closed method: ——————————————————————————————————————————————————————————————>
# check whether a file is closed or not
file.closed

# string tricks 1: ————————————————————————————————————————————————————————————>
first_name = "Bob"
last_name = "Daily"

# This produces an error because strings are immutable:
first_name[0] = "R"

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)


first_name = "Reiko"
last_name = "Matsuki"


# strings password generator: —————————————————————————————————————————————————>
def password_generator(first_name, last_name):

    lenght_first = len(first_name)
    lenght_second = len(last_name)

    first_name_last_3 = first_name[lenght_first - 3:]
    last_name_last_3 = last_name[lenght_second - 3:]

    return first_name_last_3 + last_name_last_3

password_generator("Reiko", last_name)


# string tricks 2: ————————————————————————————————————————————————————————————>
def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    # Usefull boolean composition:
    if (letter in string_two) and not (letter in common): # <-- Useful boolean
      common.append(letter)
  return common


# string methods 1: ———————————————————————————————————————————————————————————>
.lower() # returns the string with all lowercase characters.
.upper() # returns the string with all uppercase characters.
.title() # returns the string in title case, which means the first letter of
         # each word is capitalized.

abc_var = "abc def"
ABC_var = "ABC DEF"

abc_var.title()   # Produces: Abc Def
abc_var.upper()   # Produces: ABC DEF
ABC_var.lower()   # Produces: abc def



# string methods 2: ———————————————————————————————————————————————————————————>
.split() # returns a list of all the words of a stringselfself.

a_string = "Abc def ghi"
b_string = "Abc def | ghi"

a_string.split()  # Produces: ['Abc', 'def', 'ghi']  3 items
b_string.split("|")  # Produces: ['Abc def', 'ghi']  2 items split by "|"


# string methods 3:  ——————————————————————————————————————————————————————————>
.join()  # joins a list of words togheter with the used delimiter.
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of",
"steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words)
print reapers_line_one

# Produces:
# Black reapers with the sound of steel on stones

reapers_line_one = " | ".join(reapers_line_one_words)
print reapers_line_one

# Produces:
# Black | reapers | with | the | sound | of | steel | on | stones

winter_trees_lines = ['All the complicated details', 'of the attiring and',
                      'the disattiring are completed!', 'A liquid moon',
                      'moves gently among', 'the long branches.',
                      'Thus having prepared their buds', 'against a sure winter',
                      'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)

# Produces:

# All the complicated details
# of the attiring and
# the disattiring are completed!
# A liquid moon
# moves gently among
# the long branches.
# Thus having prepared their buds
# against a sure winter
# the wise trees
# stand sleeping in the cold.


# string methods 4:  ——————————————————————————————————————————————————————————>
.strip()  # removes all unnecessary white-spaces by default OR delimiters:

example_lst = "     Hello Good           "
print example_lst.strip()
# Produces:
# Hello World !

example_list_2 = "........World ..."
print example_list_2.strip(".")
# Produces:
# World


# string methods 5:  ——————————————————————————————————————————————————————————>
.replace(first, second)# Replace takes two arguments and replaces all instances
# of the first argument in a string with the second argument.

a_lil_string = "One Two Three Four"
print a_lil_string.replace(" ", "_")

# Produces:
# One_Two_Three_Four


# string methods 5:  ——————————————————————————————————————————————————————————>
.find() # finds the first index of specified delimeter:

a_string = "aaaaaaaaaaaaaaaaaabc"
a_string.find("b")

a_string = "aaaaaaaaaaaaaaaaaabc"
print a_string.find("b")

# Produces:
# Because b is at the 18th index:
# 18


# string methods 6:————————————————————————————————————————————————————————————>
.format() # formats a string with specified input

# For example:
title = "I Hear America Singing"
poet = "Walt Whitman"
print 'The poem "{}" is written by {}.'.format(title, poet)

# Produces:
# The poem "I Hear America Singing" is written by Walt Whitman.

def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

print favorite_song_statement("Ghost", "Jaden Smith")

# Produces:
# My favorite song is Ghost by Jaden Smith.

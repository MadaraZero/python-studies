# Python Console is [>>>_] ————————————————————————————————————————————————————>

# We can load this script as 'ex25' module in the Python Console.
# We can also load all of the functions with 'from ex25 import *'

# The green strings on the first line of the functions e.g.
# """This function will break[...]""", Explain what the function does. You
# can call this explanation in the python console by 'help(ex25.break_words)'
# You can also call upon all of the documentation by 'help(ex25)'

# The cool things is that you can run all of these functions in the Python
# Console whenever you want. For example, ex25.break_words(sentence)
# ex25(dot)break_words means "take the 'break_words' function from the
# 'ex25' module.

# You can also import all the functions in one go by 'from ex25 import *'
# so you don't have to type the 'ex25.'<FUNCTION> anymore.


def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words


def sort_words(words):
	"""Sorts the words."""
	return sorted(words)


def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word


def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word


def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)


def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)


def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

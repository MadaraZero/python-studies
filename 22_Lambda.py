# Lambda with Filter:  ————————————————————————————————————————————————————————>
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x: x == "Python", languages)
#                    |
#             basically says if
#   and reads as math 'x: x == "Python"' reads x such that x is the same as
# "Python".

# Lambda with Filter 2:  ——————————————————————————————————————————————————————>
>>> squares = [n ** 2 for n in range(1, 11)]
>>> print filter(lambda n: n >= 30 and n <= 70, squares)
# produces [36, 49, 64]

# raw_input() —————————————————————————————————————————————————————————————————>
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight
)
print # used for beter presentation
char_name = raw_input("What is the name of your Hero? "),
char_class = raw_input("Are you a Ninja, Wizard, or Archer? "),

print "Your character called %s is a %s from %s." % (
    char_name, char_class)

# using 'raw_input' like below looks better on the console.
print "Are you a Ninja, Samurai, Archer, or Magician?",
char_class_2 = raw_input()

print "Your class is %s." % char_class_2


# My first calculator —————————————————————————————————————————————————————————>
# below is a calculator for addition I wrote!
print "Enter a number: ",
a = int(raw_input())
print "Enter a number: ",
b = int(raw_input())
result = a + b

print "%r + %r = %r" % (a, b, result)


# Raw input & pydoc ———————————————————————————————————————————————————————————>
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight
)

# for python documentation use:
# python -m pydoc <functiong> = python -m pydoc int

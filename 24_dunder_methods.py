# Inhereting from primitive types: ————————————————————————————————————————————>
from random import randint

# a new list class that modifies the append function to generate
# the sorted version of the list after each append!
# This is possible because SortedList is a subclasss of the built in 'list' type
class SortedList(list):
    def append(self, value):
        super(SortedList, self).append(value)
        self.sort()

>>> slist = SortedList([2, 1, 4])
>>> print slist
[2, 1, 4]

>>> slist.append(6)
>>> print slist
[1, 2, 4, 6]

>>> for i in range(1, 15):
       slist.append(randint(1, 30))

>>> print slist
[1, 1, 2, 2, 2, 4, 4, 6, 9, 9, 14, 15, 16, 19, 20, 23, 27, 28]


# The __len__: ————————————————————————————————————————————————————————————————>
#    __contains__
class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  def __len__(self):
    return len(self.lawyers)

  def __contains__(self, lawyer):
    return lawyer in self.lawyers

d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
print(len(d_and_p))


# The __add__: ————————————————————————————————————————————————————————————————>
# allows using '+' for a function doing addition, rather than calling
# the function by its name:
class NiggasInParis:
    def __init__(self, niggas, paris):
        self.niggas = niggas
        self.paris = paris

    def __add__(self, other):              # <----------.  __add__
        return self.niggas + self.paris #               .
#                                                       .
#                                                       .
niggas = NiggasInParis("Niggas", "in") #                .
niggas_2 =  NiggasInParis("Muthafucking", "Paris!") #   .
#                ,.......................................
a_nigga = niggas + niggas_2
print a_nigga

# The __init__: ———————————————————————————————————————————————————————————————>
class Car(object):
    condition = "new"

    # __init__ Boots up the class variables for every other instance:
    def __init__(self, model, color, mpg):#                         ^
        self.model = model#                                  <      .
        self.color = color#                                  <      .
        self.mpg = mpg#                                      <      .
#                                                                   .
    def display_car(self):#                                         .
        print "This is a %s %s with %s MPG." % (#                   .
        self.color, self.model, str(self.mpg))#                     .
#                                                                   .
    def drive_car(self): #                                          .
        self.condition = "used" #                                   .
#                                                                   .
my_car = Car("Lamborghini", "yellow", 255) #  ,---------------------'
#                 ^............^.......^.....'


# The __repr__: ———————————————————————————————————————————————————————————————>
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):

        # __repr__ Changes how Python represents the data:
        return "<| %d, %d, %d |>" % (self.x, self.y, self.z)


my_point = Point3D(1, 2, 3)
print my_point


# hasattr() & getattr()_: —————————————————————————————————————————————————————>
class Attrium:
    pass

attributeless = Attrium()

>>> hasattr(attributeless, "fake_attribute")
# returns False

>>> getattr(attributeless, "other_fake_attribute", "No such attribute.")
# returns 800, the default value

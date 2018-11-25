# Inheritance: ————————————————————————————————————————————————————————————————>
"""
Classes, inheritance theory from: The Hard Way To Learn Python.
"""

print # for tab


# Inheritance: ————————————————————————————————————————————————————————————————>
# ---- Inheritance implicitely example:
class Parent(object):

    def implicit(self):
        print "PARENT implicity()"

class Child(Parent):
    pass

dad_1 = Parent()
son_1 = Child()

dad_1.implicit()
son_1.implicit()


# Inheritance: ————————————————————————————————————————————————————————————————>
# ---- Overriding explicitly example:
class Parent(object):

    def override(self):
        print "\nPARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad_2 = Parent()
son_2 = Child()

dad_2.override()
son_2.override()


# Inheritance: ————————————————————————————————————————————————————————————————>
# ---- Alter Before or After:
class Parent(object):

    def altered(self):
        print "\nPARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self). altered()
        print "CHILD, AFTER PARENT altered()"

dad_3 = Parent()
son_3 = Child()

dad_3.altered()
son_3.altered()


# Inheritance: ————————————————————————————————————————————————————————————————>
# ---- All Three Combined:
class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad_4 = Parent()
son_4 = Child()

print "_" * 45

dad_4.implicit() # Parent class: implicit() is called from the Parent class.
son_4.implicit() # Child class: the Child class calls the implicit() function
                 # from the Parent class.
print # for tab
dad_4.override() # Parent class: override() is called from the Parent class.
son_4.override() # Child class: a new and unique override() is called from the
                 # Child class.
print # for tab
dad_4.altered() # Parent class: Parent class calls altered() from itself.
son_4.altered() # Child class: the Child class calls altered() from itself
                # this is <line 80>, then it goes to <line 81>
                # now the Child class calls altered() from the Parent class
                # first, and then proceeds to <line 82> which is analogous to
                # new functionality.


# Inheritance: ————————————————————————————————————————————————————————————————>
# Spawning instances of classes in a class to use their properties.
class Monster():
   a_property_1 = "Can do damage to player"


class Boss():
   a_property_2 = "Gives big reward to player"


class GhostBoss():

    def __init__(self):
      self.monster = Monster() # Instantiates Monster Class object
      self.boss = Boss()       # Instantiates Boss Class object

    def take_from_monster_class(self):
        print self.monster.a_property_1

    def take_from_boss_class(self):
        print self.boss.a_property_2


>>> ghost_boss = GhostBoss()
>>> ghost_boss.take_from_monster_class()
>>> ghost_boss.take_from_boss_class()

# Can do damage to player
# Gives big reward to player

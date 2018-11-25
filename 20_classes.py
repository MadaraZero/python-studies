# Some More Class Theory:  ————————————————————————————————————————————————————>
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive

# Note that every Animal has an individual name and ageselfself.
# However, every animal has acces to 'is_alive'.
# Thus, by definition every all animals inheret 'True'.

# Some More Class Theory 2:  ——————————————————————————————————————————————————>
class Animal(object):
  """Makes cute animals."""
  # These are member variables.
  # meaning they are shared by all 'Animal classes'.
  is_alive = True #
  health = 'good' # <-----------------------------.
#                                                 .
  def __init__(self, name, age):  #               .
    self.name = name              #               .
    self.age = age                #               .
  # Add your method here!                         .
  def description(self):          #               .
    print self.name               #               .
    print self.age                #               .
#                                                 .
hippo = Animal('Hypeman', 99)     #               .
sloth = Animal('Slothman', 77)    #               .
ocelot = Animal('Ocieuseman', 18) #               .
#                                                 .
hippo.description() #                             .
#                                                 .
print hippo.health         # Produces: good ------.
print sloth.health         # Produces: good ------.
print ocelot.health        # Produces: good-------

# Inheritance: ————————————————————————————————————————————————————————————————>
class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

# Because ReturningCustomer is defined as an 'is-a Customer' it automatically
# inherents everything from the 'Customer class'
class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

# Inheritance 2: ——————————————————————————————————————————————————————————————>
class Greeting(object):
    def __init__(self, hello):
        self.hello = hello #<############
                                        #
class Text(Greeting):                   #
    def greeting(self):                 #
        print "Yeah!"                   # Inherits the 'hello' variable
                                        # Because the 'Text class' is defined
                                        # as an 'is-a Greeting class'
a_text = Text("Hi")                     #
a_text.greeting()                       #
print a_text.hello #>####################

# Inheritance 3: ——————————————————————————————————————————————————————————————>
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

shape = Triangle(12, 13, 14)
# Inheritance 4: ——————————————————————————————————————————————————————————————>

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours): # <...................
    self.hours = hours #                                 . Rather than creating
    return hours * 20.00 #                               . a new 'calculate_wage'
#                                                        . function. We simply
# Add your code below!                                   . override it. By
class PartTimeEmployee(Employee): #                      . literally duplicating
  #                                                      . it.
  def calculate_wage(self, hours): # >...................
    self.hours = hours
    return hours * 12

# Inheritance 5: ——————————————————————————————————————————————————————————————>
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours): <-------------------.
    self.hours = hours                                 |
    return hours * 20.00                               |
                                                       |
class PartTimeEmployee(Employee):                      |
  def calculate_wage(self, hours):                     |
    self.hours = hours                                 |
    return hours * 12.00                               |
                                                       |
  def full_time_wage(self, hours):                     |
    # With the 'super' syntax you can call methods from the base class.
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print milton.full_time_wage(10)

# Triangle class:  ————————————————————————————————————————————————————————————>
class Triangle(object):
  number_of_sides = 3

  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3

  def check_angles(self):
    if self.angle1 + self.angle2 + self.angle3 == 180:
      return True
    else:
      return False

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
  	self.angle1 = self.angle
  	self.angle2 = self.angle
  	self.angle3 = self.angle

  def show_angles(self):
    print self.angle1, self.angle2, self.angle3

my_triangle = Triangle(60, 50, 70)
print my_triangle.number_of_sides
print my_triangle.check_angles()

my_equ_triangle = Equilateral()
print my_equ_triangle.number_of_sides
print my_equ_triangle.check_angles()
my_equ_triangle.show_angles()

# THREE WAYS TO GET THINGS: ———————————————————————————————————————————————————>
# dict style
mystuff['apples']

# module style
mystuff.apples()
print mystuff.tangerine

# class style
thing = MyStuff()
thing.apples()
print thing.tangerine

# Example of class of Cart: ———————————————————————————————————————————————————>
class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""

  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_cart = {}
  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."

my_cart = ShoppingCart('Denis')
my_cart.add_item('Car', 190000)

# EXAMPLE OF A SIMPLE CLASS: ——————————————————————————————————————————————————>
# Example of a simple class:
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
# end of class

happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there\n"])

bulls_on_parade = Song([
    "They rally around the family",
    "With pockets full of shells\n"])

samurai_champloo = Song([
    "Ah yeah, I am a nigga",
    "You are a fringer digger",
    "Don't fuck my lil finger\n"
])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
samurai_champloo.sing_me_a_song()


# SECOND EXAMPLE OF A SIMPLE CLASS: ———————————————————————————————————————————>
# Another example of a class I created:
# ---- CLASS >-----------------------------------------------------------------
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

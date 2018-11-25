# Polymorphism: ———————————————————————————————————————————————————————————————>
# polymorphism is shared intuitive functionality.
# while the same thing might be happening from an intuitive point of view
# the same thing is not happening literally...

# Example regarding '+' operator:
1 + 1 = 2                                 # different type of addition...
"Hello " + "World!" = "Hello World!"      # compared to this type of addition...
                                          # but, nonetheless addition.

a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list))     # counts items in a list
print(len(a_dict))     # counts amount of key/value pairs in a dict
print(len(a_string))   # counts amount of characters in a string
                       # different types of counting but counting nonetheless.


# Classes with the same interface: ————————————————————————————————————————————>
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
  def get_rate(self):                                # Same Interface
    return .001 * self.price_of_insured_item         #      .
                                                     #      .
class HomeInsurance(InsurancePolicy):                #      .
  def get_rate(self):                                # Same Interface
    return .00005 * self.price_of_insured_item


# super(): ————————————————————————————————————————————————————————————————————>
class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    # with super() we basically "copy and paste" the init from the superclass
    # which is PotatoSalad

    super().__init__(potatoes, celery, onions)
    self.raisins = 40


# Exception classes: ——————————————————————————————————————————————————————————>
# Define your exception up here:
# OutOfStock is defined as an is-a Exception object
# which is a built in object in Python:
class OutOfStock(Exception):
  pass

# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock

  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
    else:
      self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
#candle_shop.buy('green')
print(candle_shop.stock['blue'])


# Assigning init variables to instances: ——————————————————————————————————————>
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    return 2 * self.pi * self.radius

    # Creating some instances of the Circle class:
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

    # Calling the class function on some instances of it:
print medium_pizza.circumference()
print teaching_table.circumference()
print round_room.circumference()


# Class example: ——————————————————————————————————————————————————————————————>
# Defining a student class:
class Student:
  # Constructor that initializes 3 variables, name, year, and grades
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  # class method that checks if grade is the same type as the Grade class.
  # If so then the function adds grade to the list variable 'self.grades'
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)


# Defining a grade class:
class Grade:
  # A member variable that says that all grades that are 65 are a passing grade:
  minimum_passing = 65

  # Constructor that initializes one variable called 'score'.
  def __init__(self, score):
    self.score = score

# Here we create 3 instances of the student class:
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


# Here we call the add_grade function on the Student instance pieter.
# with the argument 'Grade(100)', the argument is 100 of type Grade.
# The function add_grade checks whether it is of type Grade().
# In this case it is, so it adds '100' to the list pieter.grades.
pieter.add_grade(Grade(100))

# Dictionaries: ———————————————————————————————————————————————————————————————>

# Anatomy of dictionary:
<variable> = {<key>: <value>}
cat = {1: 'jack'}

# Printing by using the value of a dictionary as a key in another dictionary

dict_1 = {
    'a' : 'b'
}

dict_2 = {
    'b' : 'c'
}

# acces the data from dict_2 by using the value of dict_1 as a key to to dict_2
print dict_2[<dict_1[a]>]
                 |
print dict_2   <[b]>
                 |
                <c>

# State Mapping: ——————————————————————————————————————————————————————————————>
# Creates a mapping of state to abbreviation.
# A dictionary of states with the state name as key and abbreviation as value.
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them.
# A dictionary of cities with abbreviation as key and name as value.
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some more cities.
# In cities we add the key 'NY' that represents the value 'New York.
# in cities we add the key 'OR' that represents the value 'Portland'
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities.
# Prints out from cities dictionary the value that the 'NY'-key contains.
# Prints out from cities dictionary the value that the 'OR'-key contains.
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# Print out some states.
# Prints out from states dictionary the value that the 'Michigan'-key contains.
# Prints out from states dictionary the value that the 'Florida'-key contains.
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# Do it by using the state then cities dict.
# Prints out the city by using the value of a state as a key for cities:
# cities[states['Michigan]] transelates to: the value of the key 'Michigan'
# in states dictionary is the key in the cities dictionary.
print '-' * 25
print "Michigan has: ", cities['MI']
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# Print every state abbreviation.
print '-' * 10
# For loop that loops over state, and abreviation in states.items()
# items() returns a tupple pair e.g. ('Michigan', 'MI')
# Thus, state stands for the state key, and abbrev for the value of the key.
# example: state = Michigan : abbrev = MI
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# Print every city in state.
print '-' * 10
# For loop that loops over abbrev, and city in cities.items()
# abbrev is the key of cities.
# city is the value of cities.
# items() returns tuples of key and value pair to execute the for loop on.
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# Now do both at the same time.
print '-' * 10
for state, abbrev in states.items():
    print "%s has the city %s" % (abbrev, city)

# Now do both at the same time. For example:
# state          =     Michigan
# abbrev         =     MI
# cities[abbrev] =     MI
# cities[MI]     =     Detroit
# note how cities is using the value of a state as a key for its self.
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities
                                                          [abbrev])

print '-' * 10
# Safely get an abbreviation by state that might not be there.
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas"

# Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

# Eigen State Mapping —————————————————————————————————————————————————————————>
organizer = '.' * 70
prov = {
    'Zuid-Holland'  : 'ZH_a',
    'Noord-Holland' : 'NH_a',
    'Wadden-Eilanden' : 'WE_a'
}

steden = {
    'ZH_a' : 'Rotterdam',
    'ZH_b' : 'Zwijndrecht',
    'ZH_c' : 'Hendrik-Ido-Ambacht',
    'NH_a' : 'Amsterdam',
    'NH_b' : 'Leiden'
}

steden['WE_a'] = 'Tessel'
steden['WE_b'] = 'Vlaardingen'

print organizer
print "Hier is een afkorting van een provincie: ",  prov['Noord-Holland']
print "Hier is een andere afkorting van een provincie: ", prov['Zuid-Holland']

print organizer
print "Hier zijn een paar steden: ", steden['ZH_b']
print "Hier zijn een paar steden: ", steden['NH_b']
print "Hier zijn een paar steden: ", steden['WE_b']

print organizer
print "Hier is een abstracte manier om een stad te laten zien: ", \
    steden[prov['Noord-Holland']]
print "Hier is een abstracte manier om een stad te laten zien: ", \
    steden[prov['Wadden-Eilanden']]

print organizer
for provincie, afkorting in prov.items():
    print "%s is de afkorting van %s" % (afkorting, provincie)

print organizer
for provincie, stad in steden.items():
    print "%s heeft de stad %s" % (provincie, stad)

print organizer
for provincie, afkorting in prov.items():
    print "%s provincie heeft de afkorting %s en de stad %s" % (provincie, afkorting,
                                                            steden[afkorting])
print organizer
for a, b in steden.items():
    print "%s is key, %s is value" % (a, b)

# using specific pieces of dictionaries # State Mapping: ——————————————————————>
my_dict = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three'
}

print my_dict.keys()    # prints dictionary keys
print my_dict.values()  # prints dictionary values
print my_dict.items()   # prints all dictionary tuples and keys i.e. (key, val)

# Update method: ——————————————————————————————————————————————————————————————>
.update() # Allows for adding multiple key, val pairs at the same time:

dict = {
1 : "One",
2 : "Two",
3 : "Three",
}

dict.update({
4 : "Four",
5 : "Five"
})

print dict

# the update method adds the key value pair of 4 : Four and 5 : Five
# at the same time. Thus producing:

# >>> {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

# Creating dictionaries through list comprehension: ———————————————————————————>
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# Syntax:
students = {key:value for key, value in zip(names, heights)}

# Prdocues:
# >>> {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

# Using try-except block to spot key errors: ——————————————————————————————————>
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

try:
  print(caffeine_level["matcha"])

except KeyError:
  print("Unknown Caffeine Level.")

# Produces:
# Uknown Caffeine Level.

# Using get method: ———————————————————————————————————————————————————————————>
.get("<key>") # using get method returns None by default rather than an error if
# key/value pair does not exist:
# You can also specify what the functions returns rather than None for example:
# "Key does not exist."

dict = {
1 : "One",
2 : "Two",
3 : "Three",
}

dict.update({
4 : "Four",
5 : "Five"
})

# Using get rather than dict[key]:
print dict.get(4)
print dict.get(5)
print dict.get(6)   # Note how 6 returns None.
print dict.get(6, "No such key in dict!") # Now we changed the default "None".

# Using pop method: ———————————————————————————————————————————————————————————>
.pop() # is straightforward you specific the key and it will pop of the key/value
# pair of the dictionary i.e. removing it.
dict_2 = {
1 : "One",
2 : "Two",
3 : "Three",
4 : "Four",
5 : "Five"
}

dict_2.pop(1)
# If you don't specify the default is an error.
dict_2.pop(6, "No such key 6 in dict.")

print dict_2
# Produces:
# {2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}
# Because 1 has been popped of.


# Using keys method: ——————————————————————————————————————————————————————————>
.keys() # gets keys of dictionary and puts them in a list:
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112,
"lyleLoop": 102931, "keysmithKeith": 129384}

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15,
 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

.values() # There is also the values method that basically does the same for values.

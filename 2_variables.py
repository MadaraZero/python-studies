# Variables ———————————————————————————————————————————————————————————————————>
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driver = drivers
carpool_capacity = cars_driver * space_in_a_car
average_passengers_per_car = passengers / cars_not_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"


the_number_100 = 100
the_number_5 = 45
the_almighty_number = the_number_100 * the_number_5
some_text = "The glorious number is... "
final_composition = some_text + str(the_almighty_number)

print final_composition

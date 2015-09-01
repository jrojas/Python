# storing 100 cars
cars = 100

#4 spaces inside car
space_in_a_car = 4.0

#30 drivers
drivers = 30

#90 passengers
passengers = 90

#cars subtracted by drivers
cars_not_driven = cars - drivers

# cars_driven equals the value of drivers
cars_driven = drivers

#carpool_capacity is equal to cars_driven multiplied by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car

#average passengers per car equals passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
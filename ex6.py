#replacing %d with the value 10
x = "There are %d types of people." % 10

#binary equals binary
binary = "binary"

#do_not value is don't
do_not = "don't"

#y is equal to:  Those who know binary and those who don't
y = "Those who know %s and those who %s." % (binary, do_not)

# prints There are 10 types of people.
print x

# prints Those who know binary and those who don't.
print y

# prints I said: There are 10 types of people.
print "I said: %r." % x

# prints I also said: Those who know binary and those who don't.
print "I also said: '%s'." % y

# hilarious is false
hilarious = False

# Ask why?
joke_evaluation = "Isn't that joke so funny?! %r"

# prints joke_evaluation ?
print joke_evaluation % hilarious


w = "This is the left side of..."
e = "a string with a right side."

# This is the left side of... a string with a right side.
print w + e
types_of_people = 10
# a formatted string with a variable.
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# a formatted string with two variables.
y = f"Those who know {binary} and those who {do_not}."

# print x and y
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# another way to put a variable into a string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# how to do a string concatenation.
print(w + e)
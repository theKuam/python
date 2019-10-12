my_name = 'Ngo Minh Hai'
my_age = 23 # not a lie
my_height = 66 # inches
my_weight = 128 # lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black' # kinda bored.

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"It's mean that he's {round(my_height * 2.54)} centimeters tall")
print(f"He's {my_weight} pounds heavy.")
print(f"It's mean that he's {round(my_weight * 0.45)} kilograms heavy.")
print("Actually that's not too light.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
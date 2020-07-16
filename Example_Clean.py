#  Table of Contents
#  Week 1

'''
Week 1, adding print to console, syntax, calcs, operators and For
'''
print("----- Week 1 -----")
print("Hello World")  # print a str
print(5 * 5)  # print a calc
print(5 > 5)  # print boolean

# Variable "x" equals a str of text and print to console
x = "I'm programming in Python"
print(x)

# Print variable string to the console with an additional string
name = "Eli"
print("Hello, my " + name + ", it is nice to meet you.")

# Negation of special characters, print variable strings to console
color = "Greeen"
thing = "Thing"
print("The " + color + " " + thing + " \"Swamp " + thing + "\" " + "is one of the most terrifying beast of lore")

# Additional Calcs, addition squared, power(s) and square root
x = (((1 + 2) * 3) / 4) ** 5
print(x)

y = 4 ** (1 / 2)
print(y)

# for
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print(friend)  # Print names within the list

# For loop, while this condition is true, return value within the "Range" of 1 - 10
for i in range(10):  # colon to start the statement
    print("Hello world, again")  # Print str 10 times

'''
Cheat Sheet
False	class	finally	is	return
None	continue	for	lambda	try
True	def	from	nonlocal	while
and	del	global	not	with
as	elif	if	or	yield
assert	else	import	pass	
break	except	in	raise	

Operators 
a + b = Adds a and b
a - b = Subtracts b from a
a * b = Multiplies a and b
a / b = Divides a by b
a ** b = Elevates a to the power of b. For non integer values of b, this becomes a root (i.e. a**(1/2) is the square root of a)
a // b = The integer part of the integer division of a by b
a % b = The remainder part of the integer division of a by b
'''
# New Adding section per week
# Week 1 Quiz/Module  Review
print("-----Week 1 Quiz/Module Review -----")
#  Print string to console
print("Programming in Python is, is like Godzilla wrecking it's favorite city building")

#  Ratio with sqRoot
ratio = ((1 + 5 ** (1 / 2)) / 2)
print(ratio)

#  add two strings, print
color = "Yellow"
thing = "Sunflower"
print(color + " is the color of " + thing + " on Siesta beach")

#  Print Calc
print(86400 * 7)

password = 26 * 26 * 26 * 26 * 26 * 26
print(password)

# Print Sector Amount, when Disk Size is divided by Sector Size
# hard drives are 'divided' into Sectors of 512 bytes, Disk size osf 16gb - Disk Si
disk_size = 16 * 1024 * 1024 * 1024  # Given 16gb * 1024**3
sector_size = 512
sector_amount = disk_size / sector_size

print(sector_amount)  # Print Sector Amount

'''
Week 2
Expressions, Variables, Functions, and Conditionals
'''
print("----- Week 2 -----")
# Types, strings, floats, integers, boolean
print(type("Hello" + 'Hello with single quotes'))
print(type(20.22))
print(type(22 % 2))

x = 22 < 23
print(type(x))

#  Variables, added
length = 10
width = 2
area = length * width

print(area)

#  Expressions are a combo of numbers, symbols or other variables that produce a result
# Do use - start with a letter or underscore(_) Do NOT Use - py keywords or functions
base = 5
height = 3
area = base * height / 2

print(area)

print(7 + 8.5)  # Converted 7 to float and calc or implicit conversion same with sentences

# Explicit Conversion requires a type, in this example it will be str()
base = 6
height = 3
area = (base * height) / 2

print("The area of a triangle is base * height divided by 2 equaling: " + str(area))  # console prints String of 9.0

# Short Test/Check
total = 2048 + 4357 + 97658 + +125 + 8
files = 5
average = total / files

print("The average size is " + str(average))  # 20839.2

'''
Week 2
Expressions, Variables, Functions, and Conditionals
'''
print("----- Week 2 Quiz - Expressions and Var  -----")
bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total / 2

print("Each person needs to pay his/her share: " + str(share))

# 2 integers / 1 by the other so that result = 1
numerator = 10
denominator = 10
result = numerator / denominator

print(int(result))  # print 1

word1 = "How "
word2 = "do "
word3 = "you "
word4 = "like "
word5 = "Python "
word6 = "so "
word7 = "far?"
wordAll = word1 + word2 + word3 + word4 + word5 + word6 + word7

print(str(wordAll))  # How do you like Python so far?

# convert to string
print("2 + 2 = " + str(2 + 2))  # 2 + 2 = 4 as a string


# Week 2 - Functions and Conditionals
# def = definition of variable
def greeting(name):  # INCLUDE : semi color - defining greeting parameter is name

    print("Welcome, " + name)  # Welcome, name parameter below


greeting("Eli")


def greeting(name, department):  # defining greeting with two parameters name, department

    print(
        "Welcome, " + name + "you are within the " + department + " department, correct?")  # Welcome, name parameter below


greeting("Eli", "IT CyOps")


def print_seconds(hours, minutes, seconds):

    print(hours*3600 + minutes*60 + seconds)  # Equals 3723 seconds in total
    print(str(hours * 3600) + " = HOURS")
    print(str(minutes * 60) + " = MINUTES")
    print(str(seconds) + " = SECONDS")
    print(str(3600 + 120 + 3) + " Equals in Seconds")


print_seconds(1,2,3)

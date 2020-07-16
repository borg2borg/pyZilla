#  Table of Contents
#  Week 1

#  Week 1
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
x = (((1 + 2) * 3)/ 4)**5
print(x)

y = 4**(1/2)
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
ratio = ((1+5**(1/2))/2)
print(ratio)

#  add two strings, print
color = "Yellow"
thing = "Sunflower"
print(color + " is the color of " + thing + " on Siesta beach")

#  Print Calc
print(86400*7)

password = 26*26*26*26*26*26
print(password)

# Print Sector Amount, when Disk Size is divided by Sector Size
# hard drives are 'divided' into Sectors of 512 bytes, Disk size osf 16gb - Disk Si
disk_size = 16*1024*1024*1024  # Given 16gb * 1024**3
sector_size = 512
sector_amount = disk_size/sector_size

print(sector_amount)  # Print Sector Amount

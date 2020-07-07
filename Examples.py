# Keywords https://docs.python.org/3/library/functions.html
# False	class	finally	is	return
# None	continue	for	lambda	try
# True	def	from	nonlocal	while
# del	global	not	with
# as	elif	if	or	yield
# assert	else	import	pass
# break	except	in	raise

print("Section 1*******************")
print("Hello World")

# add/subtract #multiply/Divide, so calculations as a simple/complex calculator
a = 4 + 5
b = 9 - 5
print(a + b) # print function, prints the variables to the console

y = 4 * 3
z = 18 / 3
print(y + z) # simple addition of two variables

# power/Sq Root
c = 4 ** 4
print(c)

c = (2**10) # 2*2*2*2*2*2*2*2*2*2 to the 10 power or see below as 2*2 10 times
print(c)

f = 2*2*2*2*2*2*2*2*2*2
print(f)

b = (400**(1 / 2))
print(b)

# squareRoot
sq = (9**(1 / 2))
print(sq)

# d floor division (integer division)
d = 9 // 3
print(d)

d = 9 / 3 # float division, float being decimals
print(d)

e = 3 % 7 # modulo operator - returning the remainder of a problem or by dividing the left by the right,
print(e)

f = 3 & 4 # Equals 3  becuase 3 goes into 4 ZERO times, 3 remains
print(f)

# order Of Operations
x = (((90 + 10) * 4) ** (1 / 2))
print(x)

# Comments and Hello World from the BORG
hello = "Prepare to be borg'd, resistance is futile. You will be assimilated"
name = "USS Enterprise"
print(name + hello)

# disk size is 16 * 1024 3 times
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size/sector_size

print(sector_amount)

print("Section 1*******************")
print("Hello World")

# How To Calculate Area
height = 5
length = 5
area = height * length
print(area)

# implicitConversions convert str, int and floats
print(7 * 7.8695)
print("Hello " + "World")

# explictConversion
base = 6
height = 3
area = (base * height) / 2
print("This is the area of a Triangle is: " + str(area))

# avg
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The avg size is: " + str(average))

# billTotal - split between friends
bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total / 2
print("Each share is: " + str(share))

# resultOfInteger
numerator = 10
denominator = 10
result = numerator / denominator
print(int(result))

# wordsWords
word1 = "How "
word2 = "do "
word3 = "you "
word4 = "like "
word5 = "Python "
word6 = "so "
word7 = "far? "
wordAll = word1 + word2 + word3 + word4 + word5 + word6 + word7
print(str(wordAll))

# printWords
print("2 + 2 = " + str(2 + 2))


# defGreeting with parameters()
def greeting(name):
    print("Welcome, " + name)

greeting("Kay")


# nameAndDepartment
def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

greeting("Steve", "IT")


# printHours, Mins and Seconds in a given hour
def print_seconds(hours, minutes, seconds):
    print("There are " + str(seconds) + " seconds, " + str(minutes) + " mins in " + str(hours) + " hour")


print_seconds(1, 60, 3600)


# returnValue
def area_triangle(base, height):
    return base * height / 2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b
print("the sum of both areas is: " + str(sum))


# OR

def get_seconds(hours, minutes, seconds):
    return 3600 * hours + 60 * minutes + seconds


amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# length
name = "Kay"
number = len(name) * 9

print("Hello " + name + ". Your luck number is " + str(number))

name = "Cameron"
number = len(name) * 9

print("Hello " + name + ". Your luck number is " + str(number))


# improvedLength
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))


lucky_number("Kay")
lucky_number("Cameron")


# ALittleStyleWithClarity
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)


circle_area(5)


def rectangle_area(base, height):
    area = base * height  # base*height
    print("This area is " + str(area))


rectangle_area(5, 6)


# Conversion
def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km

miles = 55
km = convert_distance(miles)
print("The distance in kilometers is: " + str(km))
print("The round-trip in kilometers is: " + str(km * 2))

# booleanTruefalse
print(10 > 1)
print(1 == "1")


# if
# def is_positive(number):
# if number > 0:
#     return True
# else:
# return False

# usernameCharExample
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 char long")
    else:
        print("Valid username")


hint_username("Stew")


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(11))


def hint_username(username):
    if len(username) <= 3:
        print("Invalid username. Must be at least 3 char long")
    elif len(username) >= 15:
        print("invalid username. Must be at most 15 char long")
    else:
        print("Valid username")


print(hint_username("StusifiedMeAndYou"))

# Comparison operators
# a == b: a is equal to b
# a != b: a is different than b
# a < b: a is smaller than b
# a <= b: a is smaller or equal to b
# a > b: a is bigger than b
# a >= b: a is bigger or equal to b

# Logical operators
# a and b: True if both a and b are True. False otherwise.
# a or b: True if either a or b or both are True. False if both are False.
# not a: True if a is False, False if a is True.

# BranchingBlocks
# if condition1:
#	if-block
# elif condition2:
#	elif-block
# else:
#	else-block

# Remember: The if-block will be executed if condition1 is True. The elif-block will be executed if condition1 is False and condition2 is True. The else block will be executed when all the specified conditions are false.


x = (2 ** 2)
print(x)

print(len("A dog"))
print(len("A mouse"))
print(9999 + 888)
print(100 * 100)


def hint_username(username):
    if len(username) <= 3:
        print("Invalid username. Must be at least 3 char long")
    elif len(username) >= 15:
        print("invalid username. Must be at most 15 char long")
    else:
        print("Valid username")


print(hint_username("StusifiedMeAndYou"))


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = (filesize % block_size)
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return full_blocks * 4096 + block_size
    return full_blocks * 4096


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192

print(11 % 5)


def sum(x, y):
    return (x + y)


print(sum(sum(1, 2), sum(3, 4)))
print(((10 >= 5 * 2) and (10 <= 5 * 2)))


def hint_username(username):
    if len(username) <= 3:
        print("Invalid username. Must be at least 3 char long")
    elif len(username) >= 15:
        print("invalid username. Must be at most 15 char long")
    else:
        print("Valid username")


print(hint_username("StusifiedMeAndYou"))


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = (filesize % block_size)
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return full_blocks * 4096 + block_size
    return full_blocks * 4096


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192

# whileLoop
x = 0  # inital value to variable
while x < 50:  # condition, so it is true
    print("Not there yet, x=" + str(x))  # body of loop
    x = x + 1  # body of loop, adding 1 and adding back to x
print("x=" + str(x))


def attempts(n):
    x = 1
    while x <= n:  # if True, then the go to the body of the loop
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(10)

my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1

y = 100
while y != 0 and y % 2 == 0:
    y = y / 2


def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0 and n != 0:
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False


def sum_divisors(n):
    x = 1
    sum = 0
    if n == 0:
        sum += n
    else:
        while n > x:
            while n % x == 0 and n != x:
                sum += x
                x += 1
            x += 1
    # Return the sum of all divisors of n, not including n
    return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51


# 114

def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number * multiplier
        # What is the additional condition to exit out of the loop?
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        multiplier += 1


multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24

# forLoop
for x in range(5):
    print(x)

values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("total sum: " + str(sum) + " average: " + str(sum / length))

product = 1
for n in range(1, 10):
    product = product * n

print(product)


# Conversion
def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):  # upto 3 parameters
    print(x, to_celsius(x))


# SquareSum
def square(n):
    return n * n


def sum_square(x):
    sum = 0
    for n in range(x):
        sum += x
    return sum


print(sum_square(10))

# nestLoop rangeOfDominos
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# nestedLoops
# for element1 in long_list:
# for element2 in long_list:
# do something(element1, element2)
# results in 27 hours of time

# use(range)
# for x in 25:
#    print(x) #errors out

for x in range(25):
    print(x)

for x in [25]:
    print(x)


def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)


greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])
greet_friends("Barry")


def factorial(n):
    result = 1
    for x in range(1, n + 1):
        result = result * x
    return result


for n in range(0, 10):
    print(n, factorial(n))

for x in range(1, 11):
    print(x ** 3)

x = 0
while x < 101:
    result = x * 7
    x += 1
    if result > 100:
        break
    print(result)


# not enough detail
# def retry(operation, attempts):
#  for n in range(attempts):
#    if operation():
#     print("Attempt " + str(n) + " succeeded")
#     break
#    else:
#      print("Attempt " + str(n) + " failed")

# retry(create_user, 3)
# retry(stop_service, 5)

# recursion(option)
def factorial(n):
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result


factorial(4)


def sum_positive_numbers(n):
    # The base case in n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding the number to
    # the sum of the number smaller than this one.
    return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3))
print(sum_positive_numbers(5))

# recursive Py calls max 1000
# factorial(1000) #pop error max recursion depth

# example of Recursive
# def recursive_function(parameters):
#    if base_case_condition(parameters):
#        return base_case_value
#    recursive_function(modified_parameters)

# week3 Quiz
# 1
number = 1
while number <= 7:
    print(number, end=" ")
    number += 1


# 2
def show_letters(word):
    for x in word:
        print(x)


show_letters("Hello")  # print one letter at a time


# 3
def digits(n):
    count = 0
    if n == 0:
        count = 1
        return count
    while n != 0:
        count += 1
        n = n // 10
    return count


print(digits(25))
print(digits(144))
print(digits(1000))
print(digits(0))


# 4
def multiplication_table(start, stop):
    for x in range(1, 4):
        for y in range(1, 4):
            print(str(x * y), end=" ")
        print()


multiplication_table(1, 3)


# 5
def counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting Down: "
        while x >= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x += 1
    return return_string


print(counter(1, 10))
print(counter(2, 1))
print(5, 5)


def even_numbers(maximum):
    return_string = ""
    for x in range(2, maximum + 1):
        if x % 2 == 0:
            return_string += str(x) + " "
    return return_string.strip()


print(even_numbers(6))
print(even_numbers(10))

# Failure to initialize variables below
# def decade_counter():
#    while year < 50:
#        year += 10
#    return year

for x in range(1, 10, 3):
    print(x)

for x in range(10):
    for y in range(x):
        print(y)


def votes(params):
    for vote in params:
        print("possible option :" + vote)


votes(['yes', 'no', 'maybe so'])

name = "Jaylen"
print(name[5])

text = "random string with alot of characters"
print(text[-1])

color = "Orange"
print(color[1:4])

fruit = "Pinnapple"
print(fruit[:4])
print(fruit[4:])

# str are immutable or can not be changed
message = "a kong string with a typo"
# message[2] = "l"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

message = "This is a new message"
print(message)

message = "And another one"
print(message)

pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("s"))  # just first s is returned
# print(pets.index("x")) #substring error, cause x is not in the string
"Dragons" in pets

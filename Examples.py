# Keywords https://docs.python.org/3/library/functions.html
# False	class	finally	is	return
# None	continue	for	lambda	try
# True	def	from	nonlocal	while
# del	global	not	with
# as	elif	if	or	yield
# assert	else	import	pass
# break	except	in	raise
from typing import Any, Union

print("Section 1*******************")
print("Hello World")

# add/subtract #multiply/Divide, so calculations as a simple/complex calculator
a = 4 + 5
b = 9 - 5
print(a + b)  # print function, prints the variables to the console

y = 4 * 3
z = 18 / 3
print(y + z)  # simple addition of two variables

# power/Sq Root
c = 4 ** 4
print(c)

c = (2 ** 10)  # 2*2*2*2*2*2*2*2*2*2 to the 10 power or see below as 2*2 10 times
print(c)

f = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
print(f)

b = (400 ** (1 / 2))
print(b)

# squareRoot
sq = (9 ** (1 / 2))
print(sq)

# d floor division (integer division)
d = 9 // 3
print(d)

d = 9 / 3  # float division, float being decimals
print(d)

e = 3 % 7  # modulo operator - returning the remainder of a problem or by dividing the left by the right,
print(e)

f = 3 & 4  # Equals 3  becuase 3 goes into 4 ZERO times, 3 remains
print(f)

# order Of Operations
x = (((90 + 10) * 4) ** (1 / 2))
print(x)

# Comments and Hello World from the BORG
hello = "Prepare to be borg'd, resistance is futile. You will be assimilated"
name = "USS Enterprise"
print(name + hello)

# disk size is 16 * 1024 3 times
disk_size = 16 * 1024 * 1024 * 1024
sector_size = 512
sector_amount = disk_size / sector_size

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
# print(pets.index("x"))
print("Dragons" in pets)  # false
print("Cats" in pets)  # in is conditional, true or false, is Dragon part of the string? And Cats?

word = "super dog"
print(word.index("d"))  # should return the index number for the letter d starting at 0

# replace old email with new
# def replace_domain(email, old_domain, new_domain):
# if "@" + old_domain in email:
# index = email.index("@" + old_domain)
# new_email = email[:index] + "@" + new_domain
# return new_email
# return email

# print used to print strings to console
# upper/lower case
print("mountains".upper())
print("MOUNTAINS".lower())

# strip white space, also includes print to console
print(" yes ".strip())
print(" yes ".lstrip())
print(" yes ".rstrip())

# count/Endswith/isnumeric and print to console
print("The number of times e e e occurs in this string is 5".count("e"))  # console print 6
print("Forest".endswith("rest"))  # true
print("Forest".isnumeric())
print("12345".isnumeric())
print(int("12345") + int("12345"))

# join/split and print to console
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple"]))
print("This is another example".split())

# diff. problem, strip letters, only print upper initial letters
# def initials(phrase):
# words = phrase.
# result = ""
# for word in words:
# result +=
# return

# print(initials("Universal Serial Bus"))  # Should be: USB
# print(initials("local area network"))  # Should be: LAN
# print(initials("Operating system"))  # Should be: OS

name = "Manny"
number = len(name) * 3
print("Hello {}, youcr lucky number is {}".format(name, number))
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name) * 3))


# Print Name and Grade
def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)


print(student_grade("Reed", 80))

# Format Expressions, format values with float up to 2 digits diff from default value
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))


# Celsius Calculation
def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(
        x)))  # > align right on 2 and 6, with float of 2 digits prints table of F | C 0,10, 101

weather = "Rainfall"
print(weather[:4])


def is_palindrome(input_string):  # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for letter in input_string.upper():
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if letter != ' ':
            new_string = new_string + letter
            reverse_string = letter + reverse_string
    # Compare the strings
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km


def nametag(first_name, last_name):
    return ("{} {}.".format(first_name, last_name[0]))


print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."

# def replace_ending(sentence, old, new):
#    if sentence.endswith(old):
# Using i as the slicing index, combine the part
# of the sentence up to the matched string at the
# end with the new string
#        i = len(old)
#        new_sentence = sentence[:-i] + new
#        return new_sentence

#    # Return the original sentence if there is no match
#   return sentence

# print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"

# Lists, is mutable or has the ability to change
x = ["Now", "we", "have", "a", "list"]
print(type(x))
print(x)
print(x[:3])
print(x[2:3])
print(x[1:3])
print(x[3:5])

print("a" in x)  # added print for py console
print("Today" in x)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

fruits.insert(1, "Orange")
fruits.insert(25, "Peach")  # insert at the end, 25 is above the index
print(fruits)

fruits.remove("Melon")  # Remove melon
print(fruits)

print(fruits.pop(4))
print(fruits)

fruits[2] = 'Strawberry'
print(fruits)

#  Tuples, immutable
fullname = ('Grace', 'M', 'Hopper')
print(fullname)


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


result = convert_seconds(5000)
print(result)

hours, mintues, seconds = result
print(hours, minutes, seconds)

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)


# Tuples Example in the text
def file_size(file_info):
    name, type, file_size = file_info
    return ("{:.2f}".format(file_size / 1024))


print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
print(file_size(('Program', 'py', 1239)))  # Should print 1.21

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animals)

print("Total Characters: {}, Average Length: {}".format(chars, chars / len(animals)))

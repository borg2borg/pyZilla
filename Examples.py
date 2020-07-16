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
    chars += len(animal)

print("Total Characters: {}, Average Length: {}".format(chars, chars / len(animals)))

winners = ["Ashely", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index +1, person))


# def skip_elementss(elements):
#    for index, element in enumerate(elements):
#    print("{} + {}".format(index +1, element))

#    return skip_elements()


#  print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
#  print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))


def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@example.com", "Alex Shay"), ("shaty@example.com", "Shaty May")]))

multiples = []
for x in range(1,11):
    multiples.append(x*7)

print(multiples)

#  list comprehension
multiples = [x * 7 for x in range(1,11)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
length = [len(language) for language in languages]
print(length)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [file.replace('.hpp', '.h') for file in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        say = say + word[1:] + word[0] + "ay "
        # Turn the list back into a phrase
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += '-'
    return result

print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------


def group_list(group, users):
  # members = users
  return "{}: {}".format(group, ','.join(users))

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


#def guest_list(guests):
#    for x in guests:
#        name, age, profession = x
#  print("{} is {} years old and works as {}".format(name, age, profession))

#  guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer

"""





#
#
#
#Lab 4
def format_address(address_string):
  # Declare variables
  house_number = 0
  street_name = ""
  # Separate the address string into parts
  separated_address = address_string.split()
  # Traverse through the address parts
  for address in separated_address:
    # Determine if the address part is the
    # house number or part of the street name
    if address.isnumeric():
      house_number = address
  # Does anything else need to be done
  # before returning the result?
    else:
      street_name += address + " "
  # Return the formatted string
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"



def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order
    list1.reverse()
    list2.extend(list1)
    return list2


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))



def squares(start, end):
	return [ n*n for n in range(start, end+1) ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaa"))
print(count_letters("tenant"))
print(count_letters("a long string"))


def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for price in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])


colors = ["red", "white", "blue"]
print(colors.insert(2, "yellow"))


host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())


def car_listing(car_prices):
  result = ""
  for name, price in car_prices.items():
    result += "{} costs {} dollars".format(name, price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))



def combine_guests(guests1, guests2):
  new_guest_dictionary = {}
  # Combine both dictionaries into one, with each key listed
  new_guest_dictionary.update(guests2)
  # only once, and the value from guests1 taking precedence
  new_guest_dictionary.update(guests1)
  return new_guest_dictionary
Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))



def count_letters(text):
  result = {}
  text = text.replace(" ", "")
  # Go through each letter in the text
  for letter in text.lower():
    # Check if the letter needs to be counted or not
    if letter.isalpha():
      if letter not in result:
        result[letter] = 0
      # Add or increment the value in the dictionary
      result[letter] += 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


print(animal[3:6])
print(animal[-5])
print(animal[10:])


colors = ["red", "white", "yellow", "blue"]
colors.insert(2, "yellow")


host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()


# Dictionaries

# pairs and key values, str, int, tuples etc
#  Mutable

#Key - Word (wurd) (n.)
#Definition or Value 1. a unit of language....

x = {}
type(x)
print(type(x))

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

print(file_counts["txt"])
print("jpg" in file_counts)  # T or F is JPG in the dictionary?
print("java" in file_counts)  # Same as above but is java?

file_counts["cfg"] = 8
print(file_counts)

file_counts["csv"] = 17
print(file_counts)  # value replaces 17 for 2, are unique

del file_counts["cfg"]
print(file_counts)

# Example
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?

#input Key "" value:X
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)

for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))

#file_counts.keys()
#dict_keys(['jpg', 'txt', 'csv', 'py'])
#file_counts.values()
#dict_values([10, 14, 2, 23])
#for value in file_counts.values():
#    print(value)

#set - store values only present once and immutable

#cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
#for item in cool_beasts.items():
#print("{} have {}".format(item))


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaa"))
print(count_letters("tenant"))
print(count_letters("a long string"))


# Lists - ip addresses or hostnames and ip addresses,any data type
# dictionaries - usernames, groups - specific element any data type for value but keys have to be specific
# numbers, booleans, strings or tuples dict keys
#keys - keys, or even dictionaries


def email_list(domains):
	emails = []
	for domain_name, users in domains.items():
	  for user in users:
	    emails.append(user + "@" + domain_name)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user in user_groups:
				user_groups[user].append(group)
			else:
				user_groups[user] = [group]
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))




def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for price in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44
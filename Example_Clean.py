"""
Table of Contents
# Week 1
# Week 2
"""

# Week 1, adding print to console, syntax, calcs, operators and For

print("----- Week 1 -----")
print("Hello World")  # print a str -----
print(5 * 5)  # print a calc -----
print(5 > 5)  # print boolean -----

# Variable "x" equals a str of text and print to console -----
x = "I'm programming in Python"
print(x)

# Print variable string to the console with an additional string -----
name = "Eli"
print("Hello, my " + name + ", it is nice to meet you.")

# Negation of special characters, print variable strings to console -----
color = "Greeen"
thing = "Thing"
print("The " + color + " " + thing + " \"Swamp " + thing + "\" " + "is one of the most terrifying beast of lore")

# Additional Calcs, addition squared, power(s) and square root -----
x = (((1 + 2) * 3) / 4) ** 5
print(x)

y = 4 ** (1 / 2)
print(y)

# for
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print(friend)  # Print names within the list -----

# For loop, while this condition is true, return value within the "Range" of 1 - 10 -----
for i in range(10):  # colon to start the statement -----
    print("Hello world, again")  # Print str 10 times -----

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
# New Adding section per week -----
# Week 1 Quiz/Module  Review -----
print("-----Week 1 Quiz/Module Review -----")
#  Print string to console
print("Programming in Python is, is like Godzilla wrecking it's favorite city building")

#  Ratio with sqRoot -----
ratio = ((1 + 5 ** (1 / 2)) / 2)
print(ratio)

#  add two strings, print -----
color = "Yellow"
thing = "Sunflower"
print(color + " is the color of " + thing + " on Siesta beach")

#  Print Calc -----
print(86400 * 7)

password = 26 * 26 * 26 * 26 * 26 * 26
print(password)

# Print Sector Amount, when Disk Size is divided by Sector Size -----
# hard drives are 'divided' into Sectors of 512 bytes, Disk size osf 16gb - Disk Si -----
disk_size = 16 * 1024 * 1024 * 1024  # Given 16gb * 1024**3 -----
sector_size = 512
sector_amount = disk_size / sector_size

print(sector_amount)  # Print Sector Amount -----

'''
Week 2
Expressions, Variables, Functions, and Conditionals
'''
print("----- Week 2 -----")
# Types, strings, floats, integers, boolean -----
print(type("Hello" + 'Hello with single quotes'))
print(type(20.22))
print(type(22 % 2))

x = 22 < 23
print(type(x))

#  Variables, added -----
length = 10
width = 2
area = length * width

print(area)

#  Expressions are a combo of numbers, symbols or other variables that produce a result -----
# Do use - start with a letter or underscore(_) Do NOT Use - py keywords or functions -----
base = 5
height = 3
area = base * height / 2

print(area)

print(7 + 8.5)  # Converted 7 to float and calc or implicit conversion same with sentences -----

# Explicit Conversion requires a type, in this example it will be str() -----
base = 6
height = 3
area = (base * height) / 2

print("The area of a triangle is base * height divided by 2 equaling: " + str(area))  # string of 9.0 -----

# Short Test/Check
total = 2048 + 4357 + 97658 + +125 + 8
files = 5
average = total / files

print("The average size is " + str(average))  # 20839.2 -----

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

# 2 integers / 1 by the other so that result = 1 -----
numerator = 10
denominator = 10
result = numerator / denominator

print(int(result))  # print 1 -----

word1 = "How "
word2 = "do "
word3 = "you "
word4 = "like "
word5 = "Python "
word6 = "so "
word7 = "far?"
wordAll = word1 + word2 + word3 + word4 + word5 + word6 + word7

print(str(wordAll))  # How do you like Python so far? -----

# convert to string
print("2 + 2 = " + str(2 + 2))  # 2 + 2 = 4 as a string -----


# Week 2 - Functions and Conditionals
# def = definition of variable -----
def greeting(name):  # INCLUDE : semi color - defining greeting parameter is name

    print("Welcome, " + name)  # Welcome, name parameter below -----


greeting("Eli")


def greeting(name, department):  # defining greeting with two parameters name, department -----

    print(
        "Welcome, " + name + "you are within the " + department + " department, correct?")
    # Welcome, name parameter below  -----


greeting("Eli", "IT CyOps")


def print_seconds(hours, minutes, seconds):
    print(hours * 3600 + minutes * 60 + seconds)  # Equals 3723 seconds in total -----
    print(str(hours * 3600) + " = HOURS")
    print(str(minutes * 60) + " = MINUTES")
    print(str(seconds) + " = SECONDS")
    print(str(3600 + 120 + 3) + " Equals in Seconds")


print_seconds(1, 2, 3)


def area_triangle(base, height):
    return base * height / 2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b

print(area_a)
print(area_b)
print(area_a + area_b)  # print 20.5 -----
print("The sum of both areas is: " + str(sum))  # print The sum of both areas is: 20.5 -----

'''
def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)
'''


def get_seconds(hours, minutes, seconds):
    return 3600 * hours + 60 * minutes + seconds


amount_a = get_seconds(2, 30, 0)
print(amount_a)  # 9000 -----
amount_b = get_seconds(0, 45, 15)
print(amount_b)  # 2715 -----
result = amount_a + amount_b
print(amount_a + amount_b)

print(result)  # match above -----


def convert_seconds(seconds):
    hours = seconds // 3600
    print(hours)  # print 1 ----
    minutes = (seconds - hours * 3600) // 60
    print(minutes)  # print 23 -----
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    print(remaining_seconds)  # print 20 -----
    return hours, minutes, remaining_seconds  # 3 numbers -----


hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)


# Return None value ----
'''
def greeting(name):
    print("Welcome, " + name)

result = greeting("Christine")
print(result)  # none returned value, special data type - indicate empty or return nothing -----

Return value or pass data back to the user/console when a function is called
That data passed back can be stored value and stored as a variable
'''

# Code RE-use -----
name = "Kendra"
number = len(name) * 9  # len, length of string KENDRA k being 1, E being 2... so 6 * 9 = 54. Therefore number is 64

print('Hello ' + name + ", your lucky line number is " + str(number))


# or for RE-use purposes, let's switch this around ----

def lucky_number(name):
    number = len(name) * 9
    print('Hello ' + name + ", your lucky line number is " + str(number))


lucky_number("Kendra")  # 6 characters
lucky_number("Cameron")  # 7 characters


# Reuse duplicate code for the same code -----
def month_days(month, days):
    print(str(month) + " has " + str(days) + " days.")


month_days('June', 30)
month_days('July', 31)


# Calc area of a circle -----
def circle_area(radius):
    pi = 3.14
    cir_area = pi * (radius ** 2)
    print(cir_area)


circle_area(5)  # print 78.5  -----

'''
Week 2
Functions
'''
print("----- Week 2 Quiz - Functions  -----")


# convert Miles (M) to Kilometers (km) -----
def convert_distance(miles):
    km = miles * 1.6
    return km


miles = 55
km = convert_distance(miles)

print("The distance in kilometers is " + str(km))  # "String": 88.0 -----
print("The round-trip distance in kilometers is " + str(km * 2))  # "String": 176.0 -----


# reorder numbers smaller to bigger -----
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1


smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)  # 99 100 -----

smaller, bigger = order_numbers(2, 1)
print(smaller, bigger)  # 2 1 -----


def lucky_numbers(name):
    number = len(name) * 9
    print("Hello " + name + "." + "Your lucky number is " + str(number))


lucky_number("Cassandra")  # 9*9 81 -----
lucky_number("Oscar")  # 5*9 45 -----

'''
Week 3 Conditionals, < > != <= >= == and or not
'''
print(10 > 1)  # True -----
print(10 > 1 and 10 > 2)  # True -----
print(25 > 50 or 1 != 2)  # True -----
print(not 42 == "Answer")  # True -----
print(not 42 == 42)  # False -----


# Branching, like if elif else -----
def hint_username(username):
    if len(username) < 3:  # if true, run the if statement, otherwise skip -----
        print("Invalid, Must be at least 3 char long")
    else:
        print("You did it, this username is valid!")


hint_username("User")


# Simple if Else where one statement is true returned true, where the other is returned false ----
def is_positive(number):
    if number > 0:
        return True
    else:
        return False


is_positive(-100)
print(is_positive(-100))  # False -----
is_positive(1000)
print(is_positive(1000))  # True -----

# modulo return integer division quotient (number divisible evenly) is x, remainder is y and exits code-----
# example would be
print(4 % 2)  # 0 being no remainder -----
print(5 % 2)  # 1 being the remainder or modulo of 5 -----
print(float(43 / 7))  # 6 w remainder of 6.14285... therefore not 0, and considered != 0

rem3 = 43 % 7
print(rem3)  # 3
print(float(43 / 7))  # 6 w remainder of 6.14285... therefore not 0, and considered != 0

'''
Example of modulo usage - https://www.jquery-az.com/python-modulo/
year_input = int(input("Enter a year:  "))

if year_input % 4 == 0:
    print("Remainder is 0 so ", year_input, "is a leap year!")
else:
    print(year_input, "Not a leap year!")
    
    
Additional Detail
% integer division, but only returns the remainder of this division operation. 
If we’re dividing 5 by 2, the quotient is 2, and the remainder is 1. 
Two 2s can go into 5, leaving 1 left over. So 5%2 would return 1. 
Dividing 10 by 5 would give us a quotient of 2 with no remainder, since 5 
can go into 10 twice with nothing left over. In this case, 10%2 would return 0, as there is no remainder.
'''


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


is_even(9)
print(is_even(9))  # False, 99 % 2 is no 1 -----
is_even(8)
print(is_even(8))  # False, 99 % 2 is no 1 -----


def hint_username(username):
    if len(username) < 3:
        print("Invalid. Must be 3 characters or more.")
    elif len(username) > 15:
        print("Invalid. Must be less than 15 characters.")
    else:
        print("Valid, please proceed to the next round")


hint_username("User")
hint_username("Us")
hint_username("UserNumberThree")
hint_username("JackSallee")


# Return Positive, Negative or Zero -----
def number_group(number):
    if number > 0:
        return "Positive"  # True -----
    elif number < 0:
        return "Negative"  # When True -----
    else:
        return "Zero"  # Otherwise if not > or <, it is 0 -----


number_group(10)
number_group(-10)
number_group(0)

'''
Week 2
Functions
'''
print("----- Week 2 Quiz - Conditionals  -----")


def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor!"
    else:
        return "Hello there, " + name


print(greeting("Taylor"))
print(greeting("John"))

if number > 11:
    print(0)
elif number != 10:
    print(1)
elif number >= 20 or number < 12:
    print(2)
else:
    print(3)

print("A dog " + "A mouse")  # 5 vs 7 ----
print(9999 + 8888 + 100 * 100)  # 18887 vs 10000 -----


def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = (filesize % block_size)
    if partial_block_remainder > 0:
        return full_blocks * 4096 + block_size
    return full_blocks * 4096


print(calculate_storage(1))
print(1 // 4096 * 4096)
print(calculate_storage(4096))
print(4096 // 4096 * 4096)
print(calculate_storage(4097))

print(4097 // 4096 * 4096 + 4096)
print(calculate_storage(6000))
print(6000 // 4096 * 4096 + 4096)

# Should be 4096 -----
# Should be 4096 -----
# Should be 8192 -----
# Should be 8192 -----

'''
Week 2 Module Quizzes and Review
'''

print("Week 2 Module Quiz  ---------------------")


def color_translator(color):
    if color == "red":
        hex_color = "#ff000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown color"
    return hex_color


print(color_translator("blue"))
print(color_translator("yellow"))
print(color_translator("red"))
print(color_translator("black"))
print(color_translator("green"))
print(color_translator(""))
print(color_translator("Purple"))


# Try and order if, elif and else statements in order down from highest number, for some reason it didn't work otherwise
def exam_grade(score):
    if score == 100:
        grade = "Top Score, congrats!"
    elif score >= 95:
        grade = "Awesome work, congrats."
    elif score >= 60:
        grade = "Pass"
    elif score <= 10:
        grade = "Please come see me, we need to review the test together."
    else:
        grade = "Fail"
    return grade


print(exam_grade(95))
print(exam_grade(62))
print(exam_grade(55))
print(exam_grade(60))
print(exam_grade(61))
print(exam_grade(58.5))
print(exam_grade(94.5))
print(exam_grade(100))
print(exam_grade(0))

# Modulo question
x = 11 % 5  # 5 goes into 11 2 times (quotient), with a (remainder) of 1, passes back 1
print(x)

# Modulo #2
y = 10 % 5  # 5 goes into 10 2 times (quotient), with a (remainder) of 0, passes back 0
print(y)


def format_name(first_name, last_name):
    if first_name != "" and last_name != "":  # if both strings are not empty, return first_name, last_name
        return "Name: " + last_name + ", " + first_name
    elif first_name == "" and last_name != "":  # if string for last_name is not empty, return last_name
        return "Name: " + last_name
    elif first_name != "" and last_name == "":  # if string for first_name is not empty, return first_name
        return "Name: " + first_name
    else:  # Else return empty strings for first_name and last_name, return empty ""
        return ""


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))


# Should return an empty string


def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):  # if Chair is longer than Couch & Chair longer than table
        word = word1
    elif len(word1) <= len(word2) and len(word2) >= len(word3):  # if bed shorter than bath, bath is longer than beyond
        word = word2
    else:  # word 3 most be the longest of all
        word = word3
    return word


print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


def sum_input(x, y):
    return x + y


print(sum_input(sum_input(1, 2), sum_input(3, 4)))  # print 3 + 7 = 10

x = ((10 >= 5 * 2) and (10 <= 5 * 2))
print(x)  # True, 10 >= 10 and 10 <= 10 due to the = operator


def fractional_part(numerator, denominator):
    if denominator != 0:
        return (numerator % denominator) / denominator
    elif denominator == 0:
        return 0
    else:
        return 0


print(fractional_part(5, 5))  # Should be 0, 5/5 = 1

print(fractional_part(5, 4))  # Should be 0.25
print(fractional_part(5, 3))  # Should be 0.66.
print(fractional_part(5, 2))  # Should be 0.5
print(fractional_part(5, 0))  # Should be 0
print(fractional_part(0, 5))  # Should be 0

'''
Week 3
While Loops, For Loops, Recursion

While Loops instruct your computer to continuously execute your code based on
the value of a condition

Another example

While loops are great when the process is repeatable, a repeatable action until a condition changes

'''

print("----- Week 3 - While loops  -----")

x = 0
while x < 5:  # while x is 0 as the initial value it is less than 5, also the loop will continue to execute while True
    print("Not there yes, x=" + str(x))  # print statement string plus number string
    x = x + 1  # x will equal that number + 1 until x is 5, which makes the above while loop false and kick out
    # This will continue to print the statement plus the number until x = 5, which will print below

print("x=" + str(x))  # When x = 5, then just print x = 5


def attempts(n):  # define attempts as n
    x = 1  # initial value of x, so the statement will start at 1
    while x <= n:  # while x is less than or equal to n is true
        print("Attempt " + str(x))  # print statement string plus x value
        x += 1  # expression x + 1 until the value of x is <= n or bigger than n


print("Done")  # When x less than so 1 -4 and equal to n which equals 5 attempts

attempts(5)  # attempt is defined as try while loop 5 times or attempts

my_variable = 5  # Variable is 5
while my_variable < 10:  # And, while that variable of 5 is less than 10
    print("Hello")  # Print hello each time my_variable runs
    my_variable += 1  # increment += 1 each time, so increment by adding 1 each time the while loop runs

x = 1
sum = 0
while x < 10:
    sum += x  # increment 0 by 1
    x += 1  # increment 1 by 1

product = 1  # missing x
x = 1  # adding x = 1 will allow this to run/ w.o it will print 1
while x < 10:
    product = product * x
    x += 1  # should equal 362880

print(sum, product)


def count_down(current):
    while (current > 0):
        print(current)
        current -= 1  # Must call current, give it a value and increment 'down' from count_down "4 " number
    print("Zero!")  # Print zero when the while loop is great than 0 or = 0


count_down(4)

'''
using variables that are NOT defined, or Named Error
x = 1

Be aware for infinite loop
while x % 2 == 0:
    x = x / 2

print(x)


Python used 'Break' or like JS 'pop'
'''


def print_range(start, end):
    n = start
    while n <= end:
        print(n)
        n += 1  # MUST Add n+= 1


print(print_range(1, 5))

'''
Week 3 Quiz - While loop
'''

print("----- Week 3 - Quiz While loops  -----")


def print_prime_factors(number):
    factor = 2  # Multiplying factor of number
    while factor <= number:  # while the factor of 2 < = to 100
        if number % factor == 0:  # Number is a divisor of 100 % 2 == 0
            print(factor)  # print factor, in this case 2
            number = number / factor  # take the number 100 = 100/2 equals 2
        else:  # otherwise if
            factor += 1  # increment factor or 2 += by 1 and return done
    return "Done"


print_prime_factors(100)


def is_power_of_two(n):
    while n % 2 == 0 and n != 0:  # While the number's modulo '%'  2 == 0 and the number is not 0
        n = n / 2  # number = number / 2
    if n == 1:
        return True
    return False


print(is_power_of_two(0))  # 0 % 2 = 0 and it is 0 so returns False -  False
print(is_power_of_two(1))  # 1 % 2 = 1 and it's not 0, 1 ==1 returns True - True
print(is_power_of_two(8))  # 8 % 2 = 0 4 is not 0, 4 = 4 / 2 returns True - True
print(is_power_of_two(9))  # 9 % 2 = 1 and it's not 0 and not == 1 so return False - False


def sum_divisors(n):
    x = 1  # Variable x = 1
    sum = 0  # Variable sum = 0
    if n == 0:  # if sum_divisor 0
        sum += n  # increment by 0, 3, 36, 102
    else:  # else sum_divisor != 0 so, 3, 36, 102
        while n > x:  # sum_divisor = 3, 36, 102 is greater than 1
            while n % x == 0 and n != x:  # while 3, 36, 102 % equals 0 and 3, 36, 102 is not 1
                sum += x  # increment 0 by 1
                x += 1  # increment 1 by 1
            x += 1  # increment 1 by 1
    return sum  # return sum +1


print(sum_divisors(0))
print(sum_divisors(1))
print(sum_divisors(3))
print(sum_divisors(36))  # 1+2+3+4+6+9+12+18 equals 55
print(1 + 2 + 3 + 4 + 6 + 9 + 12 + 18)
print(sum_divisors(102))  # 2+3+6+17+34+51 equals 114
print(1 + 2 + 3 + 6 + 17 + 34 + 51)


def multiplication_table(number):
    multiplier = 1  # multiplier variable equals 1
    while multiplier <= 5:  # expression or condition, while 1 is < or equal to 5
        result = number * multiplier  # the result is equal to a number * 1
        if result > 25:  # condition, if this result * 1 is greater than 25,
            break  # break and print i.e in this example 3 * 6
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1  # increment the multiplier until the result is greater than 25, again 3 * 6


multiplication_table(3)  # shall print 3*1 - 3*5
multiplication_table(5)  # 5*1 - 5*5, because the result has to be greater than 25, i.e. 5 * 6 would be in this case

'''
Week 3 - For loops

For  - in: don't forget the colon
"For" loops are great when a sequence of elements(strings, numbers etc.) which you would like iterate over
'''

'''
for x in range(5):  # expression for a variable within a "range" of numbers, value 0 by default and ending at 5
    print(x)  # shall print list 0 - 4
'''


def square(n):  # define square with the parameter n
    return n * n  # return parameter of n * parameter of n, 10 * 10


def sum_squares(x):  # define sum squares with the parameter x
    sum = 0  # sum initial value is 0
    for n in range(1, x + 1):  # expression, while the parameter n, 10 in range of x
        sum += x and x != 0  # increment by parameter x or 10, and 10 != 0
    return sum  # return the sum variable


print(sum_squares(10))  # # 3,5,7,9,11 - 285

# string type for loop
friends = ['Taylor', 'Alex', 'Pat', 'Eli']  # variable friends is a list of friend(s)
for friend in friends:  # for each friend in the variable list of friends
    print("Hi " + friend)  # print string and friend name in list, "Hi Taylor....

# number type for loop
values = [23, 52, 59, 37, 48]  # variable values is a list of numbers
sum = 0  # sum variable = num 0
length = 0  # sum variable = num 0
for value in values:  # for each value in the variable list of values
    sum += value  # sum total each value 23, 52..
    length += 1  # take length which initial value is 0 and increment by 1 and list has 5 numbers, therefore length = 5
    # 23+52+59+37+48
    # 23+52+59+37+48/5

print("Sum: " + str(23 + 52 + 59 + 37 + 48))
print("Average: " + str(219 / 5))
print("Total sum:" + str(sum) + " - Average: " + str(sum / length))

product = 1  # product variable equals 1
for n in range(1, 10):  # for n in range from 1 to 10
    product = product * n  # product of 1 = product 1 * range 1 - 10 or 1*2*3*4*5*6*7*8*9

print(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9)  # So, he is the answer in long form to check the input
print(product)


# Test Example for Factorials
def factorial(n):  # define factorial parameter n
    result = 1  # variable initial value is 1
    for i in range(1, n + 1):  # i in range between 1 and n+1 = 5
        result = result * i  # so 1 = 1 * 1 - 4 AND 1 - 5
    return result


print(1 * 2 * 3 * 4)
print(factorial(4))
print(1 * 2 * 3 * 4 * 5)
print(factorial(5))
print(1 * 2 * 3 * 4 * 5 * 6)
print(factorial(6))


def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    print(x, to_celsius(x))

print(0 - 32 * 5 / 9)  # 32 * 0.55 repeating
print(1 - 32 * 5 / 9)
print(10 - 32 * 5 / 9)

'''
To quickly recap the range() function when passing one, two, or three parameters:
One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
Two parameters..., one-by-one, from the first parameter to one less than the second parameter.

Three parameters... starting with the first parameter and stopping before the second parameter, 
but this time increasing each step by the third parameter.
'''

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

teams = ["Dragons", "Wolves", "Shark", "Pandas", "Unicorns", "Gators"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

for x in [25]:  # print x in 25, it would be 25
    print(x)


def greet_friends(friends):
    for friend in friends:
        print("Hi friend, you are " + friend)


greet_friends(['Taylor', 'Wayne', 'Bruce', 'Wayne 2', 'Anne', 'Lisa', 'Francis'])  # List
greet_friends("Barry")  # element

'''
def validate_users(users):
    for user in users:
        if valid(user):
            print(user + " is valid")
        else:
            print(user + "is invalid")


validate_users(['purplecat'])
'''

'''
Week 3 For loops
'''
print("----- Week 3 - Quiz for loops  -----")


def factorial(n):  # define factorial with the parameter n
    result = 1  # the result  of the for loop is equal to 1
    for x in range(1, n + 1):  # while x in a range 1 plus parameter n, increment 1 number until we get to the number
        result = result * x  # the result will be result of 1 * x in the range of 1 to n+1

    for n in range(0, 10):  # now, n is in a range of 0 and 10
        print(n, factorial(n, n + 1))  # print each number from 0 to 10, the factorial times the number


for x in range(1, 11):  # def x within a range from 1 to 11
    print(x ** 3)  # print x, those numbers between 1 and 11, by the power of 3

x = 0
while x < 101:
    result = x * 7
    x += 1
    if result > 100:
        break
    print(result)

'''
def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("attempt " + str(n) + " succeeded")
            break
        else:
            print("attempt " + str(n) + "failed")


print(retry(str(create_user), 3))
print(retry(str(stop_service), 5))
'''

'''
Option Recursion
'''


def factorial(n):
    print("Factor called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " for factor of " + str(n))
    return result

factorial(4)



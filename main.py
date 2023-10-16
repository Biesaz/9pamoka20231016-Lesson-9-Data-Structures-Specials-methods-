# Lesson 9: Data Structures: Specials methods

# Data Structure: Special methods
# In this lecture we will review some additional functionalities of python built-in data structures. And also review math library

# List comprehensions
# It is a very useful way of making your loops more compact/ readable/ understandable.

# Example:

# Let's say you want a program that gets first 10 perfect squares, how do you do it?

# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)
# It works just fine, but there is a bit nicer way of writing this down which is even more human readable:

# squares = [number * number for number in range(10)]
# print(squares)
# Neat isn't it? All it does is the following:

# creates squares as a list.
# inside of the list it says that we are looping all the numbers in range(10)
# each object in the list is going to be that number in the loop multiplied by the number: number * number
# What is more, what if we wanted to have all the perfect squares except 25? Try writing this one down without list comprehension.

# The implementation with list comprehension:

# squares = [number * number for number in range(10) if number != 5]
# print(squares)
# Boom, simple yet efficient and still super human readable.

# Now trying writing down a list comprehension yourself that would only return perfect square of even numbers:

# Answer

# squares = [number * number for number in range(10) if number % 2 == 0]
# print(squares)
# Alright for now we have seen such numbers with only integers, but can we work with strings too? Ofcourse!

# let's say you have list of names and want to filter our only the ones starting with certain letter:

# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A")])
# You can even chain more logic with and and or clauses as well:

# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A") or "e" in name])
# As you can see you can chain as much logic as you want to here. But it is best to keep there list comprehensions as short as possible because if you have too much logic here, it might become impossible to understand even for you after couple of days...

# Note ❗ The list, set, tuple comprehensions work exactly the same except that outer brackets are different, everything else stays the same.
# Dictionary comprehensions
# Dictionaries also have this fancy one liner comprehension functionality:

# Let's say we have the same problem of perfect squares but we want to have number: percect_square structure like this: {1: 1, 2: 4, 3: 9} Try writing this without dictionary comprehension yourself.

# Dictionary comprehension example:

# squares = {i: i * i for i in range(10)}
# print(squares)
# Try doing both exercises done with lists:

# program without perfect square of 5.
# only odd numbers.
# Enumerate
# Let's imagine we have a python loops over some items in the list:

# values = ["a", "b", "c"]

# for value in values:
#     print(value)
# it is a simple nice loop, that does all it has to. Now imagine you also want to get the corresponding index of the item. How would you do it?

# You could do something like this:

# values = ["a", "b", "c"]
# index = 0

# for value in values:
#     print(index, value)
#     index += 1
# So here we have an integer that increments with each iteration and it also works. But too keep our code simpler we may use python build int function enumerate()

# values = ["a", "b", "c"]
# for count, value in enumerate(values):
#     print(count, value)
# If we wanted to change the start count:

# values = ["a", "b", "c"]
# for count, value in enumerate(values, start=1):
#     print(count, value)
# If we go a bit crazy we can combine two things we learned today:

# def even_items(numbers: list):
#     return [v for i, v in enumerate(numbers, start=1) if not i % 2]

# seq = list(range(1, 11))

# print(even_items(seq))
# Go through this once yourself, operate small things out and combine them together once again.

# NOTE enumerate returns an iterator so if you want to look what's inside you can either loop through it or convert it to list.

# math library
# for many math specifics you can use math library in python. It is a built in library simply just:

# import math
# and you are good to go.

# For example if you wanted to calculate a circle area:

# import math
# area = 5 * 5 * math.pi
# math.pi here is a constact which we can you straight out of the box.

# There are plenty more functions we could spend all day reviewing this library cause it's huge, but let's look into couple of more functions.

# factorial
# For example if we wanted to calculate factorial: 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1

# We could write a function ourselves, but actually it is already available to us:

# import math
# math.factorial(7)
# What is more it is actually quite optimised as well.

# ceil() and floor()
# All there functions do is that if you have a float value, it can literaly get "floor" or "ceiling" of it. Examples:

# import math


# print(math.ceil(6.1))

# print(math.floor(-11.1))
# Is this clear?

# power functions
# Let's say you want to have a number raised by the power of n: 5^5 = 5 * 5 * 5 * 5 * 5 = 3125

# Do this without math.

# with math:

# import math

# print(math.pow(5, 5))
# square root
# import math
# print (math.sqrt(9))
# There are many more things in math library as said before, here we reviewed just a tiny bit. But bottom line is that if you ahve something to do with math, logarithms, working with angles, trigonometry etc.

# Real Python math

# Exercises 🧠 :
# 1.
# Find all of the numbers from 1-1000 that are divisible by 6.
# divisible_six = [number for number in range(1000) if number % 6 == 0]
# print(divisible_six)

# 2.
# Find all number from 1-1000 that have 9 in them.
nine_in = [number for number in range(1000) if '9' in str(number)]
print(nine_in)

# Given string: text = 'In this lecture we will review some additional functionalities of python built-in data structures.' calculate how many words have letter 'e' in it.
# Given the same string as in previous exercise: calculate count of letters that have more than 5 characters.
# Write a program that checks if given number is a perfect square.


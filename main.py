# Lesson 9: Data Structures: Specials methods

# Data Structure: Special methods
# In this lecture we will review some additional functionalities of python built-in data structures. And also review math library

# # List comprehensions
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

names = ["Albert", "Alma", "Joseph", "Zoro"]
print([name for name in names if name.startswith("A") or "e" in name])
# As you can see you can chain as much logic as you want to here. But it is best to keep there list comprehensions as short as possible because if you have too much logic here, it might become impossible to understand even for you after couple of days...

# Note ❗ The list, set, tuple comprehensions work exactly the same except that outer brackets are different, everything else stays the same.



# Exercises 🧠 :
# 1.
# Find all of the numbers from 1-1000 that are divisible by 6.
# divisible_six = [number for number in range(1000) if number % 6 == 0]
# print(divisible_six)

# 2.
# Find all number from 1-1000 that have 9 in them.
# nine_in = [number for number in range(1000) if '9' in str(number)]
# print(nine_in)



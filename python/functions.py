# Functions

"""
## General Principles

- Don't reuse function names, i.e. don't create your own print().
- Don't shadow variables within a function.
- You can't call a function before it's defined. Python doesn't hoist.
- Put global variables above functions for clarity.
- Functions return None by default.
- Generally not recommended to return different types of data from a function

"""

def hello():
    print('Hello')

# Brackets after the variable name invokes the function
# hello()

def user_age_in_seconds():
    user_age = int(input('Enter your age: '))
    age_seconds = user_age * 365 *24 * 60 * 60
    return f'Your age in seconds is {age_seconds}.'

""" 
## Parameters and Arguments

- If there are no params passing args results in an error.
- If there are params and not passing args results in an error.

"""

def add(x, y): # x, y are called parameters
    return x + y

add(1, 3) # 1, 3 are called arguments

def say_hello(first_name, surname):
    return f'Hello, {first_name} {surname}.'

# Positional arguments
# The function assigns the args to params in the order they are passed.
say_hello('Jane', 'Doe')

# Named/Keyword arguments
# The function assignes the arg to the parameter with the same name.
# Don't use a space either side of the =
say_hello(surname='Doe', name='Jane')

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You can't divide with a divisor of 0!"

# Keyword args can make your code easier for others to understand
divide(dividend=15, divisor=0)

divide(dividend=15, 0) # Positional args must be first if using keyword args
divide(15, divisor=0) # This will not error


""" 
## Default Parameter Values

- Default parameters can't be followed by a required parameter in func declaration
- Don't decalare function default params globaly

"""

def addition(x, y=8): # y defaults to 8 if only 1 arg is passed
    return x + y

def subtract(x=5, y): # Will error, default params must follow required params
    return x - y

default_y = 3

def multiply(x, y=default_y):
    return x * y

# multiply(2) -> 6
default_y = 5
# multiply(2) -> 6
#
# The y param of multiply() is set when the code is parsed,
# not when the function is run.
# This is why later changing the gloabl var doesn't change the functions
# defualt param.
# You shouldn't reference global vars as default func params for this reason.


""" 
## Lamda Functions

- A type of function with no name that is used to return a value
- Lamda functions can be named but are normally used inline
- Almost always single line

"""

# A lamda version of add() from earlier
# Four parts to a lamda function
# lambda = declare it's a lambda function
# x, y = declare the params
# : = seperate the params from the return
# x + y = declare the return value
lambda x, y: x + y


(lambda x, y: x + y)(5, 7) # An invoked lambda

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]

# list comprehension version, usually slightly faster
doubled = [double(x) for x in sequence]
# Map version
doubled = map(double, sequence)
# Lamda version
doubled = list(map(lambda x: x * 2, sequence))
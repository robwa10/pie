# Unpacking Function Arguments

"""
## Function params

- args passes in a tuple
- *args unpacks the tuple before passing them in

"""

def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total

# print(multiply(1, 3, 5))


"""
## Passing multiple arguments

"""

def add(x, y):
    return x + y

nums = [3, 5]

# Destructures the list into the variables
# i.e. add(3, 5)
# print(add(*nums))
# You must have same number of arguments and params

# Destructuring dicts as names args
dict_nums = {"x": 15, "y": 25}
# print(add(**nums)) # Passes key/value pairs as named keyword args


def apply(*args, operator):  # This turns operator into a required keyword arg
    pass


"""
## Unpacking Keyword arguments
 - '**' collects keyword arguments
"""

def named(**kwargs):
    print(kwargs)

# named(name='Jane', age=25)


# You can also unpack a dict into named arguments
details = {'name': 'Bob', 'age': 25}

# named(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')

# print_nicely(**details)


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, **details)

# Example he talks about

def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
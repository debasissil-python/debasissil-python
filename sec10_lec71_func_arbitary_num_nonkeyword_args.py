# *args - Only applicable with non-keyword arguments. It can take any number of arguments.

# Anything can be passed in *args. 
# * - here anything can be passed
# args - it is used for convention but any variable can be used
# You cannot have keyword arguments here

def func(*args):
    return args
# What you get is a tuple
print (func(1,2,3,'hallo', 'world'))


def func(*args):
    return type(args)
# What you get is a type of args - <class tuple>
print (func(1,2,3,'hallo', 'world'))


# To find mean of a list with unlimited numbers (int or float)
def mean(*args):
    return sum(args) / len(args)

print (mean(2,3,4,5,6))


# A list with unlimited number of str - Giving all in uppercase and alphabatically sorted

def str_upper_sorted(*args):
    return str(sorted(list(args))).upper()

print (str_upper_sorted('apple', 'orange', 'guava','cherry', 'blueberry', 'kiwi','lemon'))

def str_sorted_upper(*args):
    args = [a.upper() for a in args]
    return sorted(args)

print (str_sorted_upper('apple', 'orange', 'guava','cherry', 'blueberry', 'kiwi','lemon'))



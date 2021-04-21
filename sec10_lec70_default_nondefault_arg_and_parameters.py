# Arguments are of 2 types: Keyword and Non-keyword arguments 

# Non-Keyword Arguments - They do not have any keyword attached to them
def func(a,b):
    return a*b
    # Non-Keyword Arguments
print(func(5,6))

# Keyword Arguments - They have keywords attached to them. Also called positional arguments
def func (a,b):
    return a*b
    # Keyword / Positional arguments - Does not matter what positions they take
print (func(a=5,b=6))
print (func(b=6,a=5))
print (func(5, b=6))
    # This will generate an error - SyntaxError: positional argument follows keyword argument
#print (func(a=5,6))


# Default Parameters - Not Arguments but Parameters
def func (a, b=10):
    return a+b
    # Here you don't have to specify 'b' parameter as it is already set by default
print (func(5))
    # Here you can change the value of 'b' as per your requirement
print (func(5, b=15))
print (func(5,15))


# Default parameters cannot be before non-default parameters
def func(a=5,b):
    return a+b
    # This will throw an error
print (func(a,10))








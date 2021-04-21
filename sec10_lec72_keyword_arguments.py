# **kwargs - Only applicable with keyword arguments. It can take any number of arguments.

# Anything can be passed in **kwargs. 
# ** - here anything can be passed
# kwargs - it is used for convention but any variable can be used
# You cannot have non-keyword arguments here
# Only Keyword arguments are allowed


def keyword_args(**kwargs):
    return kwargs

    # It prints out a dictionary with keys and values. 
    # It will give an error if without keyword values are given
print (keyword_args(a=2, b=22, c=222))



l = [2,3,4,5,6,7]
del l[1:]
l
# How to get an item from a list
l = [2,3,4,5,6,7]
# Both yields the same value
l.__getitem__(-2)
l[-2]

def func(x):
    if len(x) < 8:
        return False
    elif len(x) >= 8:
        return True
        
x = 'Hallooooooooo'
    
print(func(x))




def temp(t):
    if t > 7:
        return 'Warm'
    elif t <= 7:
        return 'Cold'

t = -12
print (temp(t))




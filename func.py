def func(temp):
    if temp > 25:
        return 'Hot'
    elif temp >= 15 <= 25:
        return 'Warm'
    elif temp < 15:
        return 'Cold'
        
temp = 22
print (func(temp))
 
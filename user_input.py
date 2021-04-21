def yukon_temp(temp):
    if temp >= -5 and temp <= 0:
        return 'Cold'
    elif temp > 0 and temp <= 10:
        return 'Warm'
    elif temp > 10:
        return 'Hot'
    elif temp < -5:
        return 'Chilling'

user_input = float(input("What's the Temp today : "))

print (yukon_temp(user_input))
        
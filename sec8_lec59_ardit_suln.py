openings = ('why','how','where','when','what')

def func(sentence):
    input_details = sentence.capitalize()
    if sentence.startswith(openings):
        return f'{input_details}? '
    else:
        return f'{input_details}. '

#print (func('why are you dancing'))        

user_inputs = [ ]

while True:
    user_feed = input("Say Something: ")
    if user_feed == '/end':
        break
    elif user_feed != '/end':
       user_inputs.append(func(user_feed))

c = ' '.join(user_inputs)
print(c)
